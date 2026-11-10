#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>

#define SERVER_IP "127.0.0.1"
#ifndef PORT
#define PORT 8080
#endif
#define BUFFER_SIZE 2048

int main() {
    int sock = 0;
    struct sockaddr_in serv_addr;
    char filename[BUFFER_SIZE];
    char buffer[BUFFER_SIZE];
    pid_t server_worker_pid;

    // 1. Prompt user for filename to request
    printf("Enter the filename to download from server: ");
    if (fgets(filename, sizeof(filename), stdin) == NULL) {
        return 0;
    }
    filename[strcspn(filename, "\r\n")] = '\0';

    if (strlen(filename) == 0) {
        printf("No filename provided. Exiting.\n");
        return 0;
    }

    // 2. Create TCP stream socket
    if ((sock = socket(AF_INET, SOCK_STREAM, 0)) < 0) {
        perror("Socket creation error");
        return -1;
    }

    // 3. Configure target server address
    memset(&serv_addr, 0, sizeof(serv_addr));
    serv_addr.sin_family = AF_INET;
    serv_addr.sin_port = htons(PORT);

    if (inet_pton(AF_INET, SERVER_IP, &serv_addr.sin_addr) <= 0) {
        printf("Invalid address or address format: %s\n", SERVER_IP);
        close(sock);
        return -1;
    }

    // 4. Connect to concurrent server
    printf("Connecting to concurrent server at %s:%d...\n", SERVER_IP, PORT);
    if (connect(sock, (struct sockaddr *)&serv_addr, sizeof(serv_addr)) < 0) {
        perror("Connection Failed");
        close(sock);
        return -1;
    }

    // 5. Receive worker child PID to demonstrate concurrency
    if (recv(sock, &server_worker_pid, sizeof(server_worker_pid), 0) > 0) {
        printf("[+] Connected! Handled by Server Worker PID: %d\n", server_worker_pid);
    }

    // 6. Transmit target filename to server
    send(sock, filename, strlen(filename), 0);
    printf("Requested file: '%s'\n\n--- File Content Received ---\n", filename);

    // 7. Receive and display streamed file content until EOF
    int bytes_received;
    int data_received = 0;

    while ((bytes_received = recv(sock, buffer, sizeof(buffer) - 1, 0)) > 0) {
        buffer[bytes_received] = '\0';
        printf("%s", buffer);
        data_received = 1;
    }
    printf("\n-----------------------------\n");

    if (!data_received) {
        printf("Server closed connection without sending data.\n");
    } else {
        printf("File transfer complete. Connection closed.\n");
    }

    // 8. Clean up and close socket
    close(sock);
    return 0;
}
