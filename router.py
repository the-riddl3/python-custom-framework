from http import match_response
from todos import get_todos

routes = {
    "GET": {
        "/todos": get_todos
    }
}

def route_request_to(path: str, method: str, query_params: dict, headers: dict, payload: dict):
    if method in routes and path in routes[method]:
        return routes[method][path](query_params, headers, payload)
    return match_response(headers, {"message": "Route not found"})