"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
# from django.urls import path
# from . import views


# urlpatterns = [

#     path(
#         "admin/",
#         admin.site.urls
#     ),

#     path(
#         "",
#         views.home,
#         name="home"
#     ),

#     path(
#         "student/<int:id>/",
#         views.student_detail,
#         name="student_detail"
#     ),

#     path(
#         "student/<int:id>/edit/",
#         views.student_edit,
#         name="student_edit"
#     ),

# ]


# from django.contrib import admin
# from django.urls import path
# from . import views
# from student.api_views import (hello_api,student_list_api,student_detail_api,)


# urlpatterns = [

#     path(
#         "admin/",
#         admin.site.urls
#     ),

#     path(
#         "",
#         views.home,
#         name="home"
#     ),

#     path(
#         "student/<int:id>/",
#         views.student_detail,
#         name="student_detail"
#     ),

#     path(
#         "student/<int:id>/edit/",
#         views.student_edit,
#         name="student_edit"
#     ),

#     path(
#         "student/<int:id>/delete/",
#         views.student_delete,
#         name="student_delete"
#     ),

#      path(
#         "api/hello/",
#          hello_api,
#         name="hello_api"),


#     path(
#         "api/students/",
#          student_list_api,
#         name="student_list_api"
#     ),

# ]


# Using PUT method

from django.contrib import admin
from django.urls import path

from myproject import views


from student.api_views import (
    hello_api,
    student_list_api,
    student_detail_api,
)


urlpatterns = [

    # ========================================================
    # ADMIN
    # ========================================================

    path(
        "admin/",
        admin.site.urls
    ),


    # ========================================================
    # NORMAL DJANGO HTML VIEWS
    # ========================================================

    path(
        "",
        views.home,
        name="home"
    ),

    path(
        "student/<int:id>/",
        views.student_detail,
        name="student_detail"
    ),

    path(
        "student/<int:id>/edit/",
        views.student_edit,
        name="student_edit"
    ),

    path(
        "student/<int:id>/delete/",
        views.student_delete,
        name="student_delete"
    ),


    # ========================================================
    # DJANGO REST FRAMEWORK APIs
    # ========================================================

    path(
        "api/hello/",
        hello_api,
        name="hello_api"
    ),

    path(
        "api/students/",
        student_list_api,
        name="student_list_api"
    ),

    path(
        "api/students/<int:id>/",
        student_detail_api,
        name="student_detail_api"
    ),

    path(
    "cache-test/",
    views.cache_test,
    name="cache_test"
),

# TRANSACTION EXAMPLE

path(
    "transaction-test/",
    views.transaction_test,
    name="transaction_test"
),

]