from django.shortcuts import render
from rest_framework import generics
from django.http import HttpResponse

from rest_framework import generics
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import status
from rest_framework_jwt.settings import api_settings

from .models import Coordinate
from .serializers import CoordinateSerializer

from shapely.geometry import Polygon, Point, LinearRing
from shapely.geometry import Polygon

def index(request):
    return HttpResponse("POST.")


#REST API
class FarmsApiView(generics.ListCreateAPIView):

    #na apothikeuontai mono ta kainouria, ta ypoloipa na ginontai update
    """
    GET devices/
    POST devices/
    """

    queryset = Coordinate.objects.all()
    serializer_class = CoordinateSerializer

    def post(self, request, *args, **kwargs):
        import json

        polygons = [Polygon([(30, 0), (2,8), (14, 10), (6, 1)]), Polygon([(0, 0), (5,6), (8, 12), (3, 4)]), Polygon([(0, 0), (5,8), (1, 10), (2, 100)])]

        distances = []

        print(distances)

        #parse the list, validate each entry and save to database
        for farm in request.data:
            print(farm['lon'])
            P = Polygon([[0, 0], [1, 0], [1, 1], [0, 1]])
            point = P.centroid

            print(point)

        return Response("farms were created")
