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
    char message[BUFFER_SIZE];
    char buffer[BUFFER_SIZE];

    // 1. Create TCP stream socket
    if ((sock = socket(AF_INET, SOCK_STREAM, 0)) < 0) {
        perror("Socket creation error");
        return -1;
    }

    // 2. Configure target server address
    memset(&serv_addr, 0, sizeof(serv_addr));
    serv_addr.sin_family = AF_INET;
    serv_addr.sin_port = htons(PORT);

    // Convert IPv4 address from text to binary form
    if (inet_pton(AF_INET, SERVER_IP, &serv_addr.sin_addr) <= 0) {
        printf("Invalid address or address not supported: %s\n", SERVER_IP);
        close(sock);
        return -1;
    }

    // 3. Establish TCP connection with server
    printf("Connecting to TCP server at %s:%d...\n", SERVER_IP, PORT);
    if (connect(sock, (struct sockaddr *)&serv_addr, sizeof(serv_addr)) < 0) {
        perror("Connection Failed");
        close(sock);
        return -1;
    }

    printf("Connected successfully! Type your messages below.\n");
    printf("(Type 'exit' or 'quit' to terminate the session)\n\n");

    // 4. Interactive communication loop
    while (1) {
        printf("client> ");
        if (fgets(message, sizeof(message), stdin) == NULL) {
            break;
        }

        // Strip trailing newline character
        message[strcspn(message, "\r\n")] = '\0';

        // Skip empty lines
        if (strlen(message) == 0) {
            continue;
        }

        // Send message to server
        if (send(sock, message, strlen(message), 0) < 0) {
            perror("Send failed");
            break;
        }

        // Check if user entered exit command
        if (strcmp(message, "exit") == 0 || strcmp(message, "quit") == 0) {
            // Read optional goodbye acknowledgment before terminating
            int bytes_read = recv(sock, buffer, BUFFER_SIZE - 1, 0);
            if (bytes_read > 0) {
                buffer[bytes_read] = '\0';
                printf("server> %s\n", buffer);
            }
            break;
        }

        // Receive response from server
        memset(buffer, 0, sizeof(buffer));
        int bytes_read = recv(sock, buffer, BUFFER_SIZE - 1, 0);
        if (bytes_read <= 0) {
            printf("\nServer disconnected.\n");
            break;
        }

        buffer[bytes_read] = '\0';
        printf("server> %s\n\n", buffer);
    }

    // 5. Close socket
    close(sock);
    printf("Connection closed.\n");
    return 0;
}
