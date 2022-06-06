from pickle import TRUE
from tkinter import FALSE
from django.db import models

# Create your models here.

class Track(models.Model):
    def __str__(self):
        return self.title
    
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Student(models.Model):
    def __str__(self):
        return self.first_name + " " + self.last_name
    
    first_name = models.CharField(max_length=255, default ="John")
    last_name = models.CharField(max_length=255, default="Doe")
    age = models.IntegerField(default = 30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    student_track = models.ForeignKey(Track, on_delete= models.CASCADE)
    
    def is_adult(self):
        if self.age > 20:
            return True
        return False
    is_adult.short_description = "Graduated Student"
    is_adult.boolean = True