# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""
import pandas as pd
import itertools, operator
import django_saml2_auth.views
from django.http import HttpResponse, JsonResponse
from io import BytesIO
from django.template.loader import get_template
from django.views import View
from xhtml2pdf import pisa
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from .models import *
from django.db.models import Count, Sum
from .forms import SessionForm
from .forms import ParticipantForm
from django.views import generic
from .filters import ParticipantFilter, sessionFilter
from django_filters.views import FilterView
from django.views.generic import TemplateView

# ...

@login_required(login_url="/login/")
def index(request):
    participants = Participant.objects.all().order_by("-pk")
    total_participant = participants.count()

    courses = Course.objects.all()
    total_courses = courses.count()

    session = Session.objects.all().order_by("-pk")
    total_session = session.count()

    course_comp = ListOfParticpantsWhoCompletedCourse.objects.all()
    total_course_comp = course_comp.count()

    country_count = Participant.objects.values('country').annotate(total_user = Count('id')).order_by('country')

    context = {"session": session, "participants": participants, "total_participant":total_participant, "total_courses": total_courses, "total_session": total_session, "total_course_comp": total_course_comp, }
    return render(request, "index.html", context)


def get_data(request, *args, **kwargs):
    data = {
        "sales": 100,
        "Customer": 10,

    }
    return JsonResponse(data)




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
############################################################################################
# Participant View to edit on template./ create session / create participant
############################################################################################

def participant(request, pk):
    part_data = Participant.objects.get(id=pk)
    list_part = Session.objects.filter(participant=pk).count()

    session_data = Session.objects.filter(participant=pk)
    return render(request,'pages/icons.html', {'session_data':session_data, 'list_part':list_part,'part_data':part_data})

# Session View to edit on template.
def sessionView(request, pk):
    session_data = Session.objects.get(id=pk)
    sesion = Session.objects.all()
    list_part = 2
    myFilter = sessionFilter(request.GET, queryset=sesion)
    sesion = sessionFilter.qs

    context = {'myFilter': myFilter, 'list_part':list_part,'session_data':session_data, "sesion": sesion}
    return render(request,'pages/maps.html', context)


def deleteParticipant(request):

    return render(request)


#Results Data
@login_required(login_url="/login/")
def resultData(request):
    sesions = Session.objects.all()
    context = {"sesions": sesions}
    print(sesions)
    return render(request, "pages/index.html", context)

###################################################################################################
#View for all forms
##################################################################################################

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


###################################################################################################
#View for all users filter form
##################################################################################################







##################################################################################################
#Participant List Generic View
##################################################################################################

class participantList(generic.ListView):
      template_name = 'pages/participant_list.html'
      filterset_class = ParticipantFilter

      def get_queryset(self):
          return Participant.objects.all().order_by("-pk")

class sessiontList(generic.ListView):
      template_name = 'pages/tables.html'

      def get_queryset(self):
         return Session.objects.all().order_by("-pk")


##################################################################################################
#Charts
##################################################################################################

class sessionChart(TemplateView):
    template_name = 'pages/charts.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["qs"] = Session.objects.all()
        return context

    


##################################################################################################
#PDF View
##################################################################################################


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
	"company": "Dennnis Ivanov Company",
	"address": "123 Street name",
	"city": "Vancouver",
	"state": "WA",
	"zipcode": "98663",


	"phone": "555-555-2345",
	"email": "youremail@dennisivy.com",
	"website": "dennisivy.com",
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
		filename = "Invoice_%s.pdf" %("12341231")
		content = "attachment; filename=%s" %(filename)
		response['Content-Disposition'] = content
		return response



def pdf(request):
	context = {}
	return render(request, 'pages/pdf.html', context)

#Filter-003


    









    
