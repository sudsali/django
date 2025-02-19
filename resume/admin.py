from django.contrib import admin

# Register your models here.
from .models import Header,Education, Experience, TechnicalSkill, Project

admin.site.register(Header)
admin.site.register(Education)
admin.site.register(TechnicalSkill)
admin.site.register(Experience)
admin.site.register(Project)
