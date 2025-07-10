from django.urls import path
from . import views

app_name = 'portal'

urlpatterns = [
    # صفحات عامة
    path('', views.index_view, name='index'),
    path('archef/', views.archef_view, name='archef'),
    path('contact/', views.contact_view, name='contact'),
    path('roles/', views.roles_view, name='roles'),
    path('team-university/', views.team_university_view, name='team_university'),

    # المصادقة
    path('register/', views.register_researcher_view, name='register_researcher'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    # لوحة تحكم الباحث
    path('researcher/dashboard/', views.researcher_dashboard_view, name='researcher_dashboard'),
    path('researcher/submit/', views.submit_research_view, name='submit_research'),

    # لوحة تحكم مسؤول الموافقة
    path('approver/dashboard/', views.approver_dashboard_view, name='approver_dashboard'),
    path('approver/approve-user/<int:user_id>/', views.approve_user_view, name='approve_user'),
    path('approver/reject-user/<int:user_id>/', views.reject_user_view, name='reject_user'),
    path('approver/approve-paper/<int:paper_id>/', views.approve_paper_view, name='approve_paper'),
    path('approver/reject-paper/<int:paper_id>/', views.reject_paper_view, name='reject_paper'),
]