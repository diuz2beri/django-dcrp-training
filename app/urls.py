# -*- encoding: utf-8 -*-
"""
License: MIT

"""

from django.urls import path, re_path
from app import views
from django.conf.urls import url
from django.urls import path, include
from . import views
from .views import get_data
from app.views import sessionChart
from django_filters.views import FilterView
from app.filters import sessionFilter
from app.filters import ParticipantFilter

# These are the SAML2 related URLs. You can change "^saml2_auth/" regex to
# any path you want, like "^sso_auth/", "^sso_login/", etc. (required)
# url(r'^saml2_auth/', include('django_saml2_auth.urls')),

# The following line will replace the default user login with SAML2 (optional)
# If you want to specific the after-login-redirect-URL, use parameter "?next=/the/path/you/want"
# with this view.
# url(r'^accounts/login/$', django_saml2_auth.views.signin),

# The following line will replace the admin login with SAML2 (optional)
# If you want to specific the after-login-redirect-URL, use parameter "?next=/the/path/you/want"
# with this view.
# url(r'^admin/login/$', django_saml2_auth.views.signin),

urlpatterns = [
    # Matches any html file - to be used for gentella
    # Avoid using your .html in your resources.
    # Or create a separate django app.
    re_path(r'^.*\.html', views.pages, name='pages'),
    # The home page
    path('', views.index, name='home'),
    path('participant/<str:pk>', views.participant, name='participant'),
    path('session/<str:pk>', views.sessionView, name='session'),
    path('create_participant', views.createParticipant, name='create_participant'),
    path('create_session', views.createSession, name='create_session'),

    path('pdf/', views.pdf, name="pdf"),
    path('pdf_view/', views.ViewPDF.as_view(), name="pdf_view"),
    path('pdf_download/', views.DownloadPDF.as_view(), name="pdf_download"),
    path('session_search/', views.sessiontList.as_view(), name='searchView'),
    path('participant_all/', views.participantList.as_view(), name='participant_list'),
    path('charts/', views.sessionChart.as_view(), name='chart'),
    url(r'^api/data/$', get_data, name='get_data'),
    url(r'^search/$', FilterView.as_view(filterset_class=ParticipantFilter, template_name='pages/search.html'),
        name='search'),
    url(r'^search_sess/$', FilterView.as_view(filterset_class=sessionFilter, template_name='pages/search-ses.html'),
        name='search_sess'),

    ############
    # PDF urls #
    ############

    path('pdf_ses_view/', views.GenerateSesPdf.as_view(), name="pdf_ses_view"),

    path('render/pdf/', views.gen_pdf, name='pdf_download'),
    path('ses_list/<str:pk>', views.gen_pdf_partList, name='ses_list'),
    path('render/pdf/print', views.export_search_pdf, name='search-pdf'),
    re_path(r'^export/csv/$', views.export_csv, name='export_csv'),
    re_path(r'session_pdf/$', views.DownloadSesPDF.as_view(), name="ses_download"),
    re_path(r'^export/part/$', views.export_part_csv, name='export_part_csv'),
    re_path(r'participant_pdf/$', views.DownloadPartPDF.as_view(), name="part_download"),
    url(r'pdf_ses_down/(?P<id>\d+)/$', views.ViewPDFSesion.as_view(), name="pdf_ses_down"),

]

# url(r'^admin/login/$', django_saml2_auth.views.signin) path('pdf_list/', views.SesListPDF.as_view(), name="pdf_list"),
