from django.urls import path
from . import views

urlpatterns = [
    path('', views.Blog_List_View.as_view(), name='home'),
    path('post/<int:pk>/', views.Blog_Detail_View.as_view(), name='post_detail'),
    path('post/new/', views.Blog_Create_View.as_view(), name='post_new'),
    path('post/<int:pk>/edit/', views.Blog_Update_View.as_view(), name='post_edit'),
    path('post/<int:pk>/delete/', views.Blog_Delete_View.as_view(), name='post_delete'),

]
