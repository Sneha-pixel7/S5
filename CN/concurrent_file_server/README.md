# Concurrent File Server (Fork-based Multi-client Architecture)

## What is this experiment all about?
In an iterative server, incoming client requests are handled one at a time. If a client initiates a large file transfer, all other clients are forced to wait in a pending queue until the previous client finishes. To provide high availability and scalability, production servers must be **concurrent**—capable of serving multiple simultaneous clients in parallel.

This experiment implements a **multi-process concurrent TCP file server** in C using the Unix `fork()` system call:
- The master parent process listens continuously for incoming connection requests on port `8080`.
- Upon accepting a connection via `accept()`, the parent process calls `fork()`, duplicating its execution context.
- The child process inherits the connected client socket, handles the requested file transfer, and terminates independently.
- The parent process immediately closes its duplicate client socket descriptor and returns to listening for other connections without waiting for the child to finish.
- To avoid accumulating zombie (defunct) processes in the OS process table, an asynchronous `SIGCHLD` signal handler reaps terminated child exit statuses using `waitpid(-1, NULL, WNOHANG)`.

## What is the code actually doing?
1. **Server (`server.c`)**:
   - Binds a stream socket (`SOCK_STREAM`) to port `8080` with `SO_REUSEADDR`.
   - Sets up a non-blocking `SIGCHLD` handler (`sigaction`) with `SA_RESTART` and `waitpid()`.
   - Iteratively accepts incoming connections and branches execution using `fork()`.
   - **Child Worker**:
     - Closes master `server_fd`.
     - Sends its process ID (`PID`) to the client so the client can verify which worker process is serving it.
     - Receives the requested filename from the client.
     - Opens the file using `fopen(..., "rb")`.
     - Streams file contents across the network in 2048-byte chunks using `fread()` and `send()`.
     - If the file does not exist, sends an error message: `"ERROR: File '<name>' not found on server."`
     - Closes file and socket, then cleanly exits via `exit(0)`.
   - **Parent**:
     - Closes the client socket descriptor (`close(client_socket)`) and immediately loops back to `accept()`.
2. **Client (`client.c`)**:
   - Prompts the user for a filename to request.
   - Connects to the server over TCP port `8080` using `connect()`.
   - Reads and displays the PID of the server worker child process.
   - Sends the target filename via `send()`.
   - Streams incoming bytes using `recv()` in a loop and prints the file contents directly to standard output until EOF.
   - Closes the connection cleanly.

## How to compile and run
1. Compile both files:
   ```bash
   gcc -Wall -Wextra server.c -o server
   gcc -Wall -Wextra client.c -o client
   ```
2. Start the concurrent server:
   ```bash
   ./server
   ```
3. In another terminal (or multiple terminals simultaneously), run the client:
   ```bash
   ./client
   ```
   *Example input*: Enter `server.c` to have the concurrent server stream its own source code back to you!
   *Example output*:
   ```text
   Connecting to concurrent server at 127.0.0.1:8080...
   [+] Connected! Handled by Server Worker PID: 42189
   Requested file: 'server.c'

   --- File Content Received ---
   #include <stdio.h>
   #include <stdlib.h>
   ...
   -----------------------------
   File transfer complete. Connection closed.
   ```
