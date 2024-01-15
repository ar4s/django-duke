from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from duke import get_urls

urlpatterns = [
    path("", TemplateView.as_view(template_name="index.html"), name="index"),
    *get_urls(),
    path("admin/", admin.site.urls),
]
