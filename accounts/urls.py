from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
    path('login',views.login),
    path('register',views.register),
    path('logout/',views.logout),
    path('verifyEmail/<str:id>',views.verifyEmail)
]