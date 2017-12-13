from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views


from gooseurl import views


app_name = "gooseurl"

urlpatterns = [
    url(r'^goose_url_data_fetch/$', views.goose_url_data_fetch.as_view(), name='goose_url_data_fetch'),
]