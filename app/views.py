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
import itertools, operator
import django_saml2_auth.views
from .forms import SessionForm
from .forms import ParticipantForm

from io import BytesIO
from django.template.loader import get_template
from django.views import View
from xhtml2pdf import pisa
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

    country_count = Participant.objects.values('country').annotate(total_user = Count('id')).order_by('country')
 
    context = {"session": session, "participants": participants, "total_participant":total_participant, "total_courses": total_courses, "total_session": total_session, "total_course_comp": total_course_comp, }
    return render(request, "index.html", context)


def myview(request):
    tempData = {'firstname': 'bob','lastname': 'jones'}
    weather = "sunny"
    data = {
        'person': tempData,
        'weather': weather
    }
    return render(request,'pages/maps.html',{'data':data}) 

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

# Participant View to edit on template.

def participant(request, pk):
    part_data = Participant.objects.get(id=pk)

    return render(request,'pages/icons.html',{'part_data':part_data}) 

# Session View to edit on template.
def sessionView(request, pk):
    session_data = Session.objects.get(id=pk)

    return render(request,'pages/maps.html',{'session_data':session_data}) 



#Results Data
@login_required(login_url="/login/")
def resultData(request):
    sesions = Session.objects.all()
    context = {"sesions": sesions}
    print(sesions)
    return render(request, "pages/index.html", context)  
    
#Session form

def createSession(request):

    form = SessionForm
    if request.method == 'POST':
        print('Printing POST:', request.POST)
        form = SessionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')


    context = {"form": form }

    return render(request,'pages/session.html', context)

#participant form

def createParticipant(request):
    
    formNew = ParticipantForm
    if request.method == 'POST':
        print('Printing POST:', request.POST)
        formNew = ParticipantForm(request.POST)
        if formNew.is_valid():
            formNew.save()
            return redirect('/')    

    context = {"formNew": formNew }

    return render(request,'pages/participant_form.html', context)
 

#passing value in a dictionary

from django.shortcuts import render
from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from django.views import View
from xhtml2pdf import pisa

def render_to_pdf(template_src, context_dict={}):
	template = get_template(template_src)
	html  = template.render(context_dict)
	result = BytesIO()
	pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
	if not pdf.err:
		return HttpResponse(result.getvalue(), content_type='application/pdf')
	return None


data = {
	"company": "Viti Tolu Company",
	"address": "123 Street name",
	"city": "Suva",
	"state": "Nausori",
	"zipcode": "98663",


	"phone": "555-555-2345",
	"email": "youremail@dennisivy.com",
	"website": "Vitiana.com",
	}

#Opens up page as PDF
class ViewPDF(View):
	def get(self, request, *args, **kwargs):

		pdf = render_to_pdf('pages/pdf_template.html', data)
		return HttpResponse(pdf, content_type='application/pdf')


#Automaticly downloads to PDF file
class DownloadPDF(View):
	def get(self, request, *args, **kwargs):
		
		pdf = render_to_pdf('pages/pdf_template.html', data)

		response = HttpResponse(pdf, content_type='application/pdf')
		filename = 'Invoice_%s.pdf' %("12341231")
		content = "attachment; filename='%s'" %(filename)
		response['Content-Disposition'] = content
		return response



def pdf(request):
	context = {}
	return render(request, 'pages/pdf.html', context)

    

    









    
