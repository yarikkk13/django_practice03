from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.
class PCCreateListView(APIView):
    def get(self, *args, **kwargs):
        return Response('hello from get')