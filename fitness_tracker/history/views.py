from django.shortcuts import render

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import History
from .serializers import HistorySerializer

class HistoryListAPIView(APIView):
    def get(self, request):
        histories = History.objects.all()
        serializer = HistorySerializer(histories, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = HistorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class HistoryDetailAPIView(APIView):
    def get(self, request, pk):
        history = History.objects.get(pk=pk)
        serializer = HistorySerializer(history)
        return Response(serializer.data)

    def put(self, request, pk):
        history = History.objects.get(pk=pk)
        serializer = HistorySerializer(history, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        history = History.objects.get(pk=pk)
        history.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)