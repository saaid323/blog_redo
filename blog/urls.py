from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path("post/create/", views.post_create, name='post_create'),
    path('update_post/<int:pk>', views.update_post, name='update_post'),
    path('delete_post/<int:pk>', views.delete_post, name='delete_post'),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name='logout'),
    path("signup/", views.signup, name='signup'),
    path("comments/<int:pk>", views.create_comment, name="create_comment"),
    path("delete_comment/<int:pk>", views.delete_comment, name='delete_comment'),
    path('history', views.user_history, name='history'),
    path('delete_read_history/<str:pk>', views.delete_read_history, name='delete_read_history'),
    path("can_comment/", views.can_comment, name='can_comment'),
    path("user-profile/", views.Author_profile, name="author_profile"),
    path("update_user", views.updateUser, name="update-user"),
]
