from rest_framework import serializers
from rest_flex_fields import FlexFieldsModelSerializer
from .models import *
from .vmodel import *

# Ledger Account
class LedgerAccountSerializers(serializers.ModelSerializer):
    class Meta:
        model = LedgerAccount 
        fields = "__all__"


class LedgerAccountSerializers1(serializers.ModelSerializer):
    class Meta:
        model = LedgerAccount 
        fields = "__all__"
        depth=1

# primary group
class PrimaryGroupSerializers(serializers.ModelSerializer):
    class Meta:
        model = PrimaryGroup 
        fields = "__all__"

# country 
class CountrySerializers(serializers.ModelSerializer):
    class Meta:
        model = Countrydb
        fields = "__all__"

# district
class DistrictSerializers(serializers.ModelSerializer):
    class Meta:
        model = District 
        fields = "__all__"

# police station
class PoliceStationSerializers(serializers.ModelSerializer):
    class Meta:
        model = PoliceStation 
        fields = "__all__"
        
class LedgerGroupSerializers(serializers.ModelSerializer):
    class Meta:
        model = LedgerGroup
        fields = "__all__"

class PrimaryGroupSerializer(serializers.ModelSerializer):
    name = serializers.CharField( max_length=23)
    class Meta:
        model = PrimaryGroup
        fields = ('GName')

class LedgerGroupSerializer(serializers.ModelSerializer):
    primary = PrimaryGroupSerializer()
    class Meta:
        model = LedgerGroup
        fields = ('id','name','primary')

""" 
class JoinLedgerSerializers(serializers.ModelSerializer):
    class Meta:
        model = JoinLedger 
        fields = ["Lid", "Lname", "GName"]
         """

class JoinPGSerializers(serializers.ModelSerializer):
    class Meta:
        model= JoinPrimaryGroupLedgerModel
        fields = ['id','lgname','pgname','upgname']
        
class DesignationSerializers(serializers.ModelSerializer):
    class Meta:
        model= Designationdb
        fields = "__all__"
        
class BranchSerializers(serializers.ModelSerializer):
    class Meta:
        model= Branchdb
        fields = "__all__"
        
class EmployeeSerializers(serializers.ModelSerializer):
    class Meta:
        model= Employee
        fields = "__all__"

class EmployeeSerializers1(serializers.ModelSerializer):
    class Meta:
        model= Employee
        fields = "__all__"
        depth=1
        
        
        
        
# Employee list from employee,degignation and branch table 

""" class JoinEmpDesigBranchSerializers(serializers.ModelSerializer):
    class Meta:
        model= EmpDesBranch
        fields = ['id','name','email','mobile','degignation','branch']
   """      

# user type
class userTypeSerializers(serializers.ModelSerializer):
    class Meta:
        model= userType
        fields = "__all__"
# associate user
class userSerializers(serializers.ModelSerializer):
    class Meta:
        model=AssociatUser
        fields = "__all__"

# associate user for filtering and depth 
class userSerializers1(serializers.ModelSerializer):
    class Meta:
        model=AssociatUser
        fields = "__all__"
        depth = 1

# 07/03/21

class subledgerSerializers(serializers.ModelSerializer):
    class Meta:
        model=subledger
        fields = "__all__"

class subledgerSerializers1(serializers.ModelSerializer):
    class Meta:
        model=subledger
        fields = "__all__"
        depth=1

class receptSerializers(serializers.ModelSerializer):
    class Meta:
        model=recept
        fields = "__all__"

class receptSerializers1(serializers.ModelSerializer):
    class Meta:
        model=recept
        fields = "__all__"
        depth= 1