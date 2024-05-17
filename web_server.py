"""
Simple HTTP/1.0 server
"""
import sys
import concurrent.futures
import socket
from http import parse_request
from router import route_request_to

SERVER_HOST = '0.0.0.0'
SERVER_PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 8080

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((SERVER_HOST, SERVER_PORT))
server_socket.listen(1)

def process_request(conn):
    request_str = conn.recv(1024).decode()
    path, method, query_params, headers, payload = parse_request(request_str)
    response = route_request_to(path, method, query_params, headers, payload)
    conn.sendall(response.encode())
    conn.close()

while True:
    client_connection, client_address = server_socket.accept()

    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        executor.submit(process_request, client_connection)
