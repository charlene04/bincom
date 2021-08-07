from django.db import models
from django.db.models.fields.related import ForeignKey

# Create your models here.

class Polling_unit(models.Model):
    uniqueid = models.IntegerField(primary_key=True)
    polling_unit_id =models.IntegerField(null=False, blank=True)
    ward_id = models.IntegerField( null=True, blank=True)
    lga_id = models.IntegerField( null=True, blank=True)
    uniquewardid = models.IntegerField(null=True) 
    polling_unit_number = models.CharField(max_length=50, null=True)
    polling_unit_name = models.CharField(max_length=50, null=True)
    polling_unit_description = models.TextField( null=True)
    lat = models.CharField(max_length=255, null=True)
    long = models.CharField(max_length=255, null=True) 
    entered_by_user: models.CharField(max_length=50, null=True)
    date_entered: models.DateTimeField( null=True)
    user_ip_address: models.CharField(max_length=50, null=True)
    def __str__(self):
        return self.polling_unit_name
    
    
class Agentname(models.Model):
    name_id = models.IntegerField(primary_key=True)
    firstname = models.CharField(max_length=255, null=True)
    lastname = models.CharField(max_length=255,  null=True)
    email: models.EmailField(max_length=255,  null=True)
    phone: models.CharField(max_length=13,  null=True)
    pollingunit_uniqueid= models.ForeignKey(Polling_unit, on_delete=models.CASCADE, db_column='pollingunit_uniqueid')
    
    def __str__(self):
        return '{} {}'.format(self.firstname , self.lastname)
    
    
class Announced_lga_results(models.Model):
    result_id = models.IntegerField(primary_key=True, default=0)
    lga_name = models.CharField(max_length=50,  null=True)
    party_abbreviation = models.CharField(max_length=4,  null=True)
    party_score = models.IntegerField( null=True)
    entered_by_user: models.CharField(max_length=50,  null=True)
    date_entered: models.DateTimeField( null=True)
    user_ip_address: models.CharField(max_length=50,  null=True)
    def __str__(self):
        return '{} | {} | {}'.format(self.lga_name , self.party_abbreviation, self.party_score)
    
class Announced_pu_results(models.Model):
    result_id = models.IntegerField(primary_key=True, default=0)
    polling_unit= models.ForeignKey(Polling_unit, on_delete=models.CASCADE, db_column='polling_unit_uniqueid')
    party_abbreviation = models.CharField(max_length=4,  null=True)
    party_score = models.IntegerField( null=True)
    entered_by_user: models.CharField(max_length=50, null=True)
    date_entered: models.DateTimeField( null=True)
    user_ip_address: models.CharField(max_length=50,  null=True)
    def __str__(self):
        return '{} {}'.format(self.party_abbreviation, self.party_score)
    
    
class Announced_state_results(models.Model):
    result_id = models.IntegerField(primary_key=True,default=0)
    state_name = models.CharField(max_length=50,  null=True)
    party_abbreviation = models.CharField(max_length=4,  null=True)
    party_score = models.IntegerField( null=True)
    entered_by_user: models.CharField(max_length=50, null=True)
    date_entered: models.DateTimeField( null=True)
    user_ip_address: models.CharField(max_length=50,  null=True)
    def __str__(self):
        return self.state_name
    
class Announced_ward_results(models.Model):
    result_id = models.IntegerField(primary_key=True,default=0)
    ward_name = models.CharField(max_length=50, null=True)
    party_abbreviation = models.CharField(max_length=4,  null=True)
    party_score = models.IntegerField( null=True)
    entered_by_user: models.CharField(max_length=50,  null=True)
    date_entered: models.DateTimeField( null=True)
    user_ip_address: models.CharField(max_length=50,  null=True)
    def __str__(self):
        return self.ward_name
    
class Lga(models.Model):
    uniqueid = models.IntegerField(primary_key=True,default=0)
    lga_id = models.IntegerField( null=True, blank=True)
    lga_name = models.CharField(max_length=50,  null=True)
    state_id = models.IntegerField( null=True, blank=True)
    lga_description = models.TextField( null=True) 
    entered_by_user: models.CharField(max_length=50,  null=True)
    date_entered: models.DateTimeField( null=True)
    user_ip_address: models.CharField(max_length=50,  null=True)
    def __str__(self):
        return self.lga_name
    
class Party(models.Model):
    id = models.IntegerField(primary_key=True)
    partyid = models.CharField(max_length=11, null=True)
    partyname = models.CharField(max_length=11, null=True)    
    def __str__(self):
        return self.partyname
    

    
    
class States(models.Model):
    state_id = models.IntegerField(primary_key=True, null=False, blank=True)
    state_name = models.CharField(max_length=50,  null=True)
    def __str__(self):
        return self.state_name
    
    
class Ward(models.Model):
    uniqueid = models.IntegerField(primary_key=True, default=0)
    ward_id = models.IntegerField(null=True)
    ward_name= models.CharField(max_length=50, null=True)
    lga_id= models.IntegerField(null=True)
    ward_description= models.TextField(null=True)   
    entered_by_user: models.CharField(max_length=50, null=True)
    date_entered: models.DateTimeField( null=True)
    user_ip_address: models.CharField(max_length=50,  null=True)
    def __str__(self):
        return self.ward_name