from django.db import models

# Create your models here.
class PrimaryGroup(models.Model):
	GName = models.CharField(max_length=5000)

	def __str__(self):
		return self.GName

class LedgerGroup(models.Model):
    name = models.CharField(max_length = 50000)
    primaryID = models.IntegerField(null=True)
    upperGID = models.IntegerField(null=True)
    
    created_by=models.CharField(max_length = 1000,null=True)
    created_date= models.DateTimeField(auto_now_add=True,null=True)
    updated_by=models.CharField(max_length = 1000,null=True)
    updated_date= models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.name

class Countrydb(models.Model):
	CName = models.CharField(max_length = 255,null=True)

	def __str__(self):
		return self.CName

class District(models.Model):
	DName = models.CharField(max_length = 50000,null=True)

	def __str__(self):
		return self.DName

class PoliceStation(models.Model):
	StationName = models.CharField(max_length = 50000,null=True)

	def __str__(self):
		return self.StationName

def upload_to_led(instance,filename):
    return 'ledimage/{filename}'.format(filename=filename)

class LedgerAccount(models.Model):
	name = models.CharField(max_length = 255)
	fatherName = models.CharField(max_length = 50000,null=True)
	motherName = models.CharField(max_length = 50000,null=True)
	bloodGroup = models.CharField(max_length = 255,null=True)
	parmanentAddress = models.CharField(max_length = 1000000,null=True)
	presentAddress = models.CharField(max_length = 1000000,null=True)
	email = models.EmailField(null=True)
	dateOfBirth = models.DateField(null=True)
	mobile = models.IntegerField(null=True)
	country = models.ForeignKey(Countrydb,null=True ,on_delete=models.CASCADE)
	district = models.ForeignKey(District, null=True,on_delete = models.CASCADE)
	policeStation = models.ForeignKey(PoliceStation,null=True, on_delete = models.CASCADE)
	ledger_image = models.ImageField(blank=True,null=True,upload_to=upload_to_led,default='ledimage/led.jpg')
	nid = models.CharField(max_length= 200000,null=True)

	ledgerGroupId = models.ForeignKey(LedgerGroup,null=True, on_delete = models.CASCADE)
    


""" 
class JoinLedger(models.Model):
    Lid =models.IntegerField(primary_key=True)
    Lname = models.CharField(max_length = 50000,null=True)
    GName = models.CharField(max_length = 50000,null=True)
     """
    
# 01-02-2021 

class Designationdb(models.Model):
    designation_name =models.CharField(max_length = 50000,null=True)

   
class Branchdb(models.Model):
    branch_name =models.CharField(max_length = 50000,null=True)

    createdby=models.CharField(max_length = 500,null=True)
    createdDate=models.DateTimeField(auto_now_add=False)
    updatedby=models.CharField(max_length = 500,null=True)
    updatedDate=models.DateTimeField(auto_now_add=False)

    
 
def upload_to(instance,filename):
    return 'empimage/{filename}'.format(filename=filename)

class Employee(models.Model):
    employee_NID = models.CharField(max_length = 100000)
    employee_degignation_id = models.ForeignKey(Designationdb,null=True,on_delete=models.CASCADE)
    employee_name= models.CharField(max_length = 5000)
    employee_gender =models.CharField(max_length = 20,null=True)
    employee_date_of_birth = models.CharField(max_length=255,null=True)
    employee_address = models.CharField(max_length = 5000,null=True)
    employee_mobile =models.CharField(max_length = 100,null=True)
    employee_email =models.CharField(max_length = 10000,null=True)
    employee_joinning_date =models.DateTimeField(auto_now_add=True,null=True)
    employee_bacic = models.FloatField(null=True)
    employee_status = models.IntegerField(null=True)
    employee_qualification_dtails= models.CharField(max_length=20000,null=True)
    employee_created_by = models.CharField(max_length=1000,null=True)
    employee_date = models.DateTimeField(auto_now_add=True,null=True)
    employee_updated_by=models.CharField(max_length = 1000,null=True)
    employee_updated_date= models.DateTimeField(auto_now_add=True,null=True)
    employee_image=models.ImageField(blank=True,null=True,upload_to=upload_to,default='empimage/emp.jpg')
    employee_branch_id=models.ForeignKey(Branchdb,null=True,on_delete=models.CASCADE)
    employee_skills =models.CharField(max_length = 20000,null=True)
    employee_nic_name= models.CharField(max_length=1000,null=True)
    employee_Father_name= models.CharField(max_length=1000,null=True)
    employee_Mother_name= models.CharField(max_length=1000,null=True)
    employee_sponsor_name = models.CharField(max_length=1000,null=True)
    employee_village = models.CharField(max_length= 50000,null=True)
    employee_postoffice = models.CharField(max_length =50000,null=True)
    employee_police_stations = models.CharField(max_length=50000,null=True)
    employee_District_id = models.ForeignKey(District,null=True,on_delete=models.CASCADE)
    employee_facebook_link= models.CharField(max_length=50000,null=True)

    def __str__(self):
        return self.employee_name



# User type 

class userType(models.Model):
    userType_name= models.CharField(max_length = 500,null=False)


# User 

class AssociatUser(models.Model):
    user_code=models.IntegerField()
    user_name=models.CharField(max_length = 500,null=False)
    email=models.CharField(max_length = 500,null=True)
    password=models.CharField(max_length = 500,null=False)
    full_name=models.CharField(max_length = 500,null=False)
    usertype=models.ForeignKey(userType,on_delete=models.CASCADE,null=False)
    createdby=models.CharField(max_length = 500,null=True)
    createdDate=models.DateTimeField(auto_now_add=True)
    updatedby=models.CharField(max_length = 500,null=True)
    updatedDate=models.DateTimeField(auto_now_add=True)
    employeeid=models.ForeignKey(Employee,on_delete=models.CASCADE,null=False)


# 07/03/21

class subledger(models.Model):
    name=models.CharField(max_length=500,null=True)

    createdby=models.CharField(max_length = 500,null=True)
    createdDate=models.DateTimeField(auto_now_add=True)
    updatedby=models.CharField(max_length = 500,null=True)
    updatedDate=models.DateTimeField(auto_now_add=True)



class recept(models.Model):
    ledgeracoount=models.ForeignKey(LedgerAccount,on_delete=models.CASCADE,null=False)
    recept_date=models.DateTimeField(auto_now_add=True)
    subledgerid=models.ForeignKey(subledger,on_delete=models.CASCADE,null=False)
    recept_ammount_DR=models.IntegerField()
    recept_ammount_CR=models.IntegerField()
    invoice_number=models.CharField(blank=True, max_length=8)

    createdby=models.CharField(max_length = 500,null=True)
    createdDate=models.DateTimeField(auto_now_add=True)
    updatedby=models.CharField(max_length = 500,null=True)
    updatedDate=models.DateTimeField(auto_now_add=True)

    Branch_id=models.ForeignKey(Branchdb,on_delete=models.CASCADE,null=False)
    narration=models.CharField(max_length=100000,null=True)