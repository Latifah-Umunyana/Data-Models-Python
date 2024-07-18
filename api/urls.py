
from django.urls import path

from .views import StudentListViews
from .views import ClassListViews
from .views import ClassPeriodListViews
from .views import CoursesListViews
from .views import TeacherListViews


urlpatterns = [
path("students/", StudentListViews.as_view(), name="student_list_view"),
path("classes/", ClassListViews.as_view(), name="class_list_view"),
path("periods/", ClassPeriodListViews.as_view(), name="classPeriod_list_view"),
path("courses/", CoursesListViews.as_view(), name="course_list_view"),
path("teachers/", TeacherListViews.as_view(), name="teacher_list_view")
]

