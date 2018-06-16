from django.urls import path

from .views import school_list, school_detail, student_list, student_detail

urlpatterns = [
    path(r'schools/', school_list, name= 'school-list'),
    path(r'schools/<int:school_id>', school_detail, name = 'school-detail' ),
    path(r'student/', student_list, name = 'student-list'),
    path(r'student/<int:student_id>', student_detail, name = 'student-detail'),
]
