"""onlineclass URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from app1 import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('adminl/', views.admin_login, name='admin_login'),
    path('admin_login_check/', views.admin_login_check, name='admin_login_check'),
    path('shedule_new_cls/', views.shedule_new_cls, name='shedule_new_cls'),
    path('class_added/', views.class_added, name='class_added'),
    path('view_shedule/', views.view_shedule, name='view_shedule'),
    path('showupdate/', views.showupdate, name='showupdate'),
    path('update_cls/', views.update_cls, name='update_cls'),
    path('delete/', views.delete, name='delete'),


    path('',views.Showmain,name='main'),
    path('stu_reg/',views.stu_reg,name='stu_reg'),
    path('stu_registerd/',views.stu_registerd,name='stu_registerd'),
    path('stu_login/',views.stu_login,name='stu_login'),
    path('stu_login_check/',views.stu_login_check,name='stu_login_check'),

    path('enrol_course/',views.enrol_course,name='enrol_course'),
    path('enroled_course/',views.enroled_course,name='enroled_course'),
    path('view_enrol_courses/',views.view_enrol_courses,name='view_enrol_courses'),
    path('cancel_enrol_course/',views.cancel_enrol_course,name='cancel_enrol_course'),
    path('course_canceled/',views.course_canceled,name='course_canceled')
]
