from django.urls import path
from . import views


urlpatterns = [
    # path(<urlpath_in_address_bar>, <views.py_file.FunctionName>, <name = name_mentioned_in_html_page>)

    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('dashboard', views.dashboard, name='dashboard'),
]
