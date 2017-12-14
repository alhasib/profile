from django.conf.urls import url
from .views import profile,createprofile

urlpatterns = [
    url(r'^myprofile/', profile,name='profile'),
    url(r'^create/', createprofile,name='createprofile'),
]
