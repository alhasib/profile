from django.conf.urls import url
from django.contrib.auth import views as auth_views
from .views import signup
#from registration.registrationapp import views as registrationapp_views

urlpatterns = [
    url(r'^login/', auth_views.login,name = 'login'),
    url(r'^logout/', auth_views.logout,name = 'logout'),
    url(r'^signup/$', signup,name = 'signup'),

]
