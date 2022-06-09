from . import views
from django.urls import path

urlpatterns = [
    path('home/', views.home, name='home'),
    path('work/', views.work, name='work'),
    path('hello/<st_id>', views.hello, name='hello'),
    path('show/<st_id>', views.show, name='show'),
    path('delete/<st_id>', views.deleteStudent, name="st-del"),
    path('st-add', views.addStudent, name='st-add'),
    path('st-edit<st_id>', views.editStudent, name='st-edit'),
    # REst
    path('api-list', views.api_all_students, name='api-list'),
    path('api-st/<st_id>', views.api_student_details, name='api-st'),
    path('api-add', views.api_student_create, name='api-add'),
    path('api-edit/<st_id>', views.api_student_edit, name='api-edit'),
    path('api-del/<st_id>', views.api_student_delete, name='api-del'),
]
