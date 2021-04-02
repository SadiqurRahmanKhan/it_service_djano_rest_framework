from django.urls import path, include
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns

from .views import *
from Api import views,userviews,employeeviews,receptviews,subledgerviews
from .serializers import *

router = routers.DefaultRouter()
router.register('PrimaryGroup', PrimaryGroupViewSet, basename="PrimayGroup")
router.register('LedgerAccount', LedgerAccountViewSet, basename=str)
router.register('Country', CountryViewSet, basename="Country")
router.register('District', DistrcitViewSet, basename="District")
router.register('Police', PoliceStationViewSet, basename="PoliceStation")
router.register('ledger', LedgerGroupViewSet, basename="Ledger")
#router.register('JoinLedger', JoinLedgerViewSet, basename="JoinLedger")
router.register('new', LedgerGroupViewSet, basename="LedgerGroupView")
#router.register('JoinPrimaryGroupLedgerModel', JoinPGLederapi)
# searching ledger account with id and name
# router.register('LedgerAccountsearch', LedgerAccountView)


urlpatterns = [
    path("", include(router.urls)),

#   joinning table between primary group and ledger group
    path('JPGLModelList', views.JoinPGLederapiListView, name="pglglist"),
#   get by name from Ledger group and primary group
#   path('JPGLModelListsGetByName/<str:pk>/',views.JoinPGLederapiListViewGetbyName, name="pgdflglist"),
    path('JPGLModelDetail',views.JoinPGLederapiDetailView, name ="pglglist"),

#   Ledger Group

    path('ledgerGList', views.LedgerGroupListView, name="list"),
    path('ledgerGDetail/<str:pk>/', views.LedgerGroupDetailView, name="detail"),
#   Ledger Group name search
    path('ledgerGnameDetail/<str:pk>/',views.LedgerGroupnameDetailView, name="detail"),

    path('ledgerGCreate', views.LedgerGroupCreateView, name="create"),
    path('ledgerGUpdate/<str:pk>/', views.LedgerGroupUpdateView, name="update"),
    path('ledgerGDelete/<str:pk>/', views.LedgerGroupDeleteView, name="delete"),


#  Ledger Account
# filtering with list
    path('ledgeraccount/', views.ledgeraccountAPIView.as_view()),
    path('ledgerAcDetail/<str:pk>/', views.LedgerAccountDetailView, name="detail"),
    path('ledgerAcCreate', views.LedgerAccountCreateView, name="create"),
    path('ledgerAcUpdate/<str:pk>/', views.LedgerAccountUpdateView, name="update"),
    path('ledgerAcDelete/<str:pk>/', views.LedgerAccountDeleteView, name="delete"),

    path('ledgergroupget/<str:pk>/', views.LedgerAccountLedgerGroupgetView, name="detail"),

    path('ledgerAcList', views.LedgerAccountListView, name="list"),

#   Ledger account agent search with id
#   path('ledgeridget/<str:pk>/', views.LedgerAccountidView, name="detail"),
#   Ledger account name
#   path('ledgernameget/<str:pk>/', views.LedgerAccountnameView, name="detail"),
#   searching ledger account with id and name
#   path('ledgerAcDetailapimsg/<str:pk>/',LedgerAccountviewapi.as_view(), name="detail"),

#   Degignation

    path('DegignationList', views.DesignationListView, name="list"),
    path('DegignationDetail/<str:pk>/',views.DesignationDetailView, name="detail"),
    path('DegignationCreate', views.DesignationCreateView, name="create"),
    path('DegignationUpdate/<str:pk>/',views.DesignationUpdateView, name="update"),
    path('DegignationDelete/<str:pk>/',views.DesignationDeleteView, name="delete"),

#filtering
    path('desfiltering/', views.desAPIView.as_view()),
# check for delete
    path('designationdlte/<str:pk>/', views.designationget, name="list"),


#   Branch

    path('BranchList', views.BranchListView, name="list"),
    path('BranchDetail/<str:pk>/', views.BranchDetailView, name="detail"),
    path('BranchCreate', views.BranchCreateView, name="create"),
    path('BranchUpdate/<str:pk>/', views.BranchUpdateView, name="update"),
    path('BranchDelete/<str:pk>/', views.BranchDeleteView, name="delete"),

#filtering
    path('branchfiltering/', views.branchAPIView.as_view()),
# check for delete
    path('branchdlte/<str:pk>/', views.branchget, name="list"),

#   Employee

    path('EmployeeList', employeeviews.EmployeeListView, name="list"),
    path('EmployeeDetail/<str:pk>/', employeeviews.EmployeeDetailView, name="detail"),
    path('EmployeeCreate', employeeviews.EmployeeCreateView, name="create"),
    path('EmployeeUpdate/<str:pk>/', employeeviews.EmployeeUpdateView, name="update"),
    path('EmployeeDelete/<str:pk>/', employeeviews.EmployeeDeleteView, name="delete"),
   # delet using emp id   
    path('Empeedlte/<str:pk>/', employeeviews.employeeget, name="list"),
#   filtering employee ,district , designation
    path('empdegdist/', employeeviews.EmployeeAPIView.as_view()),
#   joinning table between Employe,Degignation and Branch
#    path('empDEgigBrach', employeeviews.empdesignatinbranchDetailView, name="EmpDesigBranch"),


#   District

    path('DistrictList', views.DistrictListView, name="list"),
    path('DistrictDetail/<str:pk>/', views.DistrictDetailView, name="detail"),
    path('DistrictCreate', views.DistrictCreateView, name="create"),
    path('DistrictUpdate/<str:pk>/', views.DistrictUpdateView, name="update"),
    path('DistrictDelete/<str:pk>/', views.DistrictDeleteView, name="delete"),


# police station 

    path('policeList', views.policestationListView, name="list"),
    path('policeDetail/<str:pk>/', views.policestationDetailView, name="detail"),
    path('policeCreate', views.policestationCreateView, name="create"),
    path('policeUpdate/<str:pk>/', views.policestationtUpdateView, name="update"),
    path('policeDelete/<str:pk>/', views.policestationDeleteView, name="delete"),

# Country 

    path('CountryList', views.countryListView, name="list"),
    path('CountryDetail/<str:pk>/', views.countryDetailView, name="detail"),
    path('CountryCreate', views.countryCreateView, name="create"),
    path('CountryUpdate/<str:pk>/', views.countryUpdateView, name="update"),
    path('CountryDelete/<str:pk>/', views.countryDeleteView, name="delete"),

# usertype

    path('usertypeList', userviews.userTypeListView, name="list"),
    path('usertypeDetail/<str:pk>/', userviews.userTypeDetailView, name="detail"),
    path('usertypeCreate', userviews.userTypeCreateView, name="create"),
    path('usertypeUpdate/<str:pk>/', userviews.userTypeUpdateView, name="update"),
    path('usertypeDelete/<str:pk>/', userviews.userTypeDeleteView, name="delete"),
# filering
    path('usertypefiltering/', userviews.usertypeAPIView.as_view()),
    path('usertypedlte/<str:pk>/', userviews.usertypeget, name="list"),
# user

    path('userList', userviews.userListView, name="list"),
    path('userDetail/<str:pk>/', userviews.userDetailView, name="detail"),
    path('userCreate', userviews.userCreateView, name="create"),
    path('userUpdate/<str:pk>/', userviews.userUpdateView, name="update"),
    path('userDelete/<str:pk>/', userviews.userDeleteView, name="delete"),
# user filter
    path('userfiltering/', userviews.userAPIView.as_view()),


# recept

    path('receptList', receptviews.receptListView, name="list"),
    path('receptDetail/<str:pk>/', receptviews.receptDetailView, name="detail"),
    path('receptCreate', receptviews.receptCreateView, name="create"),
    path('receptUpdate/<str:pk>/', receptviews.receptUpdateView, name="update"),
    path('recptDelete/<str:pk>/', receptviews.receptDeleteView, name="delete"),

    path('receptfiltering/', receptviews.receptAPIView.as_view()),
    path('receptdlte/<str:pk>/', receptviews.receptget, name="list"),
    
# subledger

    path('subledgertList', subledgerviews.subledgerListView, name="list"),
    path('subledgerDetail/<str:pk>/', subledgerviews.subledgerDetailView, name="detail"),
    path('subledgerCreate', subledgerviews.subledgerCreateView, name="create"),
    path('subledgerUpdate/<str:pk>/', subledgerviews.subledgerUpdateView, name="update"),
    path('subledgerDelete/<str:pk>/', subledgerviews.subledgerDeleteView, name="delete"),

    path('subfiltering/', subledgerviews.subledgerAPIView.as_view()),


]
