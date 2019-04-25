from django.conf.urls import url
from django.contrib.auth.views import LoginView, LogoutView
from . import views


urlpatterns = [
    url(r'^register/success$', views.register_success, name='login_register_success'),
    url(r'^register$', views.register, name='login_register'),
    url(r'^login/$', LoginView.as_view(extra_context={'name': 'Login'}), name='login'),
    url(r'^logout/$', LogoutView.as_view(extra_context={'name': 'Logout'}), name='logout'),

]