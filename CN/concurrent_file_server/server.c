#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <signal.h>

#ifndef PORT
#define PORT 8080
#endif
#define BUFFER_SIZE 2048

// Signal handler to reap zombie child processes asynchronously
void sigchld_handler(int s) {
    (void)s; // Suppress unused parameter warning
    // waitpid with WNOHANG reaps all dead child processes without blocking
    while (waitpid(-1, NULL, WNOHANG) > 0);
}

// Function executed by each child process to handle an individual client
void handle_client(int client_socket, struct sockaddr_in client_addr) {
    char filename[512];
    char buffer[BUFFER_SIZE];
    FILE *file;
    pid_t my_pid = getpid();
    char client_ip[INET_ADDRSTRLEN];

    inet_ntop(AF_INET, &client_addr.sin_addr, client_ip, sizeof(client_ip));
    printf("[Worker PID %d] Serving client %s:%d\n", my_pid, client_ip, ntohs(client_addr.sin_port));

    // 1. Send the child worker's PID to client for concurrency verification
    if (send(client_socket, &my_pid, sizeof(my_pid), 0) < 0) {
        perror("Failed to send PID");
        close(client_socket);
        exit(EXIT_FAILURE);
    }

    // 2. Receive requested filename from client
    memset(filename, 0, sizeof(filename));
    int bytes_received = recv(client_socket, filename, BUFFER_SIZE - 1, 0);
    if (bytes_received <= 0) {
        printf("[Worker PID %d] Client closed connection prematurely.\n", my_pid);
        close(client_socket);
        exit(0);
    }

    filename[bytes_received] = '\0';
    // Strip trailing carriage return and newline characters
    filename[strcspn(filename, "\r\n")] = '\0';
    printf("[Worker PID %d] Client requested file: '%s'\n", my_pid, filename);

    // 3. Attempt to open requested file in binary read mode
    file = fopen(filename, "rb");
    if (file == NULL) {
        printf("[Worker PID %d] File '%s' not found. Notifying client.\n", my_pid, filename);
        snprintf(buffer, sizeof(buffer), "ERROR: File '%s' not found on server.\n", filename);
        send(client_socket, buffer, strlen(buffer), 0);
    } else {
        printf("[Worker PID %d] File '%s' opened. Streaming data...\n", my_pid, filename);
        size_t bytes_read;
        while ((bytes_read = fread(buffer, 1, sizeof(buffer), file)) > 0) {
            if (send(client_socket, buffer, bytes_read, 0) < 0) {
                perror("Socket send error during file streaming");
                break;
            }
        }
        fclose(file);
        printf("[Worker PID %d] File transfer completed successfully.\n", my_pid);
    }

    // 4. Close client socket and exit child worker process
    close(client_socket);
    exit(0);
}

int main() {
    int server_fd, client_socket;
    struct sockaddr_in server_addr, client_addr;
    socklen_t addr_len = sizeof(client_addr);
    int opt = 1;
    struct sigaction sa;

    // 1. Create TCP stream socket
    if ((server_fd = socket(AF_INET, SOCK_STREAM, 0)) < 0) {
        perror("Socket creation failed");
        exit(EXIT_FAILURE);
    }

    // 2. Set socket options to reuse address and port
    if (setsockopt(server_fd, SOL_SOCKET, SO_REUSEADDR, &opt, sizeof(opt)) < 0) {
        perror("setsockopt failed");
        close(server_fd);
        exit(EXIT_FAILURE);
    }

    // 3. Configure server address structure
    memset(&server_addr, 0, sizeof(server_addr));
    server_addr.sin_family = AF_INET;
    server_addr.sin_addr.s_addr = INADDR_ANY;
    server_addr.sin_port = htons(PORT);

    // 4. Bind socket to designated port
    if (bind(server_fd, (struct sockaddr *)&server_addr, sizeof(server_addr)) < 0) {
        perror("Bind failed");
        close(server_fd);
        exit(EXIT_FAILURE);
    }

    // 5. Put socket into listening state
    if (listen(server_fd, 10) < 0) {
        perror("Listen failed");
        close(server_fd);
        exit(EXIT_FAILURE);
    }

    // 6. Register SIGCHLD signal handler to prevent zombie processes
    sa.sa_handler = sigchld_handler;
    sigemptyset(&sa.sa_mask);
    sa.sa_flags = SA_RESTART; // Automatically restart interrupted system calls
    if (sigaction(SIGCHLD, &sa, NULL) == -1) {
        perror("sigaction error");
        close(server_fd);
        exit(EXIT_FAILURE);
    }

    printf("Concurrent TCP File Server listening on port %d...\n", PORT);

    // 7. Master connection loop
    while (1) {
        if ((client_socket = accept(server_fd, (struct sockaddr *)&client_addr, &addr_len)) < 0) {
            perror("Accept failed");
            continue;
        }

        // Fork a child process to handle client concurrently
        pid_t pid = fork();

        if (pid < 0) {
            perror("Fork failed");
            close(client_socket);
        } else if (pid == 0) {
            // Child process: closes listener socket, handles client, then exits
            close(server_fd);
            handle_client(client_socket, client_addr);
        } else {
            // Parent process: closes connected client socket and resumes listening
            close(client_socket);
        }
    }

    close(server_fd);
    return 0;
}
