# Multi-Threaded Client-Server Application

## Project Overview

This project implements a multi-threaded client-server architecture using Python's **socket** library. The server can handle multiple client requests concurrently, thanks to the use of threads. The server processes wildcard search queries sent by the clients, performs the search on a given word list, and returns the results or appropriate error messages.

The project includes both single-threaded and multi-threaded server-client implementations to showcase the advantages of multi-threading in handling concurrent requests efficiently.

## Key Features

- **Multi-threaded Server**: The server can handle multiple client connections simultaneously by spawning a new thread for each client. This allows for better performance and user experience compared to the single-threaded version.
- **Wildcard Search**: Clients can search for patterns using wildcard characters (e.g., `?`) in the server's stored word list, and the server responds with matching results.
- **Reliable Data Transfer**: The project uses **TCP** (Transmission Control Protocol) for reliable data transmission between clients and the server.
- **EOF Signaling**: To signal the end of a message, the server appends an `EOF` marker to its responses, allowing the client to know when the server has finished sending data.
- **Cross-Platform**: The program does not depend on specific platform libraries, making it portable across different operating systems.

## File Descriptions

- **client.single.threaded.py**: The single-threaded client that connects to the server, sends search queries, and processes the server's responses one at a time.
- **client.multi.threaded.py**: The multi-threaded client version, capable of sending multiple requests concurrently.
- **server.single.threaded.py**: The single-threaded server version, which handles one client request at a time.
- **server.multi.threaded.py**: The multi-threaded server version, which can handle multiple client connections simultaneously using threads.

## How It Works

### Server-Side Functions

- **Search_words**: The server function that handles client search queries. It reads a stored wordlist (`wordlist.txt`), performs the search using Python's `re` (regular expression) library, and returns the results to the client.
- **Handle_client**: Manages the communication between the server and a connected client. This includes receiving a query, performing the search, and sending back the appropriate response (either the matched words or a `404 NOT FOUND` message). It also appends `EOF` to the responses to indicate the end of transmission.
- **Start_server**: Initializes the server, opens a socket connection, and listens for client requests. For the multi-threaded version, a new thread is created for each client connection.
  
### Client-Side Functions

- **Query_server**: The client-side function that sends search queries to the server. It waits for the server's response, processes it (including checking for the `EOF` marker), and loops until the user quits.

### Protocols and Formats

- **Message Format**: 
  - Client sends a query string containing wildcards (`?`) and waits for a response.
  - Server responds with either `200 OK` and the list of matches or `404 NOT FOUND` if no matches are found, followed by `EOF`.

## Trade-offs

- **Single-threaded vs Multi-threaded**:
  - **Single-threaded**: Simpler but inefficient, as only one client can be served at a time.
  - **Multi-threaded**: More complex but allows the server to handle multiple clients concurrently, improving scalability and performance.

## Future Enhancements

- **Support for Additional Wildcards**: Implement support for additional wildcard patterns like `*` for more flexible searches.
- **SSL/TLS Encryption**: Add SSL/TLS encryption to secure the communication between clients and the server.
- **Connection Pooling**: Limit the number of simultaneous threads and implement connection pooling for better resource management.
- **Web Interface**: Implement an HTTP interface for better accessibility, allowing users to connect via a web browser instead of using the terminal.
  
## Usage

### Prerequisites

- Python 3.x installed on your system.

### Running the Project

1. **Start the Server**:
   - For the single-threaded server:
     ```bash
     python3 server.single.threaded.py
     ```
   - For the multi-threaded server:
     ```bash
     python3 server.multi.threaded.py
     ```

2. **Start the Client**:
   - For the single-threaded client:
     ```bash
     python3 client.single.threaded.py
     ```
   - For the multi-threaded client:
     ```bash
     python3 client.multi.threaded.py
     ```

3. **Usage Example**:
   - Enter a wildcard search pattern (e.g., `he??o`) when prompted by the client.
   - The server will respond with matching words or a `404 NOT FOUND` message.
   - Type `quit` to close the client connection.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

This project demonstrates the effectiveness of multi-threaded architectures in networked applications, with a focus on concurrent request handling and reliable communication. It also highlights fundamental concepts like socket programming and thread management in Python.
