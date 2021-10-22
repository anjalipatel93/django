from block import views
from django.urls import path

urlpatterns = [
    path('<slug:slug>', views.BlockView.as_view(), name = 'block_view'),
    path('about/', views.AboutView.as_view(), name='about_view'),
    path('', views.PostList.as_view(), name ='postlist_view')
]