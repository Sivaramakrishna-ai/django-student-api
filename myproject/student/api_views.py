# from rest_framework.decorators import api_view
# from rest_framework.response import Response


# @api_view(["GET"])
# def hello_api(request):

#     return Response({
#         "message": "Hello, Django REST Framework!"
#     })


# from rest_framework.decorators import api_view
# from rest_framework.response import Response

# from .models import Student
# from .serializers import StudentSerializer


# @api_view(["GET"])
# def hello_api(request):

#     return Response({
#         "message": "Hello, Django REST Framework!"
#     })


# @api_view(["GET"])
# def student_list_api(request):

#     students = Student.objects.all()

#     serializer = StudentSerializer(
#         students,
#         many=True
#     )

#     return Response(
#         serializer.data
#     )



# from rest_framework.decorators import api_view
# from rest_framework.response import Response

# from .models import Student
# from .serializers import StudentSerializer


# @api_view(["GET"])
# def hello_api(request):

#     return Response({
#         "message": "Hello, Django REST Framework!"
#     })


# @api_view(["GET", "POST"])
# def student_list_api(request):

#     if request.method == "GET":

#         students = Student.objects.all()

#         serializer = StudentSerializer(
#             students,
#             many=True
#         )

#         return Response(
#             serializer.data
#         )

#     if request.method == "POST":

#         serializer = StudentSerializer(
#             data=request.data
#         )

#         if serializer.is_valid():

#             serializer.save()

#             return Response(
#                 serializer.data,
#                 status=201
#             )

#         return Response(
#             serializer.errors,
#             status=400
#         )



### Updating a student using PUT method 

# from rest_framework.decorators import api_view
# from rest_framework.response import Response

# from django.shortcuts import get_object_or_404
# from .models import Student
# from .serializers import StudentSerializer

# @api_view(["GET"])
# def hello_api(request):
#     return Response({"Message":"Hello Django Rest Framework!"})


# @api_view(["GET","POST"])
# def student_list_api(request):
#     if request.method == "Get":
#         students = Student.objects.all()
#         serializer = StudentSerializer(
#             students,
#             many = True
#         )

#         return Response(
#             serializer.data
#         )

#     if request.method == "POST":
#         serializer = StudentSerializer(
#             data = request.data
#         )
#         if serializer.is_valid():
#           serializer.save()

#         return Response(
#             serializer.data,
#             status = 201
#         )
#     return Response(
#         serializer.errors,
#         status = 400
#         )

# @api_view(["GET","PUT"])
# def student_detail_api(request,id):
#     student = get_object_or_404(Student,id=id)

#     if request.method == "GET":
#         serializer = StudentSerializer(student)
#         return Response(serializer.data)

#     if request.method == "PUT":
#         serializer = StudentSerializer(
#             student,
#             data=request.data
#         )
#         if serializer.is_valid():
#             serializer.save()

#             return Response(
#                 serializer.data
#         )
#     return Response(
#         serializer.errors,status=400
#     )

### Now adding PATCH, PATCH = Only we want to update specific filed example: age or name or address etc only one field we change not all


# from rest_framework.decorators import api_view
# from rest_framework.response import Response

# from django.shortcuts import get_object_or_404
# from .models import Student
# from .serializers import StudentSerializer


# @api_view(["GET"])
# def hello_api(request):
#     return Response({"Message":"Hello Django Rest Framework!"})


# @api_view(["GET","POST"])
# def student_list_api(request):
#     if request.method == "GET":
#         students = Student.objects.all()
#         serializer = StudentSerializer(
#             students,
#             many = True
#         )

#         return Response(
#             serializer.data
#         )

#     if request.method == "POST":
#         serializer = StudentSerializer(
#             data = request.data
#         )
#         if serializer.is_valid():
#           serializer.save()

#           return Response(
#             serializer.data,
#             status = 201
#         )
#         return Response(
#           serializer.errors,
#           status = 400
#         )

# @api_view(["GET","PUT","PATCH"])
# def student_detail_api(request,id):
#     student = get_object_or_404(Student,id=id)

#     if request.method == "GET":
#         serializer = StudentSerializer(student)
#         return Response(serializer.data)

#     if request.method == "PUT":
#         serializer = StudentSerializer(
#             student,
#             data=request.data
#         )
#         if serializer.is_valid():
#             serializer.save()

#             return Response(
#                 serializer.data
#         )
#         return Response(
#           serializer.errors,status=400
#     )

#     if request.method == "PATCH":
#      serializer = StudentSerializer(student,
#             data=request.data,
#             partial = True
            
#         )
#      if serializer.is_valid():
#             serializer.save()

#             return Response(
#                 serializer.data
#             )

#      return Response(
#             serializer.errors,
#             status=400
#         )


### Now student DELETE method 


from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.shortcuts import get_object_or_404
from .models import Student
from .serializers import StudentSerializer


@api_view(["GET"])
def hello_api(request):
    return Response({"Message":"Hello Django Rest Framework!"})


@api_view(["GET","POST"])
def student_list_api(request):
    if request.method == "GET":
        students = Student.objects.all()
        serializer = StudentSerializer(
            students,
            many = True
        )

        return Response(
            serializer.data
        )

    if request.method == "POST":
        serializer = StudentSerializer(
            data = request.data
        )
        if serializer.is_valid():
          serializer.save()

          return Response(
            serializer.data,
            status = 201
        )
        return Response(
          serializer.errors,
          status = 400
        )

@api_view(["GET","PUT","PATCH","DELETE"])
def student_detail_api(request,id):
    student = get_object_or_404(Student,id=id)

    if request.method == "GET":
        serializer = StudentSerializer(student)
        return Response(serializer.data)

    if request.method == "PUT":
        serializer = StudentSerializer(
            student,
            data=request.data
        )
        if serializer.is_valid():
            serializer.save()

            return Response(
                serializer.data
        )
        return Response(
          serializer.errors,status=400
    )

    if request.method == "PATCH":
     serializer = StudentSerializer(student,
            data=request.data,
            partial = True
            
        )
     if serializer.is_valid():
            serializer.save()

            return Response(
                serializer.data
            )

     return Response(
            serializer.errors,
            status=400
        )

    if request.method == "DELETE":
        student.delete()
        return Response({
            "Message": "Student Deleted Successfully"},
                        status = 204)