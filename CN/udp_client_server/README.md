# Client-Server Communication using UDP Socket Programming

## What is this experiment all about?
**UDP (User Datagram Protocol)** is a lightweight, **connectionless** transport layer protocol. Unlike TCP, UDP does not establish a formal three-way handshake prior to data transfer, nor does it maintain connection state or provide retransmissions and flow control.

Key characteristics of UDP include:
- **Connectionless transmission**: Communication takes place directly by wrapping messages into independent packets (datagrams) using `sendto()` and receiving them with `recvfrom()`.
- **Low latency & minimal overhead**: Without handshakes, acknowledgments, or sequence tracking headers (UDP header is only 8 bytes vs TCP's 20+ bytes), UDP is suited for real-time applications like DNS, VoIP, streaming, and gaming.
- **Message boundary preservation**: Unlike TCP byte streams, each UDP `recvfrom()` call reads exactly one datagram sent by a corresponding `sendto()`.

This experiment demonstrates a request-response client-server architecture using UDP sockets:
- The client prompts the user for a text message and sends it to the server in a single datagram.
- The server captures the message and the client's endpoint address, inspects the text (calculating total character length, counting vowels, and converting characters to uppercase), and fires the analyzed result back to the client using `sendto()`.

## What is the code actually doing?
1. **Server (`server.c`)**:
   - Opens a UDP datagram socket with `SOCK_DGRAM`.
   - Binds to local port `8080` with `bind()`.
   - Loops indefinitely on `recvfrom()`, capturing both the payload and the sender's client `sockaddr_in`.
   - Logs the client's IP and port via `inet_ntop()`.
   - Processes the string (calculating total length, vowel frequency, and uppercase transformation).
   - Transmits the structured reply back to the sender's network endpoint with `sendto()`.
2. **Client (`client.c`)**:
   - Opens a UDP socket (`SOCK_DGRAM`).
   - Configures the destination address (`127.0.0.1:8080`) using `inet_pton()`.
   - Prompts the user for a sentence and sends it directly using `sendto()`.
   - Awaits the datagram response via `recvfrom()` and displays the server analysis.
   - Closes the socket cleanly.

## How to compile and run
1. Compile both files:
   ```bash
   gcc -Wall -Wextra server.c -o server
   gcc -Wall -Wextra client.c -o client
   ```
2. Start the server in the first terminal:
   ```bash
   ./server
   ```
3. In another terminal, run the client:
   ```bash
   ./client
   ```
   *Example input*:
   ```text
   Enter message to send over UDP: networking is fascinating!
   ```
   *Example output*:
   ```text
   Sent datagram to 127.0.0.1:8080

   Server Response: UDP-ACK [Length: 26 | Vowels: 8 | Uppercase: "NETWORKING IS FASCINATING!"]
   ```
