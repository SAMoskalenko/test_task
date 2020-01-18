from rest_framework.exceptions import APIException
from rest_framework import status as http_status


class EventException(APIException):
    default_detail = 'undefined'
    default_code = 'undefined'

    def __init__(self, detail, status, code):
        super().__init__(detail=detail, code=code)
        self.status_code = status


ERR_WRONG_EVENT = {
    'code': 400,
    'detail': "Событие не существуют",
    'status': http_status.HTTP_400_BAD_REQUEST
}

ERR_BUYING = {
    'code': 400,
    'detail': "Не достаточно билетов",
    'status': http_status.HTTP_400_BAD_REQUEST
}
