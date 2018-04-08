from django.urls import path
from . import views

urlpatterns = [
    path('', views.Blog_List_View.as_view(), name='home'),
    path('post/<int:pk>/', views.Blog_Detail_View.as_view(), name='post_detail'),

]
