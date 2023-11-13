from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView

# Create your views here.


class TestResponse(GenericAPIView):

    def get(self, request):
        return Response({'msg': 'Test Response.'}, status.HTTP_200_OK)
