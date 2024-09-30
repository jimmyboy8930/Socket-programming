import socket # networking

def query_server(host='127.0.0.1', port=65432):
    
    # try helps when program doesn't go how we want
    try: 

        # create IPv4 and TCP socket
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            
            # connect to server
            s.connect((host, port))

            while True:
                
                # prompt the user for a query or 'quit' command
                query = input("Enter your query (e.g., 'a?t') or 'quit' to exit: ")
                
                # if 'quit' is entered, send 'quit' to server and break loop
                if query.lower() == 'quit':
                    s.sendall('quit'.encode())
                    break
                
                # send query to server
                s.sendall(query.encode() + b'\n')
                response = ""
                
                # loop to receive full response from the server
                while True:
                    part = s.recv(1024).decode()
                    response += part
                    # check for the end of the response 'EOF\n'
                    if part.endswith('EOF\n'):
                        break
                
                # print server response
                print(response)
    
    # if connection won't establish, print error message
    except ConnectionRefusedError:
        print("Connection refused. Is the server running?")

if __name__ == "__main__":
    query_server()
