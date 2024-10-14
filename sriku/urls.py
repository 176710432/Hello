from django.urls import path
from sriku import views
urlpatterns=[
    path("",views.hello,name="hello")
]