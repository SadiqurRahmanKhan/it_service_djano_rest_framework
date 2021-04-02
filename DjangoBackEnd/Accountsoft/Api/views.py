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
#  Create your views here.
#  Primary Group simple views for all method
'''
class PrimaryGroupViewSet(viewsets.ModelViewSet):
    queryset = PrimaryGroup.objects.all()
    serializer_class = PrimaryGroupSerializers

'''
#  primary group simple views for only get method


class PrimaryGroupViewSet(ReadOnlyModelViewSet):
    queryset = PrimaryGroup.objects.all()
    serializer_class = PrimaryGroupSerializers


#  ledger Group views

@api_view(['GET'])
def LedgerGroupListView(request):
    queryset = LedgerGroup.objects.all()
    serializer = LedgerGroupSerializers(queryset, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def LedgerGroupDetailView(request, pk):
    queryset = LedgerGroup.objects.get(id=pk)
    serializer = LedgerGroupSerializers(queryset, many=False)
    return Response(serializer.data)

#  Ledger group name search


@api_view(['GET'])
def LedgerGroupnameDetailView(request, pk):

    queryset = LedgerGroup.objects.filter(name=pk)
    serializer = LedgerGroupSerializers(queryset, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def LedgerGroupCreateView(request, *args, **kwargs):
    
    print(request.data)
    #queryset = LedgerGroup.objects.all()
    username = request.data.get('name', None)
    serializer = LedgerGroupSerializers(data=request.data)
    if username is not None:
        #queryset = queryset.filter(ledgergrouper__name=username)
        querysetCheck = LedgerGroup.objects.filter(name=username).count()

    if querysetCheck > 0 and serializer.is_valid():
        response_message = {"statuslg": 3, "data": serializer.data}
        return Response(response_message)
    else:

        try:
            if serializer.is_valid():
                serializer.save()
                response_message = {"statuslg": 1, "data": serializer.data}
            return Response(response_message)
        except:
            response_message = {"statuslg": 0, "data": serializer.data}
        return Response(response_message)


#  response message for ledger group put

@api_view(['PUT'])
def LedgerGroupUpdateView(request, pk):
    
    queryset = LedgerGroup.objects.get(id=pk)
    oldusername = queryset.name
    username = request.data.get('name', None)
    serializer = LedgerGroupSerializers(data=request.data)
    querysetCheck = 0
    if username != oldusername:
        querysetCheck = LedgerGroup.objects.filter(name=username).count()

    serializer = LedgerGroupSerializers(instance=queryset, data=request.data)

    if querysetCheck > 0 and serializer.is_valid():
        response_message = {"statusl": 3, "data": serializer.data}
        return Response(response_message)
    else:

        try:
            if serializer.is_valid():
                serializer.save()
                response_message = {"statusl": 1, "data": serializer.data}
        except:
            response_message = {"statusl": 0, "data": serializer.data}
        return Response(response_message)


@api_view(['Delete'])
def LedgerGroupDeleteView(request, pk):
    queryset = LedgerGroup.objects.get(id=pk)
    queryset.delete()

    return Response('Delete')


#  apiview ledger account

class ledgeraccountAPIView(generics.ListCreateAPIView):
    search_fields = ['name','email', 'mobile','ledgerGroupId__name']
    filter_backends = (filters.SearchFilter,)
    queryset = LedgerAccount.objects.all()
    serializer_class = LedgerAccountSerializers1


@api_view(['GET'])
def LedgerAccountListView(request):
    queryset = LedgerAccount.objects.all()
    serializer = LedgerAccountSerializers(queryset, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def LedgerAccountDetailView(request, pk):
    queryset = LedgerAccount.objects.get(id=pk)
    serializer = LedgerAccountSerializers(queryset, many=False)
    return Response(serializer.data)


#  Ledger account message show and its working
""" 
class LedgerAccountviewapi(views.APIView):

    def get(self, request, pk):
        try:
            query = LedgerAccount.objects.get(id=pk)
            serializer = LedgerAccountSerializers(query)
            response_message = {
                "ledgeraccountstatus": 1, "data": serializer.data}
        except:
            response_message = {"ledgerAccountstatus": 0,
                                "message": "your id is not found in the database"}
        return Response(response_message)
 """

#  Ledger account check from  ledgerAccount database

#  only id search
""" @api_view(['GET'])
def LedgerAccountidView(request, pk):
    queryset = LedgerAccount.objects.get(id=pk)
    serializer = LedgerAccountSerializers(queryset, many=True)
    return Response(serializer.data)
 """
#  agent id view


@api_view(['GET'])
def LedgerAccountLedgerGroupgetView(request, pk):

        querysetCheck = LedgerAccount.objects.filter(ledgerGroupId=pk).count()

        if querysetCheck > 0:
            response_message = {
                "statusgetaget": 1, "message": "your id is found in the database"}  
        else:
            response_message = {"statusgetaget": 0,
                                "message": "your id is not found in the database"}
          
        return Response(response_message)

#  ledger account name view


""" @api_view(['GET'])
def LedgerAccountnameView(request, pk):

    queryset = LedgerAccount.objects.filter(name=pk)
    serializer = LedgerAccountSerializers(queryset, many=True)
    return Response(serializer.data)
 """

#  Ledger account searching with id and name
'''
class LedgerAccountView(viewsets.ModelViewSet):
    queryset = LedgerAccount.objects.all()
    serializer_class = LedgerAccountSerializers
    filter_backends = (DjangoFilterBackend,SearchFilter)
    filter_field = ('id','name')
    
'''

""" 
@api_view(['POST'])
def LedgerAccountCreateView(request):
    serializer = LedgerAccountSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

"""

@api_view(['POST'])
def LedgerAccountCreateView(request, *args, **kwargs):
    data=request.data
    print(data)
    #queryset = LedgerAccount.objects.all()
    username = request.data.get('name', None)
    serializer = LedgerAccountSerializers(data=request.data)
    if username is not None:
        
        querysetCheck = LedgerAccount.objects.filter(name=username).count()

    if querysetCheck > 0 and serializer.is_valid():
        response_message = {"statuslac": 3, "data": serializer.data}
        return Response(response_message)
    else:

        try:
            if serializer.is_valid():
                serializer.save()
                response_message = {"statuslac": 1, "data": serializer.data}
            return Response(response_message)
        except:
            response_message = {"statuslac": 0, "data": serializer.data}
        return Response(response_message)

""" 
@api_view(['PUT'])
def LedgerAccountUpdateView(request, pk):
    queryset = LedgerAccount.objects.get(id=pk)
    serializer = LedgerAccountSerializers(instance=queryset, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data) """


@api_view(['PUT'])
def LedgerAccountUpdateView(request, pk):

    data=request.data

    queryset = LedgerAccount.objects.get(id=pk)
    oldusername = queryset.name
    user_name=request.data.get('name',None)

    dataimage=data.copy()
    if not dataimage['ledger_image']:
       dataimage.pop('ledger_image',None)

    serializer = LedgerAccountSerializers(data=request.data)
    querysetCheck = 0
    if user_name != oldusername:
        querysetCheck = LedgerAccount.objects.filter(name=username).count()
    serializer = LedgerAccountSerializers(instance=queryset, data=request.data)

    if querysetCheck > 0 and serializer.is_valid():
        response_message = {"statuslc": 2, "data": serializer.data}
        return Response(response_message)

    else:
        try:
            if serializer.is_valid():
                serializer.save()
                response_message = {"statuslc": 1, "data": serializer.data}

        except:
            response_message = {"statuslc": 0, "data": serializer.data}
        return Response(response_message)



""" @api_view(['Delete'])
def LedgerAccountDeleteView(request, pk):
    queryset = LedgerAccount.objects.get(id=pk)
    queryset.delete()

    return Response('Delete') """

@api_view(['Delete'])
def LedgerAccountDeleteView(request, pk):
    queryset = LedgerAccount.objects.get(id=pk)
    try:
        image_path=os.path.join(settings.MEDIA_ROOT,str(queryset.ledger_image))
        os.unlink(image_path)
    except:
        pass
    queryset.delete()

    ledacData = LedgerAccount.objects.all()
    ledSerializer = LedgerAccountSerializers(ledacData,many="true")
    data={'statusdl':1,'message':'Employee deleted successfully.',"data":ledSerializer.data}
    return JsonResponse(data,safe=False)



'''class LedgerAccountCreateView(CreateAPIView):
    serializer_class = LedgerAccountSerializers
    queryset = LedgerAccount.objects.all()

    def post(self, request):
        print(request.data)
        serializer = LedgerAccountSerializers(data=request.data)
        serializer.is_valid()
        LedgerAccount = serializer.create(request)
        if LedgerAccount:
            return Response(status=HTTP_201_CREATED)
        return Response(status=HTTP_400_BAD_REQUEST)
        '''


class LedgerAccountViewSet(viewsets.ModelViewSet):
    serializer_class = LedgerAccountSerializers
    queryset = LedgerAccount.objects.all()

    '''def create(self, request):
        serializer =LedgerAccountSerializers(data=request.data)
        if serializer.is_valid():
            assignment = serializer.create(request)
            if assignment:
                return Response(status=HTTP_201_CREATED)
        return Response(status=HTTP_400_BAD_REQUEST)
    '''


class CountryViewSet(viewsets.ModelViewSet):
    serializer_class = CountrySerializers
    queryset = Countrydb.objects.all()


class DistrcitViewSet(viewsets.ModelViewSet):
    serializers = DistrictSerializers
    queryset = District.objects.all()


class PoliceStationViewSet(viewsets.ModelViewSet):
    serializers = PoliceStationSerializers
    query = PoliceStation.objects.all()


class LedgerGroupViewSet(ReadOnlyModelViewSet):
    serializer_class = LedgerGroupSerializer
    queryset = LedgerGroup.objects.all()


class LedgerGroupViewSet(viewsets.ModelViewSet):
    def list(self, request):
        query = LedgerGroup.objects.filter(primaryID=PrimaryGroup.id)
        serializers = LedgerGroupSerializers(query, many=True)
        all_data = []

        for ledgerGroup in serializers.data:
            primaryGroup = primaryGroup.objects.all
            primaryGroup_serializer = PrimaryGroupSerializers(
                primaryGroup, many=True)
            ledgerGroup = primaryGroup_serializer.data
            all_data.append(ledgerGroup)
        return Response(all_data)


 
@api_view(['GET'])
def JoinPGLederapiListView(request):
    queryset = JoinPrimaryGroupLedgerModel.objects.raw(
        'select lg.id as id, lg.name as lgname,lg1.name as upgname, pg."GName" as pgname from public."Api_ledgergroup" as lg left outer join  public."Api_primarygroup" as pg on lg."primaryID"=pg.id  left outer join  public."Api_ledgergroup" as lg1 on lg1.id=lg."upperGID"')
    serializer = JoinPGSerializers(queryset, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def JoinPGLederapiDetailView(request,pk):
    queryset=JoinPrimaryGroupLedgerModel.objects.raw('select lg.id as id, lg.name as lgname, pg."GName" as pgname from public."Api_ledgergroup" as lg left outer join  public."Api_primarygroup" as pg on lg."primaryID"=pg.id')
    serializer=JoinPGSerializers(queryset, many=False)
    return Response(serializer.data)
     
    

#  Designation


@api_view(['GET'])
def DesignationListView(request):
    queryset = Designationdb.objects.all()
    serializer = DesignationSerializers(queryset, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def DesignationDetailView(request, pk):
    queryset = Designationdb.objects.get(id=pk)
    serializer = DesignationSerializers(queryset, many=False)
    return Response(serializer.data)

'''
@api_view(['POST'])
def DesignationCreateView(request, *args, **kwargs):
    serializer = DesignationSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
'''

@api_view(['POST'])
def DesignationCreateView(request, *args, **kwargs):

   
    username = request.data.get('designation_name', None)
    serializer = DesignationSerializers(data=request.data)
    if username is not None:
        
        querysetCheck = Designationdb.objects.filter(designation_name=username).count()

    if querysetCheck > 0 and serializer.is_valid():
        response_message = {"statusdes": 3, "data": serializer.data}
        return Response(response_message)
    else:

        try:
            if serializer.is_valid():
                serializer.save()
                response_message = {"statusdes": 1, "data": serializer.data}
            return Response(response_message)
        except:
            response_message = {"statusdes": 0, "data": serializer.data}
        return Response(response_message)



'''
@api_view(['PUT'])
def DesignationUpdateView(request, pk):
    queryset = Designation.objects.get(id=pk)
    serializer = DesignationSerializers(instance=queryset, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)
'''


@api_view(['PUT'])
def DesignationUpdateView(request, pk):

    queryset = Designationdb.objects.get(id=pk)
    oldusername = queryset.designation_name
    username = request.data.get('designation_name', None)
    serializer = DesignationSerializers(data=request.data)
    querysetCheck = 0
    if username != oldusername:
        querysetCheck = Designationdb.objects.filter(designation_name=username).count()

    serializer = DesignationSerializers(instance=queryset, data=request.data)

    if querysetCheck > 0 and serializer.is_valid():
        response_message = {"statusdess": 3, "data": serializer.data}
        return Response(response_message)
    else:

        try:
            if serializer.is_valid():
                serializer.save()
                response_message = {"statusdess": 1, "data": serializer.data}
        except:
            response_message = {"statusdess": 0, "data": serializer.data}
        return Response(response_message)




@api_view(['Delete'])
def DesignationDeleteView(request, pk):
    queryset = Designationdb.objects.get(id=pk)
    queryset.delete()

    return Response('Delete')
# filtering 

class desAPIView(generics.ListCreateAPIView):
    search_fields = ['designation_name']
    filter_backends = (filters.SearchFilter,)
    queryset = Designationdb.objects.all()
    serializer_class = DesignationSerializers

# check for delete

@api_view(['GET'])
def designationget(request, pk):
    querysetCheck = Employee.objects.filter(employee_degignation_id=pk).count()
    if querysetCheck > 0:
        response_message = {
            "statusdesi": 1, "message": "your id is in user you can not delete"}  
    else:
        response_message = {"statusdesi": 0,
                            "message": "your id is not in user database ,you can delete"}
          
    return Response(response_message)


# @ Branch

@api_view(['GET'])
def BranchListView(request):
    queryset = Branchdb.objects.all()
    serializer = BranchSerializers(queryset, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def BranchDetailView(request, pk):
    queryset = Branchdb.objects.get(id=pk)
    serializer = BranchSerializers(queryset, many=False)
    return Response(serializer.data)



@api_view(['POST'])
def BranchCreateView(request, *args, **kwargs):

   
    username = request.data.get('branch_name', None)

    print(request.data)

    serializer = BranchSerializers(data=request.data)
    if username is not None:
        
        querysetCheck = Branchdb.objects.filter(branch_name=username).count()

    if querysetCheck > 0 and serializer.is_valid():
        response_message = {"statusbr": 3, "data": serializer.data}
        return Response(response_message)
    else:

        try:
            if serializer.is_valid():
                serializer.save()
                response_message = {"statusbr": 1, "data": serializer.data}
            return Response(response_message)
        except:
            response_message = {"statusbr": 0, "data": serializer.data}
        return Response(response_message)


"""
@api_view(['POST'])
def BranchCreateView(request, *args, **kwargs):
    serializer = BranchSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
"""


@api_view(['PUT'])
def BranchUpdateView(request, pk):

    queryset = Branchdb.objects.get(id=pk)
    oldusername = queryset.branch_name
    username = request.data.get('branch_name', None)
    serializer = BranchSerializers(data=request.data)
    querysetCheck = 0
    if username != oldusername:
        querysetCheck = Branchdb.objects.filter(branch_name=username).count()

    serializer = BranchSerializers(instance=queryset, data=request.data)

    if querysetCheck > 0 and serializer.is_valid():
        response_message = {"statusb": 3, "data": serializer.data}
        return Response(response_message)
    else:

        try:
            if serializer.is_valid():
                serializer.save()
                response_message = {"statusb": 1, "data": serializer.data}
        except:
            response_message = {"statusb": 0, "data": serializer.data}
        return Response(response_message)


"""

@api_view(['PUT'])
def BranchUpdateView(request, pk):
    queryset = Branchdb.objects.get(id=pk)
    serializer = BranchSerializers(instance=queryset, data=request.data)

    if serializer.is_valid():
        serializer.save()

        return Response(serializer.data)
        
"""

@api_view(['Delete'])
def BranchDeleteView(request, pk):
    queryset = Branchdb.objects.get(id=pk)
    queryset.delete()

    return Response('Delete')


# check for delete
@api_view(['GET'])
def branchget(request, pk):
    querysetCheck = Employee.objects.filter(employee_branch_id=pk).count()
    if querysetCheck > 0:
        response_message = {
            "statusdesi": 1, "message": "your id is in user you can not delete"}  
    else:
        response_message = {"statusbrn": 0,
                            "message": "your id is not in user database ,you can delete"}
          
    return Response(response_message)


#  filtering


class branchAPIView(generics.ListCreateAPIView):
    search_fields = ['branch_name']
    filter_backends = (filters.SearchFilter,)
    queryset = Branchdb.objects.all()
    serializer_class = BranchSerializers



# District

@api_view(['GET'])
def DistrictListView(request):
    queryset = District.objects.all()
    serializer = DistrictSerializers(queryset, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def DistrictDetailView(request, pk):
    queryset = District.objects.get(id=pk)
    serializer = DistrictSerializers(queryset, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def DistrictCreateView(request, *args, **kwargs):

    serializer = DistrictSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)


@api_view(['PUT'])
def DistrictUpdateView(request, pk):
    queryset = District.objects.get(id=pk)
    serializer = DistrictSerializers(instance=queryset, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['Delete'])
def DistrictDeleteView(request, pk):
    queryset = District.objects.get(id=pk)
    queryset.delete()

    return Response('Delete')



# police station

@api_view(['GET'])
def policestationListView(request):
    queryset = PoliceStation.objects.all()
    serializer = PoliceStationSerializers(queryset, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def policestationDetailView(request, pk):
    queryset = PoliceStation.objects.get(id=pk)
    serializer = PoliceStationSerializers(queryset, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def policestationCreateView(request, *args, **kwargs):

    serializer = PoliceStationSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)


@api_view(['PUT'])
def policestationtUpdateView(request, pk):
    queryset = PoliceStation.objects.get(id=pk)
    serializer = PoliceStationSerializers(instance=queryset, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['Delete'])
def policestationDeleteView(request, pk):
    queryset = PoliceStation.objects.get(id=pk)
    queryset.delete()

    return Response('Delete')


# Country 

@api_view(['GET'])
def countryListView(request):
    queryset = Countrydb.objects.all()
    serializer = CountrySerializers(queryset, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def countryDetailView(request, pk):
    queryset = Countrydb.objects.get(id=pk)
    serializer = CountrySerializers(queryset, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def countryCreateView(request, *args, **kwargs):

    serializer = CountrySerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)


@api_view(['PUT'])
def countryUpdateView(request, pk):
    queryset = Countrydb.objects.get(id=pk)
    serializer = CountrySerializers(instance=queryset, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['Delete'])
def countryDeleteView(request, pk):
    queryset = Countrydb.objects.get(id=pk)
    queryset.delete()

    return Response('Delete')
