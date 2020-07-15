# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

from django.db import models
from import_export import fields, resources
# Create your models here.
from datetime import date
from django.urls import reverse
from django import forms

from django.forms import ModelChoiceField
from django_countries.fields import CountryField
import birthday
from import_export.widgets import ManyToManyWidget
accredited = (

    ("y", "Yes"),
    ("n", "No")
)
gender = (
        ("Male", "Male"),
        ("Female", "Female"),
        ("Other", "Other")
    )

#-------------------------------------------------------# 
title_Choice = (
        ("Mr", "Mr"),
        ("Mrs", "Mrs"),
        ("Dr", "Dr"),
        ("Hon", "Hon")
    )


sector_Choice = (
        ("CS", "Civil Service"),
        ("IO", "International Organization"),
        ("NG", "National Government"),
        ("PS", "Private Sector"),
        ("RO", "Regional Organization"),
        ("O", "Others")
    )

special_general_Choice = (
        ("ad", "ADMINISTRATION"), 
        ("sg", "AGRICULTURE"), 
        ("ar", "ARCHITECTURE"), 
        ("br", "BROADCASTING OR MEDIA"), 
        ("co","COMMUNICATIONS"), 
        ("cm","COMMUNITY DEVELOPMENT"), 
        ("de","DEFENSE"), 
        ("di","DISASTER MANAGEMENT"),
        ("ec","ECONOMICS"), 
        ("eu", "EDUCATION AND TRAINING AND PUBLIC AWARENESS"), 
        ("el","ELECTIRCIAN"), 
        ("fi","FINANCE"), 
        ("fr", "FIRE AND SEARCH AND RESCUE"), 
        ("fi","FIRST AID INSTRUCTOR"), 
        ("fo","FOREIGN AFFAIRS"),
        ("he","HEALTH EDUCATION"), 
        ("la","LAND VALUATION"), 
        ("ma","MANAGEMENT"), 
        ("mr","MARITIME"), 
        ("me","MEDICAL METEREOLOGICAL_SERVICES"), 
        ("mi","MINERAL RESOURCES"), 
        ("na","NATIONAL PLANNING"), 
        ("po","POLICE"), 
        ("","PRISON SERVICES"),
        ("pu","PUBLIC HEALTH"), 
        ("pb","PUBLIC WORK AND WATER"), 
        ("re","RED CROSS"), 
        ("rs","RESEARCH DEPARTMENT"), 
        ("tr", "TRANSPORT")
        
    )
special_disaster_management_Choice = (
        ("co","COORDINATION"), 
        ("da","DAMAGE ASSEMENT AND PLANNING"),
        ("", "DISASTER OPERATION"), 
        ("ed", "EDUCATION AND TRAINING"), 
        ("ha","HAZARD ASSEMENT"), 
        ("mi","MITIGATION AND PREVENTION"),
        ("ne","NEEDS ANALYSIS AND IMPLEMENTATION"), 
        ("pr","PREPAREDNESS PLANNING")
    )
education_level_choice = (
        ("pr", "Primary"),
        ("se", "Secondary"),
        ("te", "Tertiary"),
        ("vo", "Vocational")
    )
 
trainer = (
        ("yes", "Yes"),
        ("no", "No")
    )
method_Choice = (
        ("tc","TrainingCL"),
        ("t", "Training"),
        ("w", "Workshop"),
        
    )
period_Choice = (
        ("Hours", "Hours"),
        ("Days", "Days"),
        ("Weeks", "Weeks"),
        ("months", "Months")
    )

session_type_choices = (
        ("in","in_country technical assistance"), 
        ("ic","international course"), 
        ("na","national course"), 
        ("ns","national seminar or workshop"), 
        ("po","post grad certificate programs"), 
        ("rc","regional course"), 
        ("re","regional seminar or workshop"), 
        ("su","sub national course"),
        ("c", "Consultation")
    )

completion_choices = (
    ("c", "Completed"),
    ("nc", "Not Completed")
)

class Organization(models.Model):
    organization = models.CharField(max_length=100, blank=True, null=True, unique=True)
    
    special_general = models.CharField(choices= special_general_Choice, max_length=200, blank=True, null=True)
   
    special_disaster_management = models.CharField(choices = special_disaster_management_Choice, max_length=100, blank=True, null=True)
    sector = models.CharField(choices= sector_Choice, max_length=100, blank=True, null=True)
    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return self.organization
    
    def get_absolute_url(self):
        return reverse('Partcipant detail', args=[str(self.organization)])

    def get_hostname(self):
        return "\n".join([s.hostname for s in self.host_participant.all()])
  

class Program(models.Model):
    project_name = models.CharField(max_length=100)
    ojective = models.CharField(max_length=200, blank=True, null=True)
    
    def __str__(self):
         return self.project_name

    def get_absolute_url(self):
        return reverse('Project detail', args=[str(self.project_name)])

class Participant(models.Model):
    first_name = models.CharField(max_length=100)
    last_Name = models.CharField(max_length=100)
    country = CountryField()
    trainer = models.CharField(choices = trainer, max_length=100, )
    gender = models.CharField(choices= gender, max_length=50)    
    title = models.CharField(choices= title_Choice, max_length=100, blank=True, null=True)
    date_of_birth = models.DateField(null=True, blank=True )
    position = models.CharField(max_length=1000) 
    contact_address = models.CharField(max_length=1000, blank=True, null=True)
    work_phone = models.CharField(max_length = 30, blank=True, null=True)
    fax_number = models.CharField(max_length = 100, blank=True, null=True)
    home_phone = models.CharField(max_length=30, blank=True, null=True)
    email = models.EmailField
    #previous_employment = models.CharField(max_length=100, blank=True, null=True)
    organization = models.ManyToManyField(Organization, related_name = 'host_organization')
    #role = models.ForeignKey(Role,  on_delete=models.CASCADE)
    
    education_level = models.CharField(choices = education_level_choice, max_length=100, blank=True, null=True)
   
    comments = models.CharField(max_length=1000, blank=True, null=True)
    #remove later
    def get_verifed_req_count(self):
        return id.count()


    def hostname(self):
        return "\n".join([s.hostname for s in self.host_participant.all()], [p.ListOfParticpantsWhoCompletedCourse for p in self.courseparticipant.all])
    
    def get_course_completed(self):
         return "\n".join([p.ListOfParticpantsWhoCompletedCourse for p in self.courseparticipant.all])

    def __unicode__(self):
        return "{0}".format(self.first_name)
        
    def get_organization(self):
        return "\n".join([p.organization for p in self.organization.all()])
    
    def get_hostname(self):
       return '%s,%s' % ("\n".join([p.session for p in self.host_particpant.all()]), "\n".join([p.ListOfParticpantsWhoCompletedCourse for p in self.courseparticipant.all()]))
    
       #ret = ''
       #print(self.hostname.all())
       #for session in self.session.all():
       #ret = ret + session.session_name + ','
       #return ret[:-1]
        

    
    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return 'First name - %s, Surname - %s, Date of birth - %s, Gender - %s, Country - %s ' % (self.first_name,  self.last_Name, self.date_of_birth,self.gender, self.country)
    
    #def get_absolute_url(self):
    #    return reverse('Partcipant detail', args=[str(self.first_name)])

class Project(models.Model):
    program = models.ForeignKey(Program, on_delete=models.CASCADE, blank=True, null=True)
    project_name = models.CharField(max_length=100, blank=True, null=True)
    donor = models.CharField(max_length = 100, blank=True, null=True)
    odjective = models.CharField(max_length=1000, blank=True, null=True)
    work_plan = models.CharField(max_length=1000, blank=True, null=True)
    key_result_area = models.CharField(max_length=1000, blank=True, null=True)
    output = models.CharField(max_length= 1000, blank=True, null=True)
    evaluation = models.CharField(max_length= 1000, blank=True, null=True)
    budget = models.FloatField
    funding = models.CharField(max_length=1000, blank=True, null=True)
    head_of_project = models.CharField(max_length=1000, blank=True, null=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True, )
    target_audience = models.CharField(max_length=1000, blank=True, null=True)
    overview_about_project = models.CharField(max_length=1000, blank=True, null=True)

    
    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return self.project_name

    def get_absolute_url(self):
        return reverse('Project detail', args=[str(self.project_name)])

class Course(models.Model):
    course_title = models.CharField(max_length= 100, blank=True, null=True)
   
    program = models.ForeignKey(Program, on_delete=models.CASCADE, blank=True, null=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True, blank=True)
    accredited = models.CharField(choices= accredited, max_length= 100, blank=True, null=True)
    description = models.CharField(max_length=1000, blank=True, null=True)
    documents = models.FileField(null=True, blank=True)
    #comments = models.CharField(max_length= 1000, blank=True, null=True)

    
    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return self.course_title

    def get_absolute_url(self):
        return reverse('Project detail', args=[str(self.documents)])

class Unit(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, blank=True, null=True)
    unit_id = models.CharField(max_length= 100, blank=True, null=False, primary_key=True)
    unit_name = models.CharField(max_length=1000, blank=True, null=True)


    def __str__(self):
        return '%s %s'% (self.course, self.unit_name)



    #def __str__(self):
        #"""String for representing the Model object (in Admin site etc.)"""
     #   return self.unit_name

    def get_absolute_url(self):
        return reverse('Unit detail', args=[str(self.unit_name)])

class Session(models.Model):
    name_of_activity = models.CharField(max_length=100)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    course_unit_names = models.ForeignKey(Unit, on_delete=models.CASCADE, blank=True, null=True)
    documents = models.FileField(null=True, blank=True)

    country = CountryField()
    day_number = models.CharField( max_length=100, blank=True, null=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    attendees_number = models.IntegerField(default = 1, blank=True, null=True)
    method = models.CharField(choices= method_Choice, blank=True, null=True, max_length=50)
    
    period = models.CharField(choices= period_Choice, blank=True, null=True, max_length=50)
   
    session_type = models.CharField(choices=session_type_choices, max_length=50, blank=True, null=True)
    description = models.CharField(max_length=1000, blank=True, null=True)
    comment = models.CharField(max_length=1000, blank=True, null=True)
    #participant = models.ManyToManyRel(Participant, torelated_name=None)
    participant = models.ManyToManyField(Participant, related_name='host_participant')


    #pdf = models.FileField()
    def __unicode__(self):
        return "{0}".format(self.title)

    def get_participant(self):
        return "\n".join([p.first_name for p in self.participant.all()])
    
    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return ' %s ' % (self.name_of_activity)

    def get_absolute_url(self):
        return reverse('Session detail', args=[str(self.name_of_activity)])
    def get_hostname(self):
       return "\n".join([p.session for p in self.host_session.all()])

    #def get_absolute_url(self):
     #   return reverse('Session participant', args=[str(self.attendees)])from django.db import models

class ListOfParticpantsWhoCompletedCourse(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    unit_name = models.ForeignKey(Unit, on_delete=models.CASCADE)
    sessions = models.ManyToManyField(Session, related_name = 'host_session')
    participant_list = models.ManyToManyField(Participant, related_name='courseparticipant')

    def get_participant(self):
        return "\n".join([p.first_name for p in self.participant_list.all()])

    def __str__(self):
        return '%s '% (self.course)



