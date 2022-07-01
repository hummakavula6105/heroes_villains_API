from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import SuperTypeSerializer
from .models import SuperType
from rest_framework import status

import super_types



@api_view(['GET'])
def super_types_list(request):
    
    if request.method == 'GET':
        super_type = request.query_params.get('super_type')
        print(super_type)
        
        queryset = SuperType.objects.all()

        if super_type:
            queryset = queryset.filter(super__type=super_type)
            
        serializer = SuperTypeSerializer(super_types, many=True)
        return Response (serializer.data)

    elif request.method == 'POST':
        serializer = SuperTypeSerializer(data=request.data)
        print(serializer)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def super_types_detail(request, pk):
    super_type = get_object_or_404(SuperType, pk=pk)
    if request.method == 'GET':
        serializer = SuperTypeSerializer(super_type);
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = SuperTypeSerializer(super_type, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        super_type.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)