from django.shortcuts import render

# Create your views here.


from django.contrib.auth.models import User

from rest_framework import authentication,permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import RetrieveUpdateDestroyAPIView,ListCreateAPIView

from course_management.serializers import UserSerializer,CourseSerializer

from course_management.models import Course

from rest_framework.pagination import PageNumberPagination

class SignUpView(APIView):

    def post(self,request):
        form_data = request.data
        serializer_instance = UserSerializer(data=form_data)

        if serializer_instance.is_valid():
             cleaned_data = serializer_instance.validated_data
             instance = User.objects.create_superuser(**cleaned_data)

             serializer_instance = UserSerializer(instance)
             return Response(data=serializer_instance.data)
        else:
            return Response(data=serializer_instance.errors)


# class CourseCreateListView(ListCreateAPIView):
#     authentication_classes = [authentication.BasicAuthentication]
#     permission_classes = [permissions.IsAuthenticated]

#     queryset = Course.objects.all()

#     serializer_class = CourseSerializer

    #==============================

    # def get(self,request):

    #     courses = Course.objects.all()
    #     serializer_instance = CourseSerializer(courses,many=True)
    #     return Response(data=serializer_instance.data)

 


    # def post(self,request):
    #     form_data = request.data
    #     serializer_instance = CourseSerializer(data=form_data)

    #     if serializer_instance.is_valid():
    #         cleaned_data = serializer_instance.validated_data

    #         serializer_instance.save()

    #         return Response(data=serializer_instance.data)
    #     else:
    #         return Response(data=serializer_instance.errors)

    


# class CourseRetriveUpdateDestroyView(RetrieveUpdateDestroyAPIView):

#     queryset = Course.objects.all()

#     serializer_class = CourseSerializer

#     authentication_classes = [authentication.BasicAuthentication]
#     permission_classes = [permissions.IsAuthenticated]


# =========================================================================
#                       VeiwSet
# =========================================================================


from rest_framework.viewsets import ModelViewSet

from course_management.pagenation import CustomPagenation,CustomLimitOffsetPagenation

class CourseModelViewSetView(ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    pagination_class = CustomLimitOffsetPagenation

    def get_queryset(self):

        qs = Course.objects.all()

        query_parameter = self.request.query_params


        if "language" in query_parameter:

            language = query_parameter.get("language")

            qs = qs.filter(language__iexact=language)

        return qs
    
    


