from django.urls import path
from . import views
urlpatterns = [
    path("hello/",views.hello),
    # path("hi/",views.hi),
    path('create/',views.create_student)
]