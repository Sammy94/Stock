from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Stock
from .serializers import StockSerializer
# Create your views here.


#/Stocks

class StockList(APIView):

    def get(self,request):
        stock = Stock.objects.all()
        serializer = StockSerializer(stock,many=True)
        return Response(serializer.data)


