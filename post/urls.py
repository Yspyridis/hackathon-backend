from django.urls import path

from .views import FarmsApiView
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    #REST API
    path('farms-api/', FarmsApiView.as_view(), name="farms-api-create"),
]
