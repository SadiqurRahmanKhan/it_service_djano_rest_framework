from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(LedgerGroup)
admin.site.register(PrimaryGroup)
admin.site.register(Countrydb)
admin.site.register(District)
admin.site.register(PoliceStation)
admin.site.register(LedgerAccount)
#admin.site.register(JoinPrimaryGroupLedgerModel)
admin.site.register(Designationdb)
admin.site.register(Branchdb)
admin.site.register(Employee)
#admin.site.register(EmpDesBranch)
admin.site.register(userType)
admin.site.register(AssociatUser)
admin.site.register(recept)
admin.site.register(subledger)


