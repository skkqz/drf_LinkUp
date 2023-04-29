from django.contrib import admin
from .models import Organizations


@admin.register(Organizations)
class OrganizationsAdmin(admin.ModelAdmin):

    list_display = ['name']

