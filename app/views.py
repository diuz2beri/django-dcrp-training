# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse, JsonResponse
from .models import *
from django.db.models import Count, Sum
import pandas as pd
# ...

@login_required(login_url="/login/")
def index(request):
    participants = Participant.objects.all()
    total_participant = participants.count()

    courses = Course.objects.all()
    total_courses = courses.count()

    session = Session.objects.all()
    total_session = session.count()

    course_comp = ListOfParticpantsWhoCompletedCourse.objects.all()
    total_course_comp = course_comp.count()

    labels = []
    data = []

    country_count = Participant.objects.values('country').annotate(total_user = Count('id'))
    
    #for country in country_count:
     #   labels.append(country) 
      #  data.append(total_user)
        


    context = {"participants": participants, "total_participant":total_participant, "total_courses": total_courses, "total_session": total_session, "total_course_comp": total_course_comp, }
    return render(request, "index.html", context)

@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]
        template = loader.get_template('pages/' + load_template)
        return HttpResponse(template.render(context, request))

    except:

        template = loader.get_template( 'pages/error-404.html' )
        return HttpResponse(template.render(context, request))

# Views Code Here.

def map(request):
    participants = Participant.objects.all()
    total_participant = participants.count()

    courses = Course.objects.all()
    total_courses = courses.count()

    session = Session.objects.all()
    total_session = session.count()

    course_comp = ListOfParticpantsWhoCompletedCourse.objects.all()
    total_course_comp = course_comp.count()

    shops = Participant.objects.all().values('country')

    context = {"shops": shops, "participants": participants, "total_participant":total_participant, "total_courses": total_courses, "total_session": total_session, "total_course_comp": total_course_comp}
    return render(request, "maps.html", context)

#Results Data

def resultData(request, obj):
    county_dataset = []
    
    shops = Participant.objects.all().values('country').annotate(total=Count('country'))

    

    









    
