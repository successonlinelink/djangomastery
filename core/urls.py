from django.urls import path
from core import views # we did this way to reduce chunk of imports

app_name = "portfolio"

urlpatterns = [
    path("", views.index, name="index"),
    path("post/<pid>/", views.portfolio_detail, name="portfolio_detail"),
    
    path("service/", views.service, name="service"),
    path("contact/", views.contact, name="contact"),


]