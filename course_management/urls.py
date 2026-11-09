

from django.urls import path

from course_management.views import SignUpView
# from course_management.views import CourseCreateListView,CourseRetriveUpdateDestroyView

from course_management.views import CourseModelViewSetView

from rest_framework.routers import DefaultRouter    # restframework have already defined routers for the viewset


router = DefaultRouter()
router.register("course_viewset",CourseModelViewSetView)


print(router.urls)

urlpatterns = [
                path("admin/register/",SignUpView.as_view()),             # to register new admin user

                # path("courses/",CourseCreateListView.as_view()),          # to create and list course

                # path("<int:pk>/courses/",CourseRetriveUpdateDestroyView.as_view()),  # to retrive , update , delete   courses 



                


] + router.urls        # to list, retrive, create, update, destroy    using VIEWSET