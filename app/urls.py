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

# These are the SAML2 related URLs. You can change "^saml2_auth/" regex to
# any path you want, like "^sso_auth/", "^sso_login/", etc. (required)
#url(r'^saml2_auth/', include('django_saml2_auth.urls')),

# The following line will replace the default user login with SAML2 (optional)
# If you want to specific the after-login-redirect-URL, use parameter "?next=/the/path/you/want"
# with this view.
#url(r'^accounts/login/$', django_saml2_auth.views.signin),

# The following line will replace the admin login with SAML2 (optional)
# If you want to specific the after-login-redirect-URL, use parameter "?next=/the/path/you/want"
# with this view.
#url(r'^admin/login/$', django_saml2_auth.views.signin),

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
    
    path('pdf/', views.pdf,name="pdf"),
    path('pdf_view/', views.ViewPDF.as_view(), name="pdf_view"),
    path('pdf_download/', views.DownloadPDF.as_view(), name="pdf_download"),
    path('session_search/', views.sessiontList.as_view(), name='searchView'),
    path('participant_all/', views.participantList.as_view(), name='participant_list'),
    url(r'^api/data/$', get_data, name='get_data'),
   ]
    
    #url(r'^admin/login/$', django_saml2_auth.views.signin)

