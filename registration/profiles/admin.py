from django.contrib import admin

# Register your models here.
from .models import Division,District,Area,Profile
admin.site.register(Division)
admin.site.register(District)
admin.site.register(Area)
admin.site.register(Profile)
