from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import SumSerializer
from rest_framework.response import Response

class SumAPI(APIView):
    def post(self, request):
        serial=SumSerializer(data=request.data)
        if serial.is_valid():
            num1=serial.validated_data['number1']
            num2=serial.validated_data['number2']
            return Response({'answer':num1 + num2}, status=200)
        return Response(serial.errors, status=400)
    
