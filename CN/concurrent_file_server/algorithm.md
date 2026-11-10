# Algorithm: Concurrent File Server using TCP Sockets and Fork

## Server Algorithm
1. **Socket Setup & Address Configuration**:
   - Create a TCP stream socket using `socket(AF_INET, SOCK_STREAM, 0)`.
   - Set the `SO_REUSEADDR` socket option with `setsockopt()` to allow immediate address reuse.
   - Configure the server's `sockaddr_in` structure with `AF_INET`, `INADDR_ANY`, and port `PORT` (`htons()`).
   - Bind the socket to the network interface using `bind()`.
   - Transition the socket to passive listening mode using `listen(server_fd, backlog)`.

2. **Zombie Process Prevention**:
   - Configure a `SIGCHLD` signal handler with `sigaction()` utilizing `waitpid(-1, NULL, WNOHANG)`.
   - When any child process terminates, the non-blocking `waitpid()` call immediately reaps its exit status, preventing zombie / defunct processes in the process table.

3. **Concurrency Loop (`fork()`)**:
   - Loop indefinitely:
     - Accept an incoming client connection using `accept()`, obtaining a new client socket descriptor `client_socket`.
     - Spawn a child process using `fork()`:
       - **Parent Process**:
         - Closes its copy of `client_socket` immediately (responsibility delegated to child).
         - Re-enters `accept()` to listen for further incoming connections without blocking.
       - **Child Worker Process**:
         - Closes the master listening socket `server_fd` (not needed by worker).
         - Retrieves its unique process ID via `getpid()` and transmits it to the client with `send()`.
         - Reads the requested filename from the client using `recv()`.
         - Attempts to open the requested file in binary read mode (`fopen(filename, "rb")`).
         - If file is missing (`file == NULL`), sends an error string (`"ERROR: File not found on server."`).
         - If file exists, reads contents in chunks into a buffer (`fread()`) and streams each block across the network using `send()` until EOF is reached.
         - Closes the file descriptor (`fclose()`), closes `client_socket`, and terminates child execution with `exit(0)`.

---

## Client Algorithm
1. **Input & Socket Creation**:
   - Prompt the user to enter the target filename to request from the server.
   - Create a TCP stream socket using `socket(AF_INET, SOCK_STREAM, 0)`.

2. **Server Address Configuration**:
   - Initialize the `sockaddr_in` structure with address family `AF_INET`, server port `PORT`, and parse IPv4 address `"127.0.0.1"` into network byte order with `inet_pton()`.

3. **Connection & Concurrency Handshake**:
   - Establish TCP connection to the server using `connect()`.
   - Receive the server worker process PID via `recv()` and display it to verify multi-process concurrent servicing.

4. **File Request & Data Streaming**:
   - Send the target filename string to the server via `send()`.
   - Enter a data reception loop:
     - Read incoming chunks from the network byte stream using `recv()`.
     - While bytes received $> 0$, null-terminate the buffer and display/stream the received data to standard output.
     - When `recv()` returns 0 (indicating server has completed transfer and closed connection), exit loop.

5. **Cleanup**:
   - Close the client socket with `close()`.
   - Terminate execution.
