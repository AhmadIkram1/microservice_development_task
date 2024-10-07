from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name="home"),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    
    path('roomcreate/', views.room_create_view, name='room_create'),
    path('roomlist/', views.room_read_view, name='room_list'),
    path('roomupdate/<int:id>/', views.room_update_view, name='room_update'),
    path('roomdelete/<int:id>/', views.room_delete_view, name='room_delete'),
    
    path('enrollmentcreate/', views.enrollment_create_view, name='enrollment_create'),
    path('enrollmentlist/', views.enrollment_read_view, name='enrollment_list'),
    path('enrollmentupdate/<int:id>/', views.enrollment_update_view, name='enrollment_update'),
    path('enrollmentdelete/<int:id>/', views.enrollment_delete_view, name='enrollment_delete'),
    
    path('schedulecreate/', views.schedule_create_view, name='schedule_create'),
    path('schedulelist/', views.schedule_read_view, name='schedule_list'),
    path('scheduleupdate/<int:id>/', views.schedule_update_view, name='schedule_update'),
    path('scheduledelete/<int:id>/', views.schedule_delete_view, name='schedule_delete'),
]