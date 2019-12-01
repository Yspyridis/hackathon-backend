from django.shortcuts import render
from rest_framework import generics
from django.http import HttpResponse
from django.http import JsonResponse

from rest_framework import generics
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import status
from rest_framework_jwt.settings import api_settings

from .models import Coordinate, farms
from .serializers import CoordinateSerializer, FarmsSerializer

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

    queryset = farms.objects.all()
    serializer_class = FarmsSerializer

    def post(self, request, *args, **kwargs):
        import json

		# check if the farm is near a natura 2000 area
		# if the distance is less than 5, then the farm is unsastainable

        natura_points = []
        polygons = Coordinate.objects.all()
        for polygon in polygons:
            natura_points.append(Point(polygon.x, polygon.y))

        distances = []
        results = {}
        for farm in request.data:

            farm_cords = farm['coords']
            farm_name = str(farm['name'])
            farm_type = str(farm['type'])

            points = []
            for point in farm_cords:
                points.append((point['lat'], point['lng']))
            print(points)

            P = Polygon( points )
            point = P.centroid

            for natura_point in natura_points:
                distances.append(point.distance(natura_point))
            results['name'] = farm_name
            results['farm_center'] = str(point)

            if min(distances) >= 30: #  this is hardcoded
                results['sustainable'] = "SUSTAINABLE"
                sustainable = True
            else:
                results['sustainable'] = "UN-SUSTAINABLE"
                sustainable = False

        newFarm = farms(farm_name = farm_name, corp_type = farm_type, cords = str(points), farm_center = (str(point)), sustainable = sustainable)
        newFarm.save()

        queryset = farms.objects.all().values()
        return JsonResponse({'results': list(queryset)})
