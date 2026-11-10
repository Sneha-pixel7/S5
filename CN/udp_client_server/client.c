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
    int sockfd;
    char buffer[BUFFER_SIZE];
    char message[BUFFER_SIZE];
    struct sockaddr_in servaddr;

    // 1. Create UDP datagram socket
    if ((sockfd = socket(AF_INET, SOCK_DGRAM, 0)) < 0) {
        perror("Socket creation failed");
        exit(EXIT_FAILURE);
    }

    // 2. Configure target server address
    memset(&servaddr, 0, sizeof(servaddr));
    servaddr.sin_family = AF_INET;
    servaddr.sin_port = htons(PORT);

    if (inet_pton(AF_INET, SERVER_IP, &servaddr.sin_addr) <= 0) {
        printf("Invalid address/ Address not supported: %s\n", SERVER_IP);
        close(sockfd);
        exit(EXIT_FAILURE);
    }

    // 3. Get message input from user
    printf("Enter message to send over UDP: ");
    if (fgets(message, sizeof(message), stdin) == NULL) {
        close(sockfd);
        return 0;
    }

    // Strip trailing newline character
    message[strcspn(message, "\r\n")] = '\0';

    if (strlen(message) == 0) {
        printf("Empty message. Exiting.\n");
        close(sockfd);
        return 0;
    }

    // 4. Send datagram directly to server (no handshake or connection needed)
    sendto(sockfd, (const char *)message, strlen(message), 0,
           (const struct sockaddr *)&servaddr, sizeof(servaddr));
    printf("Sent datagram to %s:%d\n", SERVER_IP, PORT);

    // 5. Receive response from server
    socklen_t len = sizeof(servaddr);
    int n = recvfrom(sockfd, (char *)buffer, BUFFER_SIZE - 1, 0,
                     (struct sockaddr *)&servaddr, &len);
    if (n < 0) {
        perror("recvfrom failed");
        close(sockfd);
        exit(EXIT_FAILURE);
    }
    buffer[n] = '\0';

    printf("\nServer Response: %s\n", buffer);

    // 6. Close socket
    close(sockfd);
    return 0;
}
