"""
Simple HTTP/1.0 server
"""
import socket
from http import parse_request
from router import route_request_to

SERVER_HOST = '0.0.0.0'
SERVER_PORT = 8000

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((SERVER_HOST, SERVER_PORT))
server_socket.listen(1)

while True:
    client_connection, client_address = server_socket.accept()
    request_str = client_connection.recv(1024).decode()

    path, method, query_params, headers, payload = parse_request(request_str)
    response = route_request_to(path, method, query_params, headers, payload)

    client_connection.sendall(response.encode())
    client_connection.close()

