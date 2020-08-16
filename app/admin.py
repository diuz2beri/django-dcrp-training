# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) SPC
"""

#admin.site.register(Course)
#from import_export.admin import resources, ImportExportModelAdmin
from admin_auto_filters.filters import AutocompleteFilter
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Course, Participant,  Session, Project, Organization, Program, Unit, ListOfParticpantsWhoCompletedCourse

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


admin.site.register(Participant, ParticipantAdmin)

class SessionAdmin(ImportExportModelAdmin):
    list_display = ('name_of_activity','day_number', 'course', 'attendees_number', 'method', 'period', 'session_type')
    list_filter = ('name_of_activity', 'course', 'attendees_number', 'method', 'period', 'session_type', 'project')
    filter_horizontal = ['participant']
    search_fields = ['name_of_activity']
    filter_horizontal = ['course_units']
    filter_horizontal = ['trainer']
    exclude = ('Course_unit_names',)
    view_on_site = True

admin.site.register(Session, SessionAdmin)

class ProjectAdmin(ImportExportModelAdmin):
    list_display = ('program', 'project_name')
    list_filter = ('program', 'project_name')
    search_fields = ['project_name']
    view_on_site = False

admin.site.register(Project, ProjectAdmin)


class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('organization', 'sector','special_general', 'special_disaster_management')
    list_filter = ('organization', 'sector', 'special_general', 'special_disaster_management')
    view_on_site = False
    inlines = [ParticipantInline]
    
admin.site.register(Organization, OrganizationAdmin)

class ProgramAdmin(admin.ModelAdmin):
    pass

admin.site.register(Program, ProgramAdmin)



from .models import Trainer

class TrainerAdmin(ImportExportModelAdmin):
    list_display = ('first_name', 'last_Name', 'country', 'position')
    list_filter = ('first_name', 'last_Name', 'country', 'position')
    search_fields = ['first_name', 'lastname','country']

admin.site.register(Trainer, TrainerAdmin)

from .models import Assesors

class AssesorAdmin(ImportExportModelAdmin):
    list_display = ('title', 'first_name', 'last_Name', 'country', 'position')

admin.site.register(Assesors, AssesorAdmin)

