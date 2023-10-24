from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import HostelPost,Dante
from rest_framework import status
from .serializers import HotelSerializer, DanteSerializer
@api_view(['GET','POST'])
def home(request):
    hostels = HostelPost.objects.all()
    if request.method == 'POST':
        converted = HotelSerializer(data = request.data)
        if converted.is_valid():
            converted.save()
            return Response(status=status.HTTP_201_CREATED)
    converted = HotelSerializer(hostels, many = True)
    return Response(converted.data)
@api_view(['GET','POST','DELETE'])
def about(request):
    students=Dante.objects.all()
    convert=DanteSerializer(students, many=True)
    return Response(convert.data)
# Create your views here.
@api_view(['DELETE'])
def deleteHostel(request, pk):
    hostel = HostelPost.objects.get(id=pk)
    if request.method == 'DELETE':
        hostel.delete()
        return Response(status=status.HTTP_200_OK)
