from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from core.models import PCModel
from .serializers import PCSerializer


# Create your views here.
class PCCreateListView(ListCreateAPIView):
    serializer_class = PCSerializer
    queryset = PCModel.objects.all()


class PCRetrieveDeleteView(RetrieveUpdateDestroyAPIView):
    serializer_class = PCSerializer
    queryset = PCModel.objects.all()
