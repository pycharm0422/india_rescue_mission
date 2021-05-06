from django.contrib import admin
from . models import Telemedicine, Doctor, Resource, Messages, MessageBoard


admin.site.register(Telemedicine)
admin.site.register(Doctor)
admin.site.register(Resource)
admin.site.register(Messages)
admin.site.register(MessageBoard)
