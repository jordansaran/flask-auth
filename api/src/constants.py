from api.src.utils import httpstatus_to_api_response


class StatusAPI:
    INTERNAL_SERVER_ERROR_API = httpstatus_to_api_response((
        500,
        "Internal Server Error",
        "Server got itself in trouble",
    ))
    REQUEST_SUCCESS_API = httpstatus_to_api_response((
        204,
        'Requisição executado com sucesso.',
        'A requisição executou corretamente sua função.'
    ))
    REQUEST_NOT_FOUND_API = httpstatus_to_api_response((
        404,
        'Objeto não encontrado.',
        'O objetivo não foi encontrado na base de dados.'
    ))
    BAD_REQUEST_API = httpstatus_to_api_response((
        400,
        'Bad Request',
        'Bad request syntax or unsupported method'
    ))
    UNAUTHORIZED = httpstatus_to_api_response((
        401,
        'Unauthorized',
        'No permission -- see authorization schemes'
    ))
    UNENVIRONMENT = httpstatus_to_api_response((
        401,
        'UNENVIRONMENT',
        'type environment not found'
    ))
