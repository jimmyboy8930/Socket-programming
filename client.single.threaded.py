import socket # networking

def query_server(query, host='127.0.0.1', port=65432):
    
    # try helps when program doesn't go how we want
    try: 
        
        # create IPv4 and TCP socket
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            
            # connect to server
            s.connect((host, port))
            
            # send query to server and append a newline
            s.sendall(query.encode() + b'\n')
            
            # wait for and receive server respose then print
            response = s.recv(1024).decode()
            print(response)
    
    # if connection won't established then print an error message
    except ConnectionRefusedError:
        print("Connection refused. Is the server running?")

# program start
if __name__ == "__main__":
    
    # get input query
    query = input("Enter your query (e.g., 'a?t'): ")
    
    # pass query to function that queries server
    query_server(query)
