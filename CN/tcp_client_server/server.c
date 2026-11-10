#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <ctype.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>

#ifndef PORT
#define PORT 8080
#endif
#define BUFFER_SIZE 2048

// Process incoming message: reverse string and convert to uppercase
void process_message(const char *input, char *output, size_t *char_count) {
    size_t len = strlen(input);
    *char_count = len;

    for (size_t i = 0; i < len; i++) {
        output[i] = toupper((unsigned char)input[len - 1 - i]);
    }
    output[len] = '\0';
}

int main() {
    int server_fd, client_socket;
    struct sockaddr_in server_addr, client_addr;
    socklen_t client_len = sizeof(client_addr);
    int opt = 1;
    char buffer[BUFFER_SIZE];
    char processed[BUFFER_SIZE];
    char response[BUFFER_SIZE * 2];

    // 1. Create TCP stream socket
    if ((server_fd = socket(AF_INET, SOCK_STREAM, 0)) < 0) {
        perror("Socket creation failed");
        exit(EXIT_FAILURE);
    }

    // 2. Set socket options to reuse address and port immediately after restart
    if (setsockopt(server_fd, SOL_SOCKET, SO_REUSEADDR, &opt, sizeof(opt)) < 0) {
        perror("setsockopt failed");
        close(server_fd);
        exit(EXIT_FAILURE);
    }

    // 3. Configure server address structure
    memset(&server_addr, 0, sizeof(server_addr));
    server_addr.sin_family = AF_INET;
    server_addr.sin_addr.s_addr = INADDR_ANY; // Bind to all local interfaces
    server_addr.sin_port = htons(PORT);

    // 4. Bind socket to designated IP and Port
    if (bind(server_fd, (struct sockaddr *)&server_addr, sizeof(server_addr)) < 0) {
        perror("Bind failed");
        close(server_fd);
        exit(EXIT_FAILURE);
    }

    // 5. Listen for incoming client connections (backlog queue of 5)
    if (listen(server_fd, 5) < 0) {
        perror("Listen failed");
        close(server_fd);
        exit(EXIT_FAILURE);
    }

    printf("TCP Server listening on port %d...\n", PORT);

    // 6. Iterative server loop
    while (1) {
        printf("\nWaiting for an incoming connection...\n");

        if ((client_socket = accept(server_fd, (struct sockaddr *)&client_addr, &client_len)) < 0) {
            perror("Accept failed");
            continue;
        }

        char client_ip[INET_ADDRSTRLEN];
        inet_ntop(AF_INET, &client_addr.sin_addr, client_ip, sizeof(client_ip));
        printf("[+] Client connected from %s:%d\n", client_ip, ntohs(client_addr.sin_port));

        // Communication loop with connected client
        while (1) {
            memset(buffer, 0, sizeof(buffer));
            int bytes_read = recv(client_socket, buffer, BUFFER_SIZE - 1, 0);

            if (bytes_read <= 0) {
                // Client disconnected or error occurred
                printf("[-] Client %s:%d disconnected.\n", client_ip, ntohs(client_addr.sin_port));
                break;
            }

            buffer[bytes_read] = '\0';
            // Strip trailing newline/carriage return characters
            buffer[strcspn(buffer, "\r\n")] = '\0';

            // Check if client wishes to end communication
            if (strcmp(buffer, "exit") == 0 || strcmp(buffer, "quit") == 0) {
                printf("[-] Client %s:%d requested disconnect ('%s').\n", client_ip, ntohs(client_addr.sin_port), buffer);
                const char *bye_msg = "Goodbye! Connection closed by server.";
                send(client_socket, bye_msg, strlen(bye_msg), 0);
                break;
            }

            printf("[Client -> Server]: \"%s\"\n", buffer);

            // Process message (reverse and uppercase transformation)
            size_t char_count = 0;
            process_message(buffer, processed, &char_count);

            snprintf(response, sizeof(response),
                     "ACK [Length: %zu | Uppercase & Reversed: \"%s\"]",
                     char_count, processed);

            printf("[Server -> Client]: Sending response\n");
            send(client_socket, response, strlen(response), 0);
        }

        close(client_socket);
    }

    close(server_fd);
    return 0;
}
