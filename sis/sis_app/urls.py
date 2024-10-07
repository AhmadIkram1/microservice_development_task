from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name="home"),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    #path('protected/', views.ProtectedView.as_view(), name='protected'),
    
    path('studentcreate/', views.student_create_view, name='student_create'),
    path('studentlist/', views.student_read_view, name='student_list'),
    path('studentupdate/<int:id>/', views.student_update_view, name='student_update'),
    path('studentdelete/<int:id>/', views.student_delete_view, name='student_delete'),
    
    path('coursecreate/', views.course_create_view, name='course_create'),
    path('courselist/', views.course_read_view, name='course_list'),
    path('courseupdate/<int:id>/', views.course_update_view, name='course_update'),
    path('coursedelete/<int:id>/', views.course_delete_view, name='course_delete'),
    
    path('enrollmentcreate/', views.enrollment_create_view, name='enrollment_create'),
    path('enrollmentlist/', views.enrollment_read_view, name='enrollment_list'),
    path('enrollmentupdate/<int:id>/', views.enrollment_update_view, name='enrollment_update'),
    path('enrollmentdelete/<int:id>/', views.enrollment_delete_view, name='enrollment_delete'),
    
    path('schedulecreate/', views.schedule_create_view, name='schedule_create'),
    path('schedulelist/', views.schedule_read_view, name='schedule_list'),
    path('scheduleupdate/<int:id>/', views.schedule_update_view, name='schedule_update'),
    path('scheduledelete/<int:id>/', views.schedule_delete_view, name='schedule_delete'),
    
    path('getenrollments/', views.get_enrolled_students, name='enrolled_students'),
]  