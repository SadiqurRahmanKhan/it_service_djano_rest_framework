from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework import views, viewsets, generics, mixins
from rest_framework.viewsets import ReadOnlyModelViewSet
from .models import *
#from .vmodels import *
from .serializers import *
from rest_flex_fields.views import FlexFieldsMixin
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.filters import SearchFilter
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.renderers import JSONRenderer
from rest_framework import status
from rest_framework.status import (
    HTTP_201_CREATED,
    HTTP_400_BAD_REQUEST
)


class subledgerAPIView(generics.ListCreateAPIView):
    search_fields = ['name']
    filter_backends = (filters.SearchFilter,)
    queryset = subledger.objects.all()
    serializer_class = subledgerSerializers1
 

@api_view(['GET'])
def subledgerListView(request):
    queryset = subledger.objects.all()
    serializer = subledgerSerializers(queryset, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def subledgerDetailView(request, pk):
    queryset = subledger.objects.get(id=pk)
    serializer = subledgerSerializers(queryset, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def subledgerCreateView(request, *args, **kwargs):
    data=request.data
    print(data)
    #queryset = LedgerGroup.objects.all()
    username = request.data.get('name', None)
    serializer = subledgerSerializers(data=request.data)
    if username is not None:
        
        querysetCheck = subledger.objects.filter(name=username).count()

    if querysetCheck > 0 and serializer.is_valid():
        response_message = {"statussub": 3, "data": serializer.data}
        return Response(response_message)
    else:

        try:
            if serializer.is_valid():
                serializer.save()
                response_message = {"statussub": 1, "data": serializer.data}
            return Response(response_message)
        except:
            response_message = {"statussub": 0, "data": serializer.data}
        return Response(response_message)


 

@api_view(['PUT'])
def subledgerUpdateView(request, pk):

    data=request.data

    queryset = subledger.objects.get(id=pk)
    oldusername = queryset.name
    user_name=request.data.get('name',None)

    serializer = subledgerSerializers(data=request.data)
    querysetCheck = 0
    if user_name != oldusername:
        querysetCheck = subledger.objects.filter(name=user_name).count()
    serializer = subledgerSerializers(instance=queryset, data=request.data)

    if querysetCheck > 0 and serializer.is_valid():
        response_message = {"statussb": 2, "data": serializer.data}
        return Response(response_message)

    else:
        try:
            if serializer.is_valid():
                serializer.save()
                response_message = {"statussb": 1, "data": serializer.data}

        except:
            response_message = {"statussb": 0, "data": serializer.data}
        return Response(response_message)


   # return Response(serializer.data)


@api_view(['Delete'])
def subledgerDeleteView(request, pk):
    queryset =subledger.objects.get(id=pk)
    queryset.delete()

    userData = subledger.objects.all()
    resSerializer = subledgerSerializers(userData,many="true")
    data={'statussbr':1,'message':'User deleted successfully.',"data":resSerializer.data}
    return JsonResponse(data,safe=False)





# finding using emp id 

""" 
@api_view(['GET'])
def subledgerget(request, pk):
    querysetCheck = subledger.objects.filter(employeeid=pk).count()
    if querysetCheck > 0:
        response_message = {
            "statusgetuser": 1, "message": "your id is in user you can not delete"}  
    else:
        response_message = {"statusgetuser": 0,
                            "message": "your id is not in user database ,you can delete"}
          
    return Response(response_message)
 """