from django.contrib import admin
from django.urls import path
from exercicios.views import ListaExercicisView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("exercicios", ListaExercicisView.as_view()),
]
