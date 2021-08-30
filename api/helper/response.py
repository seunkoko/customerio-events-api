def response_message(
        status='success',
        status_code=200,
        message='Successful request',
        data={}):
    return {
        'status': status,
        'message': message,
        'data': data
    }, status_code
