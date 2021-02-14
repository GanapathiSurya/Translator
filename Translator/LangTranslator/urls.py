from django.urls import path
from LangTranslator import views

urlpatterns=[
  path('',views.index,name="index"),
  path('filetranslate/',views.filetranslate,name="filetranslate")
]