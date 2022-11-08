from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import exception_handler

def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if response is not None:
        custom_response_data={
            'error': True,
            'data':{},
            'message': exc.detail,
        }

        if response.status_code == 200:
            Response(custom_response_data,status=status.HTTP_400_BAD_REQUEST)

        return Response(custom_response_data,status=response.status_code)
        
    else:
        return Response({
            'error': True,
            'data':{},
            'message': str(exc),
        }, status=status.HTTP_400_BAD_REQUEST)