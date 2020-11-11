from django.contrib import admin

from .models import Admin, Officer, Case,Criminal_Record,Suspect

admin.site.register(Admin)
admin.site.register(Officer)
admin.site.register(Case)
admin.site.register(Suspect)
admin.site.register(Criminal_Record)