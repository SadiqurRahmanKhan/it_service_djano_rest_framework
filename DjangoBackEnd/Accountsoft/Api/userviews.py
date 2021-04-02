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
# from rest_framework.views import APIView
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

# userType

@api_view(['GET'])
def userTypeListView(request):
    queryset = userType.objects.all()
    serializer = userTypeSerializers(queryset, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def userTypeDetailView(request, pk):
    queryset = userType.objects.get(id=pk)
    serializer = userTypeSerializers(queryset, many=False)
    return Response(serializer.data)



@api_view(['POST'])
def userTypeCreateView(request, *args, **kwargs):

   
    username = request.data.get('userType_name', None)
    print(request.data)

    serializer = userTypeSerializers(data=request.data)
    if username is not None:
        
        querysetCheck = userType.objects.filter(userType_name=username).count()

    if querysetCheck > 0 and serializer.is_valid():
        response_message = {"statusst": 3, "data": serializer.data}
        return Response(response_message)
    else:

        try:
            if serializer.is_valid():
                serializer.save()
                response_message = {"statusst": 1, "data": serializer.data}
            return Response(response_message)
        except:
            response_message = {"statusst": 0, "data": serializer.data}
        return Response(response_message)




@api_view(['PUT'])
def userTypeUpdateView(request, pk):

    queryset = userType.objects.get(id=pk)
    oldusername = queryset.userType_name
    username = request.data.get('userType_name', None)
    serializer = userTypeSerializers(data=request.data)
    querysetCheck = 0
    if username != oldusername:
        querysetCheck = userType.objects.filter(userType_name=username).count()

    serializer = userTypeSerializers(instance=queryset, data=request.data)

    if querysetCheck > 0 and serializer.is_valid():
        response_message = {"statusstt": 3, "data": serializer.data}
        return Response(response_message)
    else:

        try:
            if serializer.is_valid():
                serializer.save()
                response_message = {"statusstt": 1, "data": serializer.data}
        except:
            response_message = {"statusstt": 0, "data": serializer.data}
        return Response(response_message)


@api_view(['Delete'])
def userTypeDeleteView(request, pk):
    queryset = userType.objects.get(id=pk)
    queryset.delete()

    return Response('Delete')


class usertypeAPIView(generics.ListCreateAPIView):
    search_fields = ['userType_name']
    filter_backends = (filters.SearchFilter,)
    queryset = userType.objects.all()
    serializer_class = userTypeSerializers
   

@api_view(['GET'])
def usertypeget(request, pk):
    querysetCheck = AssociatUser.objects.filter(usertype=pk).count()
    if querysetCheck > 0:
        response_message = {
            "statusgetusertyp": 1, "message": "your id is in user you can not delete"}  
    else:
        response_message = {"statusgetuser": 0,
                            "message": "your id is not in user database ,you can delete"}
          
    return Response(response_message)




# user 


@api_view(['GET'])
def userListView(request):
    queryset = AssociatUser.objects.all()
    serializer = userSerializers(queryset, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def userDetailView(request, pk):
    queryset = AssociatUser.objects.get(id=pk)
    serializer = userSerializers(queryset, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def userCreateView(request, *args, **kwargs):
    print(request.data) 
   # print(request.data)
    username = request.data.get('user_name', None)
    serializer = userSerializers(data=request.data)
    if username is not None:
       
        querysetCheck = AssociatUser.objects.filter(user_name=username).count()

    if querysetCheck > 0 and serializer.is_valid():
        response_message = {"statususr": 3, "data": serializer.data}
        return Response(response_message)
    else:

        try:
            if serializer.is_valid():
                serializer.save()
                response_message = {"statususr": 1, "data": serializer.data}
            return Response(response_message)
        except:
            response_message = {"statususr": 0, "data": serializer.data}
        return Response(response_message)


@api_view(['PUT'])
def userUpdateView(request, pk):

    queryset = AssociatUser.objects.get(id=pk)
    oldusername = queryset.user_name
    username = request.data.get('user_name', None)
    serializer = userSerializers(data=request.data)
    querysetCheck = 0
    if username != oldusername:
        querysetCheck = AssociatUser.objects.filter(user_name=username).count()

    serializer = userSerializers(instance=queryset, data=request.data)

    if querysetCheck > 0 and serializer.is_valid():
        response_message = {"statususrr": 3, "data": serializer.data}
        return Response(response_message)
    else:

        try:
            if serializer.is_valid():
                serializer.save()
                response_message = {"statususrr": 1, "data": serializer.data}
        except:
            response_message = {"statususrr": 0, "data": serializer.data}
        return Response(response_message)


@api_view(['Delete'])
def userDeleteView(request, pk):
    queryset =AssociatUser.objects.get(id=pk)
    queryset.delete()

    userData = AssociatUser.objects.all()
    usrSerializer = userSerializers(userData,many="true")
    data={'status':1,'message':'User deleted successfully.',"data":usrSerializer.data}
    return JsonResponse(data,safe=False)


# filtering users


class userAPIView(generics.ListCreateAPIView):
    search_fields = ['=user_name','=password', 'usertype__userType_name']
    filter_backends = (filters.SearchFilter,)
    #print(request.data)
    queryset = AssociatUser.objects.all()
    serializer_class = userSerializers1
    


