

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from student.models import Student
from student.forms import StudentForm
# from django.db import transaction


# HOME + REGISTER + SEARCH
def home(request):

    if request.method == "POST":

        form = StudentForm(request.POST)

        if form.is_valid():

            student = form.save(commit=False)

            student.name = student.name.title()
            student.age = student.age + 1
            student.city = student.city.title()

            student.save()

            return redirect("home")

    else:

        form = StudentForm()


    search = request.GET.get("search")

    if search:

        students = Student.objects.filter(
            name__icontains=search
        )

    else:

        students = Student.objects.all()


    context = {
        "form": form,
        "students": students
    }


    return render(
        request,
        "home.html",
        context
    )


# STUDENT DETAILS
def student_detail(request, id):

    student = get_object_or_404(
        Student,
        id=id
    )

    return render(
        request,
        "student_detail.html",
        {
            "student": student
        }
    )


# EDIT STUDENT
def student_edit(request, id):

    student = get_object_or_404(
        Student,
        id=id
    )

    if request.method == "POST":

        student.name = request.POST.get("name")
        student.age = request.POST.get("age")
        student.city = request.POST.get("city")

        student.save()

        return redirect(
            "student_detail",
            id=student.id
        )

    return render(
        request,
        "student_edit.html",
        {
            "student": student
        }
    )


# DELETE STUDENT
def student_delete(request, id):

    student = get_object_or_404(
        Student,
        id=id
    )

    student.delete()

    return redirect("home")


# CACHE EXAMPLE
from django.http import HttpResponse
from django.core.cache import cache


def cache_test(request):

    value = cache.get("message")

    if value is None:

        value = "Hello from database/server"

        cache.set("message", value, 60)

        print("CACHE MISS")

    else:

        print("CACHE HIT")

    return HttpResponse(value)

## Transacion test
# TRANSACTION TEST

# def transaction_test(request):

#     with transaction.atomic():

#         student = Student.objects.create(
#             name="Transaction Test",
#             age=20,
#             city="Vizag"
#         )

#         print("Student created inside transaction")

#         raise Exception("Something went wrong")

#     return HttpResponse("Transaction successful")