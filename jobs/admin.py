from django.contrib import admin
from jobs.models import Tag, Job

# Register your models here.

class JobAdmin(admin.ModelAdmin):
    list_display = ('name', 'place', 'mission', 'date', 'email', 'get_tags')

admin.site.register(Tag)
admin.site.register(Job, JobAdmin)