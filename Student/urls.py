from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.login_view, name='login'),  # Login view
    path('signup/', views.signup, name='signup'),  # Signup view
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),  # Built-in logout view
    path('student/dashboard/', views.student_dashboard, name='student_dashboard'),  # Student dashboard view
    path('lecturer/dashboard/', views.lecturer_dashboard, name='lecturer_dashboard'),  # Lecturer dashboard view
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
