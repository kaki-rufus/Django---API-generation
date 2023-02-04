from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import *

# Create your views here.
@api_view(['GET', 'POST'])
def Home(request):
    if request.method == 'GET':
        emp = Employee.objects.all()
        serializer = employeeSerializer(emp, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serialized = employeeSerializer(data=request.data)
        if serialized.is_valid():
            serialized.save()
        return Response(serialized.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def Update(request, id):
    try:
        dta = Employee.objects.get(pk=id)
    except Employee.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = employeeSerializer(dta)
        return Response(serializer.data)
    if request.method == 'PUT':
        serialized = employeeSerializer(dta, data=request.data)
        if serialized.is_valid():
            serialized.save()
            return Response(serialized.data)
        return Response(serialized.data, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        dta.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


