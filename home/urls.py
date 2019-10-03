from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.log_in, name = 'login'),
    path('signup', views.signup, name='signup'),
    path('selfstudy', views.selfstudy, name='selfstudy'),
    path('faq', views.faq, name='faq'),
    path('linux_certification', views.linux_certification, name='linux_certification'),
    path('workexperience', views.workexperience, name='workexperience'),
    path('jobplacements', views.jobplacements, name='jobplacements'),
    path('apply', views.apply, name='apply'),
    path('apply_jnr', views.apply_jnr, name='apply_jnr'),
    path('qualify', views.qualify, name='qualify'),
    path('required2', views.required2, name='required2'),
    path('qualify2', views.qualify2, name='qualify2'),
    path('required', views.required, name='required'),
    path('pay', views.pay, name='pay'),
    path('accepted', views.accepted, name='accepted'),
    path('group', views.group, name='group'),
    path('logout', views.log_out, name="logout")
]