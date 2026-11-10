# Algorithm: Client-Server Communication using UDP Socket Programming

## Server Algorithm
1. **Socket Creation**:
   - Create a connectionless datagram socket using `socket(AF_INET, SOCK_DGRAM, 0)`.
   - Validate the returned socket descriptor.

2. **Address Binding**:
   - Initialize the `sockaddr_in` structure for the server: set address family to `AF_INET`, port to `PORT` using `htons()`, and IP address to `INADDR_ANY`.
   - Bind the datagram socket to the local address using `bind()`.

3. **Receive & Process Loop**:
   - Loop indefinitely to handle arriving client datagrams:
     - Clear the input buffer.
     - Block until a datagram arrives from any client using `recvfrom()`, capturing the sender's address structure (`cliaddr`) and address length (`len`).
     - Null-terminate the received message and log the sender's IP and port (`inet_ntop()`, `ntohs()`).
     - Analyze the message payload (e.g., compute character length, count vowels, convert to uppercase).
     - Format the response string.

4. **Response Transmission**:
   - Transmit the processed response back to the client's captured address using `sendto()`.

5. **Shutdown**:
   - Close the datagram socket with `close()` when stopping the server.

---

## Client Algorithm
1. **Socket Creation**:
   - Create a UDP datagram socket using `socket(AF_INET, SOCK_DGRAM, 0)`.
   - Validate socket initialization.

2. **Server Address Specification**:
   - Populate the server's `sockaddr_in` structure with family `AF_INET`, destination port `PORT` (`htons()`), and target IP (`"127.0.0.1"`) using `inet_pton()`.

3. **Input & Transmission**:
   - Prompt the user to enter a text message from standard input via `fgets()`.
   - Strip newline characters and check message validity.
   - Transmit the message directly in a single UDP datagram using `sendto()`, specifying the server's address structure. Note: No prior connection handshake is established.

4. **Reception & Output**:
   - Block and wait for the server's reply datagram using `recvfrom()`.
   - Null-terminate the received byte stream.
   - Display the response received from the server on the console.

5. **Cleanup**:
   - Close the client socket with `close()`.
   - Terminate execution cleanly.
