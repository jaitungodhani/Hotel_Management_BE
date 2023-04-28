from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status
import logging

logger = logging.getLogger(__file__)

def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)
    logger.error(str(exc))
    response_data = {
            'error' : True,
            'data'  : {},
            'message' : str(exc)
        }

    if response is not None:
        return Response(response_data, status=response.status_code)
    else:
        return Response(response_data, status=status.HTTP_400_BAD_REQUEST)