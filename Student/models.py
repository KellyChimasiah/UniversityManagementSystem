from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

# CustomUser Model
class CustomUser(AbstractUser):
    user_type = models.CharField(
        max_length=10, 
        choices=[('student', 'Student'), ('lecturer', 'Lecturer')], 
        default='student'
    )
    
    # Define a custom related_name to avoid the conflict
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name='user permissions',
        related_name='customuser_set',  # Change 'customuser_set' to avoid the conflict
        blank=True
    )
    
    groups = models.ManyToManyField(
        Group,
        verbose_name='groups',
        related_name='customuser_set',  # Change 'customuser_set' if needed
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
    )

# Lecturer Model
class Lecturer(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='lecturer')
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)  # Ensure uniqueness of email
    
    # Additional fields, if needed
    department = models.CharField(max_length=100, blank=True, null=True)  # Optional
    office_number = models.CharField(max_length=50, blank=True, null=True)  # Optional
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'

# Course Model
class Course(models.Model):
    course_name = models.CharField(max_length=100)
    course_code = models.CharField(max_length=10, unique=True)  # Added unique course code
    description = models.TextField(blank=True, null=True)  # Optional description for the course
    lecturer = models.ForeignKey(Lecturer, on_delete=models.SET_NULL, related_name='courses', null=True, blank=True)
    
    def __str__(self):
        return self.course_name

# Student Model
class Student(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='student')
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)  # Ensure uniqueness of email
    phone_number = models.CharField(max_length=15)  # Allow for different formats (including international)
    date_of_birth = models.DateField()
    
    # Relationship with courses (One-to-many relationship; a student can be enrolled in one or more courses)
    courses = models.ManyToManyField(Course, related_name='students', blank=True)
    
    # Optional fields for student profile
    profile_picture = models.ImageField(upload_to='students/', blank=True, null=True)
    address = models.TextField(blank=True, null=True)  # Optional address field
    enrollment_date = models.DateField(auto_now_add=True)  # Automatically set the date when the student is created
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'
