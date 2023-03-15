from django.urls import path
from django.views.i18n import set_language

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('set-language/<str:lang_code>/', set_language, name='set_language'),
]