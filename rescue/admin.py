from django.contrib import admin
from . models import Telemedicine, Doctor, Resource, Messages


admin.site.register(Telemedicine)
admin.site.register(Doctor)
admin.site.register(Resource)
admin.site.register(Messages)
