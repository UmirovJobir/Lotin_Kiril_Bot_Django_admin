from django.contrib import admin
from import_export.admin import ImportExportActionModelAdmin
from django.contrib.auth.models import Group#, User
from .models import Dictionary, Users

admin.site.unregister(Group)

@admin.register(Users, Dictionary)
class Admin(ImportExportActionModelAdmin):
    pass