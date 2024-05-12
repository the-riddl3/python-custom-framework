import json
import re


def parse_request(request_str: str):
    header_str, payload_str = split_request(request_str)
    header_lines = split_header_by_lines(header_str)
    headers = header_lines_to_dict(header_lines[1:])
    method, path, protocol = header_lines[0].split()
    path, query_params = split_path_and_query_params(path)
    payload = parse_payload(headers, payload_str)
    return path, method, query_params, headers, payload

def parse_payload(headers: dict, payload_str: str):
    content_type = headers['Content-Type'] if 'Content-Type' in headers else None
    match content_type:
        case _:
            return json.loads(payload_str) if payload_str else {}

def match_response(headers: dict, payload: dict):
    accept = headers['Accept'] if 'Accept' in headers else None
    match accept:
        case _:
            return json_response(payload)

def json_response(payload: dict) -> str:
    return f'HTTP/1.0 200 OK\nContent-Type: application/json\n\n{json.dumps(payload)}'

def split_path_and_query_params(path: str) -> (str, dict):
    path_arr = path.split('?')
    if len(path_arr) < 2:
        return path, {}
    path_only = path_arr[0]
    query_param_str = path.split('?')[1]
    query_params = dict(param.split('=') for param in query_param_str.split('&'))
    return path_only, query_params

def header_lines_to_dict(header_lines: list[str]) -> dict:
    header_strs = list(filter(lambda header: ':' in header, header_lines))
    return dict(header.split(': ') for header in header_strs)

def split_header_by_lines(header_str: str):
    return list(filter(lambda line: line, re.split('(?:\n|\r|\r\n)', header_str)))

def split_request(request_str: str):
    return re.split('(?:\n\n|\r\r|\r\n\r\n)', request_str)
