from django.contrib import admin
from .models import Student, Track

# Register your models here.

class CustomStudent(admin.ModelAdmin):
    fieldsets = (
        ['Student Information', {'fields' : ['first_name', 'last_name', 'age']}],
        ['Tracks', {'fields' : ['student_track']}]
    )
    
    list_display = ('first_name', 'last_name', 'age', 'student_track', 'is_adult')

class InlineStudent(admin.StackedInline):
    model = Student
    extra = 1

class CustomTrack(admin.ModelAdmin):
    inlines = [InlineStudent]

admin.site.register(Student, CustomStudent)
admin.site.register(Track, CustomTrack)