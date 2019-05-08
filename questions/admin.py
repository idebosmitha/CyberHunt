from django.contrib import admin

from .models import *

admin.site.register(Question)
admin.site.register(File)
admin.site.register(Image)
admin.site.register(Submission)
