# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin

# Register your models here.

from admin_auto_filters.filters import AutocompleteFilter

# Register your models here.

from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
#from import_export.admin import resources, ImportExportModelAdmin
from .models import Course, Participant,  Session, Project, Organization, Program, Unit, ListOfParticpantsWhoCompletedCourse
#admin.site.register(Course)

class SessionFilter(AutocompleteFilter):
    title = 'Session'
    
class UnitAdmin(admin.ModelAdmin):
    list_display = ('course', 'unit_id', 'unit_name')
    list_filter = ('unit_name', 'unit_id', 'course' )
    search_fields = ['unit_name']
    view_on_site = False

admin.site.register(Unit, UnitAdmin)
class CoursecompletedInline(admin.TabularInline):
    model = ListOfParticpantsWhoCompletedCourse.participant_list.through

class CompletedCourseAdmin(admin.ModelAdmin):
    list_display = ['course', 'unit_name']
    search_fields = ['course']
    list_filter = ['course', 'unit_name', 'sessions', 'participant_list']
    filter_horizontal = ['participant_list']
    view_on_site = False
    
admin.site.register(ListOfParticpantsWhoCompletedCourse, CompletedCourseAdmin)
class CourseAdmin(ImportExportModelAdmin):
    list_display = ('course_title', 'program', 'project', 'accredited')
    list_filter = ('course_title', 'program', 'project', 'accredited')
    view_on_site = False
admin.site.register(Course,CourseAdmin)


#admin.site.register(Participants)
class SessionInline(admin.TabularInline):
    model = Session.participant.through
class ParticipantInline(admin.TabularInline):
    model = Participant.organization.through
class Listcourseinline(admin.TabularInline):
    model = ListOfParticpantsWhoCompletedCourse.participant_list.through
class ParticipantAdmin(ImportExportModelAdmin):
    list_display = ('first_name', 'last_Name', 'gender', 'date_of_birth', 'get_organization', 'country')
    list_filter = ('gender',  'education_level', 'trainer', 'organization')
    filter_horizontal = ['organization']
    search_fields = ['first_name']
    inlines = [SessionInline, Listcourseinline]
    view_on_site = False

    #def session_display(self, obj):
     #   return ", ".join([
      #      Session.name_of_activity for Session in obj.Session.all()
       # ])
    #session_display.short_description = "Session"
    #save_as = True
    #save_on_top = True
    #change_list_template = 'change_list_graph.html'
    #search_fields = (
     #   ('f','first_name'),
    #    ('l', 'last_name')
   # )
admin.site.register(Participant, ParticipantAdmin)
#admin.site.register(Program)
#admin.site.register(Session)
#class SessionResource(resources.ModelResource):

 #   class Meta:
  #      model = Session
class SessionAdmin(ImportExportModelAdmin):
    list_display = ('name_of_activity','day_number', 'course', 'attendees_number', 'method', 'period', 'session_type')
    list_filter = ('name_of_activity', 'course', 'attendees_number', 'method', 'period', 'session_type')
    filter_horizontal = ['participant']
    search_fields = ['name_of_activity']
    view_on_site = False
    #save_as = True
    #save_on_top = True
    #change_list_template = 'change_list_graph.html'
    #resource_class =
admin.site.register(Session, SessionAdmin)
#admin.site.register(Project)
class ProjectAdmin(ImportExportModelAdmin):
    list_display = ('program', 'project_name')
    list_filter = ('program', 'project_name')
    search_fields = ['project_name']
    view_on_site = False

admin.site.register(Project, ProjectAdmin)
# Register your models here.

class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('organization', 'sector','special_general', 'special_disaster_management')
    list_filter = ('organization', 'sector', 'special_general', 'special_disaster_management')
    view_on_site = False
    inlines = [ParticipantInline]
    

admin.site.register(Organization, OrganizationAdmin)


class ProgramAdmin(admin.ModelAdmin):
    pass


admin.site.register(Program, ProgramAdmin)



