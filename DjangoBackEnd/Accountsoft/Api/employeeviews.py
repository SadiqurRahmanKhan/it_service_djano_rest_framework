from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework import views, viewsets, generics, mixins
from rest_framework.viewsets import ReadOnlyModelViewSet
from .models import *
#from .vmmodels import *
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


# @ Employee
#  filtering 

class EmployeeAPIView(generics.ListCreateAPIView):
    search_fields = ['employee_nic_name','employee_name', 'employee_branch_id__branch_name','employee_District_id__DName','employee_degignation_id__designation_name']
    filter_backends = (filters.SearchFilter,)
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializers1


@api_view(['GET'])
def EmployeeListView(request):
    queryset = Employee.objects.all()
    serializer = EmployeeSerializers(queryset, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def EmployeeDetailView(request, pk):
    queryset = Employee.objects.get(id=pk)
    serializer = EmployeeSerializers(queryset, many=False)
    return Response(serializer.data)

""" @api_view(['POST'])
def EmployeeCreateView(request, *args, **kwargs):
    serializer = EmployeeSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
 """
""" 
@api_view(['POST'])
def EmployeeCreateView(request):
    employeeN = request.data.get('employee_name',None)

    print(request.data)
    serializer = EmployeeSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
 """

@api_view(['POST'])
def EmployeeCreateView(request, *args, **kwargs):
    data=request.data
    print(data)
    #queryset = LedgerGroup.objects.all()
    username = request.data.get('employee_name', None)
    serializer = EmployeeSerializers(data=request.data)
    if username is not None:
        
        querysetCheck = Employee.objects.filter(employee_name=username).count()

    if querysetCheck > 0 and serializer.is_valid():
        response_message = {"statusem": 3, "data": serializer.data}
        return Response(response_message)
    else:

        try:
            if serializer.is_valid():
                serializer.save()
                response_message = {"statusem": 1, "data": serializer.data}
            return Response(response_message)
        except:
            response_message = {"statusem": 0, "data": serializer.data}
        return Response(response_message)


 

@api_view(['PUT'])
def EmployeeUpdateView(request, pk):

    data=request.data

    queryset = Employee.objects.get(id=pk)
    oldusername = queryset.employee_name
    user_name=request.data.get('employee_name',None)

    dataimage=data.copy()
    if not dataimage['employee_image']:
       dataimage.pop('employee_image',None)

    serializer = EmployeeSerializers(data=request.data)
    querysetCheck = 0
    if user_name != oldusername:
        querysetCheck = Employee.objects.filter(employee_name=user_name).count()
    serializer = EmployeeSerializers(instance=queryset, data=request.data)

    if querysetCheck > 0 and serializer.is_valid():
        response_message = {"statusemp": 2, "data": serializer.data}
        return Response(response_message)

    else:
        try:
            if serializer.is_valid():
                serializer.save()
                response_message = {"statusemp": 1, "data": serializer.data}

        except:
            response_message = {"statusemp": 0, "data": serializer.data}
        return Response(response_message)


   # return Response(serializer.data)

""" 
@api_view(['PUT'])
def EmployeeUpdateView(request, pk):
    queryset = Employee.objects.get(id=pk)
    serializer = EmployeeSerializers(instance=queryset, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)
 """


@api_view(['Delete'])
def EmployeeDeleteView(request, pk):
    queryset = Employee.objects.get(id=pk)
    try:
        image_path=os.path.join(settings.MEDIA_ROOT,str(queryset.employee_image))
        os.unlink(image_path)
    except:
        pass
    queryset.delete()

    EmployeeData = Employee.objects.all()
    EmpSerializer = EmployeeSerializers(EmployeeData,many="true")
    data={'status':1,'message':'Employee deleted successfully.',"data":EmpSerializer.data}
    return JsonResponse(data,safe=False)
    #return Response('Delete')
 

""" @api_view(['Delete'])
def EmployeeDeleteView(request, pk):
    queryset = Employee.objects.get(id=pk)
    queryset.delete()

    return Response('Delete')

 """


# finding using emp id 

""" 
@api_view(['GET'])
def employeeget(request, pk):
    queryset = user.objects.filter(employeeid=pk)
    serializer = userSerializers(queryset, many=True)
    return Response(serializer.data)

 """

@api_view(['GET'])
def employeeget(request, pk):
    querysetCheck = AssociatUser.objects.filter(employeeid=pk).count()
    if querysetCheck > 0:
        response_message = {
            "statusgetuser": 1, "message": "your id is in user you can not delete"}  
    else:
        response_message = {"statusgetuser": 0,
                            "message": "your id is not in user database ,you can delete"}
          
    return Response(response_message)




# Employee , degignation and branch join view
""" 
@api_view(['GET'])
def empdesignatinbranchDetailView(request):
    queryset = EmpDesBranch.objects.raw(
        'select em.id as id, em.employee_name as EmployeName,em.employee_email as Email,em.employee_mobile as Mobile,dg."designation_name" as Designation,br."branch_name" as Branch from public."Api_employee" as em left outer join  public."Api_designation" as dg on em."id"=dg.id  left outer join  public."Api_branch" as br on br.id=em."id"')
    serializer = JoinEmpDesigBranchSerializers(queryset, many=True)
    return Response(serializer.data)

 """