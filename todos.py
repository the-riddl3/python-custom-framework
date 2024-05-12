from http import json_response, match_response


def get_todos(query_params: dict, headers: dict, payload: dict):
    return match_response(headers, {"message": "Why are you trying to read my todo list bruh"})

