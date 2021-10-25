from django.db import models

class Hero(models.Model):
    name = models.CharField(max_length=60)
    alias = models.CharField(max_length=60)
    
    def __str__(self):
        return self.name
        
class Student(models.Model):
    name = models.CharField(max_length=60)
    mobile = models.CharField(max_length=60)
    country = models.CharField(max_length=60)
    gender = models.CharField(max_length=60) 
    birth_date = models.CharField(max_length=60)
    birth_month = models.CharField(max_length=60)
    birth_year = models.CharField(max_length=60)
    address1 = models.CharField(max_length=60, null=True, blank=True)
    address2 = models.CharField(max_length=60, null=True, blank=True)
    prev_qualification = models.CharField(max_length=60)    
    IELTSBand = models.CharField(max_length=60, null=True, blank=True)    
    Desiredlevel = models.CharField(max_length=60, null=True, blank=True)    
    StudyDestination = models.CharField(max_length=60)    
    IntendedSemester = models.CharField(max_length=60, null=True, blank=True  )   
    DesiredSubject = models.CharField(max_length=60)    
    email = models.CharField(max_length=60, null=True, blank=True  )
    
    def __str__(self):
        return self.name
        
class Agent(models.Model):
    name = models.CharField(max_length=60)
    role = models.CharField(max_length=60)
    country = models.CharField(max_length=60)
    agency_name = models.CharField(max_length=60)    
    
    mobile = models.CharField(max_length=60)
    website = models.CharField(max_length=60, null=True, blank=True)
    address2 = models.CharField(max_length=60, null=True, blank=True)
    offices = models.CharField(max_length=60, null=True, blank=True)    
    subagents = models.CharField(max_length=60, null=True, blank=True)    
    YearFounded = models.CharField(max_length=60, null=True, blank=True)    
    number_of_staff = models.CharField(max_length=60, null=True, blank=True)    
    services_provided = models.CharField(max_length=60, null=True, blank=True) 
    charge = models.CharField(max_length=60, null=True, blank=True)
    students_sent_abroad = models.CharField(max_length=60, null=True, blank=True)    
    association_bin = models.CharField(max_length=60, null=True, blank=True)    
    associations = models.CharField(max_length=60, null=True, blank=True)    
    recruitment_area = models.CharField(max_length=60, null=True, blank=True)    
    facebooklink = models.CharField(max_length=60, null=True, blank=True) 
    email = models.CharField(max_length=60, null=True, blank=True  )
    
    def __str__(self):
        return self.name         

        
class Uni(models.Model):
    name = models.CharField(max_length=60)
    mobile = models.CharField(max_length=60)
    country = models.CharField(max_length=60)
    UGfee = models.CharField(max_length=60, null=True, blank=True)    
    PGfee = models.CharField(max_length=60, null=True, blank=True)
    Diplomafee = models.CharField(max_length=60, null=True, blank=True)
    AccomodationCost = models.CharField(max_length=60, null=True, blank=True)
    FallSemester = models.CharField(max_length=60, null=True, blank=True)
    SpringSemester = models.CharField(max_length=60, null=True, blank=True)    
    SummerSemester = models.CharField(max_length=60, null=True, blank=True)    
    ranking = models.CharField(max_length=60, null=True, blank=True)    
    email = models.CharField(max_length=60, null=True, blank=True  )
    
    def __str__(self):
        return self.name    

class Product(models.Model):
    name = models.CharField(max_length=60)
    partner = models.CharField(max_length=60)
    branches = models.CharField(max_length=60, null=True, blank=True)
    product_type = models.CharField(max_length=60)    
    approx_fee = models.CharField(max_length=60)
    revenue_type = models.CharField(max_length=60, null=True, blank=True)
    intake_month = models.CharField(max_length=60, null=True, blank=True)
    duration = models.CharField(max_length=60, null=True, blank=True)
    description = models.CharField(max_length=60, null=True, blank=True)
    
    def __str__(self):
        return self.name  


class Service(models.Model):
    name = models.CharField(max_length=60)
    partner = models.CharField(max_length=60)
    branches = models.CharField(max_length=60, null=True, blank=True)
    product_type = models.CharField(max_length=60)    
    approx_fee = models.CharField(max_length=60)
    revenue_type = models.CharField(max_length=60, null=True, blank=True)

    duration = models.CharField(max_length=60, null=True, blank=True)
    description = models.CharField(max_length=60, null=True, blank=True)
    
    def __str__(self):
        return self.name         
        

class Application(models.Model):
    client_name = models.CharField(max_length=60)
    applied_intake_date = models.CharField(max_length=60, null=True, blank=True)
    client_phone = models.CharField(max_length=60, null=True, blank=True)
    client_assignee = models.CharField(max_length=60, null=True, blank=True)    
    application_assignee = models.CharField(max_length=60, null=True, blank=True)
    product = models.CharField(max_length=60, null=True, blank=True)

    partner = models.CharField(max_length=60, null=True, blank=True)
    partner_branches = models.CharField(max_length=60, null=True, blank=True)
    partners_client_id = models.CharField(max_length=60, null=True, blank=True)
    work_flow = models.CharField(max_length=60, null=True, blank=True)
    application_start_by = models.CharField(max_length=60, null=True, blank=True)
    application_start_by_branch = models.CharField(max_length=60, null=True, blank=True)
    status = models.CharField(max_length=60, null=True, blank=True)
    stage_in_queue = models.CharField(max_length=60, null=True, blank=True)
    created_at = models.CharField(max_length=60, null=True, blank=True)
    
    def __str__(self):
        return self.name  
        
class User(models.Model):
    email = models.CharField(max_length=60)
    usertype = models.CharField(max_length=60)
      
    def __str__(self):
        return self.email   
        
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='post_images')
    
    def __str__(self):
        return self.title        
# Create your models here.
