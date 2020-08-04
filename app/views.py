# -*- encoding: utf-8 -*-
"""
License: MIT

"""
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
# from django_filters.views import FilterView
# from io import BytesIO
# from django.template.loader import get_template
# from django.views import View
# from xhtml2pdf import pisa
# import pandas as pd
# import itertools, operator
# import django_saml2_auth.views
# from django.db.models import Count, Sum
from django.http import JsonResponse
from django.shortcuts import redirect
from django.shortcuts import render
from django.template import loader
from django.views import View
from django.views import generic
from django.views.generic import TemplateView
from app.utils import render_to_pdf
from .filters import ParticipantFilter, sessionFilter
from .forms import ParticipantForm
from .forms import SessionForm
from .models import *
import csv
import datetime


############################################################################################
# Homepage View
############################################################################################

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

    # country_count = Participant.objects.values('country').annotate(total_user = attendees_number )

    context = {"session": session, "participants": participants, "total_participant": total_participant,
               "total_courses": total_courses, "total_session": total_session, "total_course_comp": total_course_comp, }
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

        template = loader.get_template('pages/error-404.html')
        return HttpResponse(template.render(context, request))


############################################################################################
# Participant View to edit on template./ create session / create participant
############################################################################################

def participant(request, pk):
    part_data = Participant.objects.get(id=pk)
    list_part = Session.objects.filter(participant=pk).count()

    session_data = Session.objects.filter(participant=pk)
    return render(request, 'pages/icons.html',
                  {'session_data': session_data, 'list_part': list_part, 'part_data': part_data})


# Session View to edit on template.
def sessionView(request, pk):
    session_data = Session.objects.get(id=pk)
    sesion = Session.objects.all()
    list_part = 2
    myFilter = sessionFilter(request.GET, queryset=sesion)
    sesion = sessionFilter.qs

    context = {'myFilter': myFilter, 'list_part': list_part, 'session_data': session_data, "sesion": sesion}
    return render(request, 'pages/maps.html', context)


def deleteParticipant(request):
    # delete
    return render(request)


# Results Data
@login_required(login_url="/login/")
def resultData(request):
    sesions = Session.objects.all()
    context = {"sesions": sesions}
    print(sesions)
    return render(request, "pages/index.html", context)


###################################################################################################
# View for all forms
##################################################################################################

def createSession(request):
    form = SessionForm
    if request.method == 'POST':
        print('Printing POST:', request.POST)
        form = SessionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {"form": form}

    return render(request, 'pages/session.html', context)


# participant form

def createParticipant(request):
    formNew = ParticipantForm
    if request.method == 'POST':
        print('Printing POST:', request.POST)
        formNew = ParticipantForm(request.POST)
        if formNew.is_valid():
            formNew.save()
            return redirect('/')

    context = {"formNew": formNew}

    return render(request, 'pages/participant_form.html', context)


###################################################################################################
# View for all users filter form
##################################################################################################
def search_part(request):
    user_list = Participant.objects.all()
    user_filter = ParticipantFilter(request.GET, queryset=user_list)
    return render(request, 'pages/search.html', {'filter': user_filter})



def export_part_csv(request):
    participant = Participant.objects.all()
    participants = ParticipantFilter(request.GET, queryset=participant)

    responce = HttpResponse(content_type='text/csv')
    responce['Content-Disposition'] = 'attachment; filename=session search' + str(datetime.datetime.now()) + '.csv'
    writer = csv.writer(responce)
    writer.writerow(['Name', 'Email', 'Position',  'County', 'Gender'])

    for item in participants.qs:
        writer.writerow([item.first_name + item.last_Name, item.email, item.position, item.country.name, item.gender])
    return responce

# Automaticly downloads to PDF file
class DownloadPartPDF(View):

    def get(self, request, *args, **kwargs):

        participant = Participant.objects.all()
        participants = ParticipantFilter(request.GET, queryset=participant)
        context = {'filter': participants}
        pdf = render_to_pdf('pages/pdf_part_list.html', context)
        response = HttpResponse(pdf, content_type='application/pdf')
        filename = "Participant_%s.pdf" % ("12341231")
        content = "attachment; filename=%s" % (filename)
        response['Content-Disposition'] = content
        return response

##################################################
# session data filter | export csv | export pdf #
#################################################
def search_sess(request):
    sess_filter_search = sessionFilter(request)
    context = {'filter': sess_filter_search}
    return render(request, 'pages/search-ses.html', context)


def export_search_pdf(request):
    sess_filter = sess_filter_search
    context = {'filter': sess_filter}
    result = render_to_pdf('pages/pdf_ses_print.html', context)
    return result


def export_csv(request):
    session_old = Session.objects.all()
    sessions = sessionFilter(request.GET, queryset=session_old)

    responce = HttpResponse(content_type='text/csv')
    responce['Content-Disposition'] = 'attachment; filename=session search' + str(datetime.datetime.now()) + '.csv'
    writer = csv.writer(responce)
    writer.writerow(['Activity name', 'Session type', 'Method', 'Project', 'Country', 'Total Participants'])

    for item in sessions.qs:
        writer.writerow([item.name_of_activity, item.session_type, item.method, item.project, item.country.name, item.attendees_number])
    return responce

# Automaticly downloads to PDF file
class DownloadSesPDF(View):


    def get(self, request, *args, **kwargs):

        session_old = Session.objects.all()
        sessions_q = sessionFilter(request.GET, queryset=session_old)
        context = {'filter': sessions_q}
        pdf = render_to_pdf('pages/pdf_ses_print.html', context)
        response = HttpResponse(pdf, content_type='application/pdf')
        filename = "Session_%s.pdf" % ("12341231")
        content = "attachment; filename=%s" % (filename)
        response['Content-Disposition'] = content
        return response


##################################################################################################
# class Test(ButtonAdmin):
#     buttons = (
#         Button('test', "A Test Button"),
#         Button('redirect', "A redirect"),
#     )
#
#     def tool_test(self, request, obj, button):
#         session_list = Session.objects.all()
#         sess_filter = sessionFilter(request.GET, queryset=session_list).qs
#         context = {'filter': sess_filter, 'report_id': report_id}
#
#         return 'pages/search-ses.html', { context, "message" : "a test"}
#
#     def tool_redirect(self, request, obj, button):
#         context = sess_filter
#         result = render_to_pdf('pages/pdf_ses_print.html', context)
#
#         return HttpResponseRedirect('/render/pdf ')
#
#
#
#
#
#
# Participant List Generic View
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
#  Charts
##################################################################################################

class sessionChart(TemplateView):
    template_name = 'pages/charts.html'

    def get_queryset(self):
        query = Session.objects.all("q")
        return sessionFilter(query)

    def get_context_data(self):
        context = super(sessionFilter, self).get_context_data
        context['query'] = self.request.GET.get("q")
        return context


####################################################################################################
#   PDF View
####################################################################################################


def gen_pdf(request):
    # resp = HttpResponse(pdf, content_type='application/pdf')
    session = Session.objects.all().order_by("-pk")
    total_session = session.count()
    context = {'session': session, 'total_session': total_session}
    result = render_to_pdf('pages/pdf_ses_temp.html', context)
    return result


def gen_pdf_partList(request, pk):
    session_data = Session.objects.get(id=pk)
    session = Session.objects.all().order_by('pk')
    part_list = session.objects.prefetch_related('participant')
    total_participant = part_list.count()
    context = {'session_data': session_data, 'part_list': part_list, 'total_participant': total_participant}
    participants = render_to_pdf('pages/pdf_ses_list.html', context)
    return participants


def gen_ses_pdf(request, pk):
    session_data = sessiontList(generic.ListView)
    session = Session.objects.all().order_by('pk')
    part_list = session.objects.prefetch_related('participant')
    total_participant = part_list.count()
    context = {'session_data': session_data, 'part_list': part_list, 'total_participant': total_participant}
    participants = render_to_pdf('pages/pdf_ses_list.html', context)
    return participants


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


# Opens up page as PDF
class ViewPDF(View):

    def get(self, request, *args, **kwargs):
        pdf = render_to_pdf('pages/pdf_template.html', data)
        return HttpResponse(pdf, content_type='application/pdf')


# Automaticly downloads to PDF file
class DownloadPDF(View):
    def get(self, request, *args, **kwargs):
        pdf = render_to_pdf('pages/pdf_template.html', data)
        response = HttpResponse(pdf, content_type='application/pdf')
        filename = "Invoice_%s.pdf" % ("12341231")
        content = "attachment; filename=%s" % (filename)
        response['Content-Disposition'] = content
        return response


def pdf(request):
    context = {}
    return render(request, 'pages/pdf.html', context)


class GenerateSesPdf(View):
    model = Session
    template_name = 'pages/charts.html'

    @property
    def get_queryset(self):
        query = Session.objects.all('q')
        return sessionFilter(query)

    def get_context_data(self):
        context = super(sessionFilter, self).get_context_data(**kwargs)
        context['query'] = self.request.GET.get("q")
        return context
