from django.urls import path
from .views import PCCreateListView

urlpatterns = [
    path('', PCCreateListView.as_view(), name='pc_list_create')
]
