from django.urls import path

from blog import views

urlpatterns = [
    path('<int:blog_pk>', views.blog_detail, name ="blog_detail"),
]
