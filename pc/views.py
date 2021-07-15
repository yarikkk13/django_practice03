from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import PCModel
from .serializers import PCSerializer


# Create your views here.
class PCCreateListView(APIView):
    def get(self, *args, **kwargs):
        qs = PCModel.objects.all()
        serializer = PCSerializer(qs, many=True)
        return Response(serializer.data, status.HTTP_200_OK)

    def post(self, *args, **kwargs):
        body = self.request.data
        serializer = PCSerializer(data=body)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)


class PCRetrieveDeleteView(APIView):
    def get(self, *args, **kwargs):
        pk = kwargs.get('pk')
        data = get_object_or_404(PCModel, pk=pk)
        serializer = PCSerializer(data)
        return Response(serializer.data, status.HTTP_200_OK)

    def put(self, *args, **kwargs):
        pk = kwargs.get('pk')
        body = self.request.data
        try:
            data = PCModel.objects.get(pk=pk)
        except Exception:
            return Response('not found', status.HTTP_404_NOT_FOUND)
        serializer = PCSerializer(data, data=body)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_202_ACCEPTED)

    def patch(self, *args, **kwargs):
        pk = kwargs.get('pk')
        body = self.request.data
        try:
            data = PCModel.objects.get(pk=pk)
        except Exception:
            return Response('not found', status.HTTP_404_NOT_FOUND)
        serializer = PCSerializer(data, data=body, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_202_ACCEPTED)

    def delete(self, *args, **kwargs):
        pk = kwargs.get('pk')
        try:
            data = PCModel.objects.get(pk=pk)
        except Exception as e:
            return Response(e, status.HTTP_404_NOT_FOUND)
        data.delete()
        return Response('delete', status.HTTP_204_NO_CONTENT)
