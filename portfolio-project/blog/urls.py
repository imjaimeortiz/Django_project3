from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_blogs, name='blogs'),
    path('<int:blog_id>/', views.detail, name='detail')
]
