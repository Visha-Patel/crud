from django.urls import path
from . import views

urlpatterns = [
        path("",views.ins,name="insert"),
        path("display/",views.dis,name="display"),
        path("inserted/",views.insert,name="inserted"),
        path("delete/<int:id>",views.dele,name='dele'),
        path("update/<int:id>",views.update,name='update'),
]