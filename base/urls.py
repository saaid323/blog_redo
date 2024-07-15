from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("create", views.CreateBlog, name="create_blog"),
    path("update/<str:pk>", views.UpdateBlog, name="update_blog"),
    path("delete_blog/<str:pk>", views.deleteBlog, name="delete")
]
