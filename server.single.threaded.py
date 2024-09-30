import socket  # networking libraries
import re  # expression matching

def search_words(query_pattern):
    
    # open file and read
    with open('wordlist.txt') as f:
        words = f.readlines()
    
    # convert queries into expression replace '?' with '.'
    # '$' to match the entire word, not just a substring
    pattern = re.compile(query_pattern.replace('?', '.') + '$', re.IGNORECASE)
    
    # filter list of words to find matches
    matches = [word.strip() for word in words if pattern.match(word.strip())]
    return matches

def handle_client(conn, addr):
    
    print(f"Connected by {addr}")
    
    # keep connection open loop
    while True:
        # get data from the client
        data = conn.recv(1024).decode().strip()
        
        # if no data is received, close
        if not data:
            print("No data received. Closing connection.")
            break

        # print the query for server side knowledge
        print(f"Query: {data}")
        
        # search for matching words
        matches = search_words(data)
        
        # prepare a response if matches were found
        if matches:
            response = "200 OK\n" + "\n".join(matches)
        else:
            response = "404 NOT FOUND\n"
        
        # send response to client
        conn.sendall(response.encode())
    
    # close connection when done
    conn.close()

def start_server(host='127.0.0.1', port=65432):
    
    # create a socket using IPv4 and TCP 
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        
        # bind the socket to a host and port
        s.bind((host, port))
        
        # listen for incoming connections
        s.listen()
        
        print(f"Server started. Listening on {host}:{port}")
        
        # wait to accept a connection
        conn, addr = s.accept()
        
        # handle client connection, one time use because single threaded
        handle_client(conn, addr)

# start program
if __name__ == "__main__":
    start_server()
