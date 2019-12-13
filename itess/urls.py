from django.urls import path
from . import views
app_name = "itess"

urlpatterns = [
    path('informations/',views.get_infos, name = "informations"),
    
]