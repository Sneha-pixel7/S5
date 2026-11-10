# Client-Server Communication using TCP Socket Programming

## What is this experiment all about?
**TCP (Transmission Control Protocol)** is a connection-oriented, reliable transport layer protocol. Before any application data can travel across the network, the client and server must establish an explicit virtual circuit through the **TCP Three-Way Handshake** (`SYN` $\rightarrow$ `SYN-ACK` $\rightarrow$ `ACK`). 

Once connected, TCP guarantees:
- **Reliable in-order delivery**: Bytes arrive in the exact order sent without loss or duplication.
- **Flow and Congestion Control**: Dynamically throttles transmission rates to prevent buffer overflows and network saturation.
- **Connection persistence**: The communication channel remains open for interactive exchanges until either endpoint explicitly closes it (`FIN`/`ACK`).

This experiment demonstrates a classic two-way interactive client-server architecture:
- The client connects to the server and transmits arbitrary text messages.
- The server logs the connection details (remote IP address and ephemeral port), computes statistics (string length), performs a data transformation (reversing the string and converting characters to uppercase), and transmits the structured reply back to the client.
- The session continues interactively until the client types `exit` or `quit`.

## What is the code actually doing?
1. **Server (`server.c`)**:
   - Creates a stream socket (`SOCK_STREAM`) bound to port `8080`.
   - Uses `setsockopt(SO_REUSEADDR)` to avoid `Address already in use` bind errors upon restarting.
   - Puts the socket into passive listening mode with `listen()`.
   - Accepts client connections with `accept()`, printing client IP and port via `inet_ntop()`.
   - Reads incoming data continuously via `recv()`.
   - Transforms received text (length calculation, reverse indexing, uppercase conversion via `toupper()`).
   - Transmits acknowledgment responses back via `send()`.
   - Gracefully tears down individual client connections when an `exit` command is received or when the client disconnects.
2. **Client (`client.c`)**:
   - Creates a stream socket (`SOCK_STREAM`) and parses the target server IP (`127.0.0.1`) via `inet_pton()`.
   - Initiates the TCP three-way handshake using `connect()`.
   - Enters an interactive terminal loop reading user input with `fgets()`.
   - Sends messages to the server using `send()`.
   - Receives transformed acknowledgments using `recv()` and displays them on the console.
   - Terminates cleanly upon entering `exit` or `quit`.

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
   client> Hello Computer Networks!
   ```
   *Example output*:
   ```text
   server> ACK [Length: 25 | Uppercase & Reversed: "!SKROWTEN RETUPMOC OLLEH"]
   ```
   *Example exit*:
   ```text
   client> exit
   server> Goodbye! Connection closed by server.
   Connection closed.
   ```
