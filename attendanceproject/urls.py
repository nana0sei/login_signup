"""attendanceproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from attendanceapp import views
from attendanceapp import hodView
from attendanceapp import staffViews
from attendanceapp import studentViews
from attendanceproject import settings

urlpatterns = [
    path('demo/', views.showDemoPage),
    path('admin/', admin.site.urls),
    path('',views.showLoginPage, name="show_login"),
    path('get_user_details', views.GetUserDetails),
    path('logoutUser', views.LogoutUser, name="logout"),
    path('doLogin', views.doLogin, name="doLogin"),
    path('admin_home', hodView.admin_home, name="admin_home"),
    path('add_staff', hodView.add_staff, name="add_staff"),
    path('add_staff_save', hodView.add_staff_save, name="add_staff_save"),
    path('add_course', hodView.add_course, name="add_course"),
    path('add_course_save', hodView.add_course_save, name="add_course_save"),
    path('add_student', hodView.add_student, name="add_student"),
    path('add_student_save', hodView.add_student_save, name="add_student_save"),
    path('manage_staff', hodView.manage_staff, name="manage_staff"),
    path('manage_student', hodView.manage_student, name="manage_student"),
    path('manage_course', hodView.manage_course, name="manage_course"),
    path('edit_staff/<str:staff_id>', hodView.edit_staff, name="edit_staff"),
    path('edit_staff_save', hodView.edit_staff_save, name="edit_staff_save"),
    path('edit_student/<str:student_id>', hodView.edit_student, name="edit_student"),
    path('edit_student_save', hodView.edit_student_save, name="edit_student"),
    path('manage_session', hodView.manage_session, name="manage_session"),
    path('manage_session_save', hodView.manage_session_save, name="manage_session_save"),


    # Staff URL paths
    path('staff_home', staffViews.staff_home, name="staff_home"),
    path('staff_take_attendance', staffViews.staff_take_attendance, name="staff_take_attendance"),
    path('get_students', staffViews.get_students, name="get_students"),


    path('student_home', studentViews.student_home, name="student_home"),






]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
