from django.urls import path
from .views import PCCreateListView, PCRetrieveDeleteView

urlpatterns = [
    path('', PCCreateListView.as_view(), name='pc_list_create'),
    path('/<int:pk>', PCRetrieveDeleteView.as_view(), name='pc_retrive_delete')
]
