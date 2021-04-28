from django.urls import path
from django.conf.urls import url
from dypasswordApp import views
urlpatterns = [
url(r'^$',views.input),
url(r'^comp$',views.compute)
]
