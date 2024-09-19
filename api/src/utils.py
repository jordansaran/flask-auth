""""Utilities to API"""
def httpstatus_to_api_response(http_status: tuple = None) -> dict | None:
    """Convert tuple from HTTPStatus to ApiResponse(dict)"""
    if http_status is None:
        return None
    try:
        return {
            'code': http_status[0],
            'type': http_status[1],
            'message': http_status[2],
        }
    except AttributeError as _error:
        return None
