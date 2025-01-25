from django.contrib import admin
from .models import Lecturer, Course, Student, CustomUser
from django.contrib.auth.admin import UserAdmin

# Customizing the Lecturer model admin
class LecturerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')  # Fields to display in the list view
    search_fields = ('first_name', 'last_name', 'email')  # Make these fields searchable
    list_filter = ('first_name', 'last_name')  # Add filters for first_name and last_name

# Customizing the Course model admin
class CourseAdmin(admin.ModelAdmin):
    list_display = ('course_name', 'lecturer')  # Fields to display in the list view
    search_fields = ('course_name', 'lecturer__first_name')  # Make course_name and lecturer's name searchable
    list_filter = ('lecturer',)  # Add a filter by lecturer

# Customizing the Student model admin
class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', )
    search_fields = ('first_name', 'last_name', 'email')  # Make these fields searchable
    
   

# Customizing the CustomUser model admin
class CustomUserAdmin(UserAdmin):
    # Fields to be displayed in the list view
    list_display = ('username', 'email', 'user_type', 'is_staff', 'is_active')
    
    # Fields to be displayed in the form view
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('user_type',)}),  # Add user_type to the admin form
    )
    
    # Add user_type to the search functionality
    search_fields = ('username', 'email', 'user_type')

    # Optionally, add filters to filter by user_type or other fields
    list_filter = ('user_type', 'is_staff', 'is_active')

# Registering the models with their customized admin
admin.site.register(Lecturer, LecturerAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(CustomUser, CustomUserAdmin)  # Register CustomUserAdmin with CustomUser
