from rest_framework.views import exception_handler


def custom_exception_handler(exc, context):
    print(f"custom_exception_handler ==> {exc}")
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = exception_handler(exc, context)

    # Now add the HTTP status code to the response.
    if response is not None:
        response.data['status_code'] = response.status_code
        response.data['test'] = 'exception_handler test'

    return response
