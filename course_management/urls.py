

from django.urls import path

from course_management.views import SignUpView
from course_management.views import CourseCreateListView,CourseRetriveUpdateDestroyView


urlpatterns = [
                path("admin/register/",SignUpView.as_view()),             # to register new admin user

                path("courses/",CourseCreateListView.as_view()),          # to create and list course

                path("<int:pk>/courses/",CourseRetriveUpdateDestroyView.as_view())  # to retrive , update , delete   courses 


]