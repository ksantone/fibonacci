from django.urls import path
from django.urls.conf import include
from . import views

urlpatterns = [
	path('', views.test, name="test"),
	path('mainapp', views.test_views, name="test_views"),
	path('mainapp/other', views.other_view, name="other_view"),
]