
from onlineapp import views
from django.urls import include, path  # For django versions from 2.0 and up
from onlineapp.views import *
from onlineapp.views import logiform, signupform, r_collegeview, r_studentview

urlpatterns = [

    # path('get_colleges/', views.database),
    # path('get_colleges/<int:id>/', views.studentinfo, name="studentinfo")

    path('get_colleges/', class_view.as_view(), name="colleges"),
    path('get_colleges/<str:acronym>/<int:pk>/', class_view.as_view(), name="studentinfo"),

    path("add_college/", AddCollegeView.as_view(), name="addcollege"),

    path("add_college/<str:acronym>/", AddCollegeView.as_view(), name="addinfo"),
    path("add_college/<int:pk>/", AddCollegeView.as_view(), name="addinfo"),

    path("add_college/<int:pk>/edit", AddCollegeView.as_view(), name="editcollege"),
    path("add_college/<int:pk>/delete", AddCollegeView.as_view(), name="deletecollege"),

    path("add_student/<int:id>/edit/", AddStudentView.as_view(), name="editstudent"),
    path("add_student/<int:id>/delete/", AddStudentView.as_view(), name="deletestudent"),

    path("add_student/<int:pk>/", AddStudentView.as_view(), name="addstudentinfo"),

    path("login/", logiform.loginForm_view.as_view(), name="login"),
    path("signup/", signupform.signupForm_view.as_view(), name="signup"),

    path("logout/", college.logout_user, name="logout"),

    path('api/vl/colleges/', r_collegeview.r_collegeview),
    path('api/vl/colleges/<int:id>/', r_collegeview.r_collegeview),
    path('api/vl/students/', r_studentview.r_studentview),
    path('api/vl/students/<int:pk>/', r_studentview.r_studentview),
    path('api/vl/studentdetails/<int:pk>/', r_studentview.r_studentmocktestview)
]
