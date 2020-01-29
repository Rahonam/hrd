from django.contrib import admin
from .models import Candidate, Application_Submit, Application_Review, Application_Interview, Application_Hire

admin.site.register(Candidate)
admin.site.register(Application_Submit)
admin.site.register(Application_Review)
admin.site.register(Application_Interview)
admin.site.register(Application_Hire)
