from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework import views, viewsets, generics, mixins
from rest_framework.viewsets import ReadOnlyModelViewSet
from .models import *
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
import datetime
from rest_framework.status import (
    HTTP_201_CREATED,
    HTTP_400_BAD_REQUEST
)
 

class receptAPIView(generics.ListCreateAPIView):
    search_fields = ['=invoice_number']
    filter_backends = (filters.SearchFilter,)
    queryset = recept.objects.all()
    serializer_class = receptSerializers1
 

@api_view(['GET'])
def receptListView(request):
    queryset = recept.objects.all()
    serializer = receptSerializers(queryset, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def receptDetailView(request, pk):
    queryset = recept.objects.get(id=pk)
    serializer = receptSerializers(queryset, many=False)
    return Response(serializer.data)
# 
import json
import requests

@api_view(['POST'])
def receptCreateView(request, *args, **kwargs):
   # data=request.data
    """
    print(data["recept_ammount_DR"]) 
    users = json.dumps(data)
    d2 = json.loads(users)
    print(d2)
    """
    print(request.data)
    
    rpt_date= request.data.get('recept_date', None)
    subid= request.data.get('subledgerid', None)
    credby= request.data.get('createdby', None)
    cedDate= request.data.get('createdDate', None)
    updedby= request.data.get('updatedby', None)
    uatDate= request.data.get('updatedDate', None)
    Brh_id= request.data.get('Branch_id', None)
    nation= request.data.get('narration', None)


    today = datetime.date.today()
    today_string = today.strftime('%y%m%d')
    print(today_string)
    next_invoice_number = '01'
    invoice_number='0'
    last_invoice = recept.objects.filter(invoice_number__startswith=today_string).order_by('invoice_number').last()

    print('lastinv'+str(last_invoice))

    if last_invoice:
            
        last_invoice_number = int(last_invoice.invoice_number[6:])
        print(last_invoice_number)
        next_invoice_number = '{0:02d}'.format(last_invoice_number + 1)
        print(next_invoice_number)
        invoice_number = today_string + next_invoice_number
    else:
        invoice_number = today_string + next_invoice_number


    rpt_ammount_DRarry= request.data.get('recept_ammount_DR', None)

    rcptr = len(rpt_ammount_DRarry)
    print(rcptr)

    for x in range(rcptr):

        rpt_ammount_DR= rpt_ammount_DRarry[x]['recept_ammount_DR']

        print(rpt_ammount_DR)

        rpt_ammount_CR= rpt_ammount_DRarry[x]['recept_ammount_CR']
        print(rpt_ammount_CR)
        lgacoount= rpt_ammount_DRarry[x]['atvalue']

        print(lgacoount)
        
        formatrData={
            "ledgeracoount":lgacoount,
            "recept_date":rpt_date,
            "subledgerid":subid,
            "recept_ammount_DR":rpt_ammount_DR,
            "recept_ammount_CR":rpt_ammount_CR,
            "createdby":credby,
            "createdDate":cedDate,
            "updatedby":updedby,
            "updatedDate":uatDate,
            "Branch_id":Brh_id,
            "invoice_number":invoice_number,
            "narration":nation
            }
        print(invoice_number)
        print(formatrData)
    #  print(request.data)
        #request.data=formatrData
        #finalData = json.dumps(formatrData)
        #print(finalData)
        #queryset = LedgerGroup.objects.all()
        #username = request.data.get('narration', None)
        #print(request.data)

        serializer = receptSerializers(data=formatrData)

        
        if serializer.is_valid():
            print('save hit')
            serializer.save()
            print('save hit2')
            response_message = {"statusrecpt": 1, "data": serializer.data}
                
    return Response(response_message)
""" except:
            print('error hit')
            response_message = {"statusrecpt": 0, "data": serializer.data}
        return Response(response_message) """


"""

@api_view(['POST'])
def receptCreateView(request, *args, **kwargs):
   # data=request.data
    """
"""print(data["recept_ammount_DR"]) 
    users = json.dumps(data)
    d2 = json.loads(users)
    print(d2)"""
"""
    print(request.data)
    
    rpt_date= request.data.get('recept_date', None)
    subid= request.data.get('subledgerid', None)
    credby= request.data.get('createdby', None)
    cedDate= request.data.get('createdDate', None)
    updedby= request.data.get('updatedby', None)
    uatDate= request.data.get('updatedDate', None)
    Brh_id= request.data.get('Branch_id', None)
    nation= request.data.get('narration', None)


    today = datetime.date.today()
    today_string = today.strftime('%y%m%d')
    print(today_string)
    next_invoice_number = '01'
    invoice_number='0'
    last_invoice = recept.objects.filter(invoice_number__startswith=today_string).order_by('invoice_number').last()

    print('lastinv'+str(last_invoice))

    if last_invoice:
            
        last_invoice_number = int(last_invoice.invoice_number[6:])
        print(last_invoice_number)
        next_invoice_number = '{0:02d}'.format(last_invoice_number + 1)
        print(next_invoice_number)
        invoice_number = today_string + next_invoice_number
    else:
        invoice_number = today_string + next_invoice_number


    rpt_ammount_DRarry= request.data.get('recept_ammount_DR', None)

    rcptr = len(rpt_ammount_DRarry)
    print(rcptr)

    for x in range(rcptr):

        rpt_ammount_DR= rpt_ammount_DRarry[x]['recept_ammount_DR']

        print(rpt_ammount_DR)

        rpt_ammount_CR= rpt_ammount_DRarry[x]['recept_ammount_CR']
        print(rpt_ammount_CR)
        lgacoount= rpt_ammount_DRarry[x]['atvalue']

        print(lgacoount)
        
        formatrData={
            "ledgeracoount":lgacoount,
            "recept_date":rpt_date,
            "subledgerid":subid,
            "recept_ammount_DR":rpt_ammount_DR,
            "recept_ammount_CR":rpt_ammount_CR,
            "createdby":credby,
            "createdDate":cedDate,
            "updatedby":updedby,
            "updatedDate":uatDate,
            "Branch_id":Brh_id,
            "invoice_number":invoice_number,
            "narration":nation
            }
        print(invoice_number)
        print(formatrData)
    #  print(request.data)
        #request.data=formatrData
        #finalData = json.dumps(formatrData)
        #print(finalData)
        #queryset = LedgerGroup.objects.all()
        #username = request.data.get('narration', None)
        #print(request.data)

        serializer = receptSerializers(data=formatrData)

        
        if serializer.is_valid():
            print('save hit')
            serializer.save()
            print('save hit2')
            response_message = {"statusrecpt": 1, "data": serializer.data}
                
    return Response(response_message)
""" 
""" except:
            print('error hit')
            response_message = {"statusrecpt": 0, "data": serializer.data}
        return Response(response_message) """
 
"""

"""

@api_view(['PUT'])
def receptUpdateView(request, pk):

    queryset = recept.objects.get(id=pk)

    print(queryset)

#    oldinvoice = queryset.invoice_number
#    print(oldusername)

    invoice=request.data.get('id',None)

    print(invoice)

    print(request.data)

    rpt_date= request.data.get('recept_date', None)
    subid= request.data.get('subledgerid', None)
    credby= request.data.get('createdby', None)
    cedDate= request.data.get('createdDate', None)
    updedby= request.data.get('updatedby', None)
    uatDate= request.data.get('updatedDate', None)
    Brh_id= request.data.get('Branch_id', None)
    nation= request.data.get('narration', None)


    today = datetime.date.today()
    today_string = today.strftime('%y%m%d')
#    print(today_string)
    next_invoice_number = '01'
    invoice_number='0'
    last_invoice = recept.objects.filter(invoice_number__startswith=today_string).order_by('invoice_number').last()

    print('lastinv'+str(last_invoice))

    if last_invoice:
            
        last_invoice_number = int(last_invoice.invoice_number[6:])
        print(last_invoice_number)
        next_invoice_number = '{0:02d}'.format(last_invoice_number + 1)
        print(next_invoice_number)
        invoice_number = today_string + next_invoice_number
    else:
        invoice_number = today_string + next_invoice_number


    rpt_ammount_DRarry= request.data.get('recept_ammount_DR', None)

#    rcptr = len(rpt_ammount_DRarry)
#    print(rcptr)

    for x in range(rpt_ammount_DRarry):

        rpt_ammount_DR= rpt_ammount_DRarry[x]['recept_ammount_DR']

        print(rpt_ammount_DR)

        rpt_ammount_CR= rpt_ammount_DRarry[x]['recept_ammount_CR']
        print(rpt_ammount_CR)
        lgacoount= rpt_ammount_DRarry[x]['atvalue']

        print(lgacoount)
        
        formatrData={
            "ledgeracoount":lgacoount,
            "recept_date":rpt_date,
            "subledgerid":subid,
            "recept_ammount_DR":rpt_ammount_DR,
            "recept_ammount_CR":rpt_ammount_CR,
            "createdby":credby,
            "createdDate":cedDate,
            "updatedby":updedby,
            "updatedDate":uatDate,
            "Branch_id":Brh_id,
            "invoice_number":invoice_number,
            "narration":nation
            }

        print(invoice_number)
        print(formatrData)

        serializer = receptSerializers(instance=queryse,data=formatrData)

        
        if serializer.is_valid():
            serializer.save()
            response_message = {"statusrecp": 1, "data": serializer.data}
                
        return Response(response_message)

# return Response(serializer.data)
"""

@api_view(['PUT'])
def receptUpdateView(request, pk):
    queryset = recept.objects.get(id=pk)

    print(queryset)

    oldinvoice = queryset.invoice_number
    print(oldusername)

    invoice=request.data.get('id',None)
    print(invoice)

    serializer = receptSerializers(data=request.data)

    querysetCheck = 0
    if invoice == oldinvoice:
        querysetCheck = recept.objects.filter(invoice_number=invoice).count()
    serializer = receptSerializers(instance=queryset, data=request.data)

    if querysetCheck > 0 and serializer.is_valid():
        response_message = {"statusre": 2, "data": serializer.data}
        return Response(response_message)

    else:
        try:
            if serializer.is_valid():
                serializer.save()
                response_message = {"statusre": 1, "data": serializer.data}

        except:
            response_message = {"statusre": 0, "data": serializer.data}
        return Response(response_message)

"""

@api_view(['Delete'])
def receptDeleteView(request, pk):
    queryset =recept.objects.filter(invoice_number=pk)
    queryset.delete()

    userData = recept.objects.all()
    resSerializer = receptSerializers(userData,many="true")
    data={'statusr':1,'message':'Recept deleted successfully.',"data":resSerializer.data}
    return Response(data)

"""
@api_view(['Delete'])
def receptDeleteView(request, pk):
    queryset = recept.objects.filter(invoice_number=pk)
    queryset.delete()

    return Response('Delete')

"""



# finding using subled id

 
@api_view(['GET'])
def receptget(request, pk):
    querysetCheck = recept.objects.filter(invoice_number=pk).count()
    if querysetCheck > 0:
        response_message = {
            "statusgetrecept": 1, "message": "your id is in subledgerid you can not delete"}  
    else:
        response_message = {"statusgetrecept": 0,
                            "message": "your id is not in subledgerid database ,you can delete"}
          
    return Response(response_message)
