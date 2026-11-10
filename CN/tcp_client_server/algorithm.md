# Algorithm: Client-Server Communication using TCP Socket Programming

## Server Algorithm
1. **Socket Creation**:
   - Create a stream socket using `socket(AF_INET, SOCK_STREAM, 0)`.
   - Verify that the socket descriptor is valid ($> 0$).

2. **Socket Configuration**:
   - Set the socket option `SO_REUSEADDR` using `setsockopt()` to allow immediate reuse of the local address and port after termination.
   - Initialize a `sockaddr_in` structure with address family `AF_INET`, port `PORT` (converted using `htons()`), and IP address `INADDR_ANY` to accept connections on all local network interfaces.

3. **Binding & Listening**:
   - Bind the socket to the specified IP address and port using `bind()`.
   - Put the socket into listening mode with `listen(server_fd, backlog)`, setting a queue backlog of 5 pending connections.

4. **Accepting Connections & Communication**:
   - Enter an infinite loop to serve incoming client requests:
     - Block until a connection request arrives and accept it using `accept()`, generating a dedicated `client_socket`.
     - Retrieve and print client IP address and port using `inet_ntop()` and `ntohs()`.
     - Enter an inner communication loop:
       a. Receive message bytes from client via `recv()`.
       b. If received bytes $\le 0$, client disconnected; break from inner loop.
       c. Null-terminate the buffer and check for termination tokens (`"exit"` or `"quit"`).
       d. Process the client's payload (e.g., compute length, reverse string, convert to uppercase).
       e. Format structured acknowledgment string and transmit back to client using `send()`.
     - Close `client_socket` and wait for the next client.

5. **Termination**:
   - Close listening socket `server_fd` when shutting down.

---

## Client Algorithm
1. **Socket Creation**:
   - Create a TCP stream socket using `socket(AF_INET, SOCK_STREAM, 0)`.
   - Verify the descriptor returned.

2. **Server Address Setup**:
   - Initialize a `sockaddr_in` structure with `AF_INET` and target server port `PORT` (`htons()`).
   - Convert IPv4 server address string (`"127.0.0.1"`) to binary network byte order using `inet_pton()`.

3. **Connection Handshake**:
   - Establish TCP three-way handshake connection with the remote server using `connect()`.
   - Verify connection success; report error and terminate if unreachable.

4. **Communication Loop**:
   - Repeatedly prompt the user for input messages from standard input:
     - Read input string using `fgets()`, stripping newline characters.
     - Transmit message to server over the established connection using `send()`.
     - If the message equals `"exit"` or `"quit"`, optionally receive final goodbye message and break loop.
     - Block and wait for server response using `recv()`.
     - Null-terminate received buffer and display server output to console.

5. **Cleanup**:
   - Close socket descriptor using `close()`.
   - Terminate client execution with return status 0.
