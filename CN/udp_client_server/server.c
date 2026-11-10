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

// Analyze message: compute length, count vowels, and convert to uppercase
void analyze_message(const char *input, char *upper_output, size_t *char_count, int *vowel_count) {
    size_t len = strlen(input);
    *char_count = len;
    *vowel_count = 0;

    for (size_t i = 0; i < len; i++) {
        char ch = input[i];
        upper_output[i] = toupper((unsigned char)ch);
        char lower = tolower((unsigned char)ch);
        if (lower == 'a' || lower == 'e' || lower == 'i' || lower == 'o' || lower == 'u') {
            (*vowel_count)++;
        }
    }
    upper_output[len] = '\0';
}

int main() {
    int sockfd;
    char buffer[BUFFER_SIZE];
    char upper_text[BUFFER_SIZE];
    char response[BUFFER_SIZE * 2];
    struct sockaddr_in servaddr, cliaddr;
    socklen_t len;

    // 1. Create UDP datagram socket
    if ((sockfd = socket(AF_INET, SOCK_DGRAM, 0)) < 0) {
        perror("Socket creation failed");
        exit(EXIT_FAILURE);
    }

    // 2. Configure server address structure
    memset(&servaddr, 0, sizeof(servaddr));
    memset(&cliaddr, 0, sizeof(cliaddr));

    servaddr.sin_family = AF_INET;
    servaddr.sin_addr.s_addr = INADDR_ANY; // Bind to any available local interface
    servaddr.sin_port = htons(PORT);

    // 3. Bind socket to server IP and port
    if (bind(sockfd, (const struct sockaddr *)&servaddr, sizeof(servaddr)) < 0) {
        perror("Bind failed");
        close(sockfd);
        exit(EXIT_FAILURE);
    }

    printf("UDP Server listening on port %d...\n", PORT);

    // 4. Infinite loop to process datagrams
    while (1) {
        len = sizeof(cliaddr);
        memset(buffer, 0, sizeof(buffer));

        // Block until a datagram arrives from any client
        int n = recvfrom(sockfd, (char *)buffer, BUFFER_SIZE - 1, 0,
                         (struct sockaddr *)&cliaddr, &len);
        if (n < 0) {
            perror("recvfrom failed");
            continue;
        }
        buffer[n] = '\0';
        buffer[strcspn(buffer, "\r\n")] = '\0';

        char client_ip[INET_ADDRSTRLEN];
        inet_ntop(AF_INET, &cliaddr.sin_addr, client_ip, sizeof(client_ip));
        printf("\n[Datagram Received] From %s:%d\n", client_ip, ntohs(cliaddr.sin_port));
        printf("Client Message: \"%s\"\n", buffer);

        // Process message
        size_t char_count = 0;
        int vowel_count = 0;
        analyze_message(buffer, upper_text, &char_count, &vowel_count);

        // Construct server response
        snprintf(response, sizeof(response),
                 "UDP-ACK [Length: %zu | Vowels: %d | Uppercase: \"%s\"]",
                 char_count, vowel_count, upper_text);

        // Send reply directly back to sender's address
        sendto(sockfd, (const char *)response, strlen(response), 0,
               (const struct sockaddr *)&cliaddr, len);
        printf("Sent response back to %s:%d\n", client_ip, ntohs(cliaddr.sin_port));
    }

    close(sockfd);
    return 0;
}
