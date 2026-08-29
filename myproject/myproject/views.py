# # from django.shortcuts import render

# # def home(request):
# #     return render(request, "home.html")

# # from django.shortcuts import render

# # def home(request):

# #     context = {
# #         "is_logged_in": True
# #     }

# #     return render(request, "home.html", context)

# # from django.shortcuts import render

# # def home(request):

# #     username = request.GET.get("username")

# #     context = {
# #         "username": username
# #     }

# #     return render(request, "home.html", context)




# # from django.shortcuts import render

# # def home(request):

# #     username = ""

# #     if request.method == "POST":
# #         username = request.POST.get("username")

# #     context = {
# #         "username": username
# #     }

# #     return render(request, "home.html", context)


# # from django.shortcuts import render
# # from student.models import Student

# # def home(request):

# #     if request.method == "POST":

# #         name = request.POST.get("name")
# #         age = request.POST.get("age")
# #         city = request.POST.get("city")

# #         student = Student(
# #             name=name,
# #             age=age,
# #             city=city
# #         )

# #         student.save()

# #     return render(request, "home.html")





# # from django.shortcuts import render
# # from student.models import Student


# # def home(request):

# #     if request.method == "POST":

# #         name = request.POST.get("name")
# #         age = request.POST.get("age")
# #         city = request.POST.get("city")

# #         student = Student(
# #             name=name,
# #             age=age,
# #             city=city
# #         )

# #         student.save()

# #     students = Student.objects.all()

# #     context = {
# #         "students": students
# #     }

# #     return render(request, "home.html", context)


# # def student_detail(request, id):

# #     student = Student.objects.get(id=id)

# #     context = {
# #         "student": student
# #     }

# #     return render(request, "student_detail.html", context)



# # from django.shortcuts import render
# # from student.models import Student


# # def home(request):

# #     if request.method == "POST":

# #         name = request.POST.get("name")
# #         age = request.POST.get("age")
# #         city = request.POST.get("city")

# #         student = Student(
# #             name=name,
# #             age=age,
# #             city=city
# #         )

# #         student.save()

# #     students = Student.objects.all()

# #     context = {
# #         "students": students
# #     }

# #     return render(
# #         request,
# #         "home.html",
# #         context
# #     )


# # def student_detail(request, id):

# #     student = Student.objects.get(id=id)

# #     context = {
# #         "student": student
# #     }

# #     return render(
# #         request,
# #         "student_detail.html",
# #         context
# #     )


# # def student_edit(request, id):

# #     student = Student.objects.get(id=id)

# #     if request.method == "POST":

# #         student.name = request.POST.get("name")

# #         student.age = request.POST.get("age")

# #         student.city = request.POST.get("city")

# #         student.save()

# #         return render(
# #             request,
# #             "student_detail.html",
# #             {"student": student}
# #         )

# #     return render(
# #         request,
# #         "student_edit.html",
# #         {"student": student}
# #     )


# # from django.shortcuts import render, redirect, get_object_or_404
# # from student.models import Student


# # # HOME / REGISTER / SHOW ALL STUDENTS
# # def home(request):

# #     if request.method == "POST":

# #         name = request.POST.get("name")

# #         age = request.POST.get("age")

# #         city = request.POST.get("city")

# #         student = Student(
# #             name=name,
# #             age=age,
# #             city=city
# #         )

# #         student.save()

# #     students = Student.objects.all()

# #     context = {
# #         "students": students
# #     }

# #     return render(request, "home.html", context)


# # # SHOW ONE STUDENT
# # def student_detail(request, id):

# #     student = get_object_or_404(Student, id=id)

# #     context = {
# #         "student": student
# #     }

# #     return render(request, "student_detail.html", context)


# # # EDIT STUDENT
# # def student_edit(request, id):

# #     student = get_object_or_404(Student, id=id)

# #     if request.method == "POST":

# #         student.name = request.POST.get("name")

# #         student.age = request.POST.get("age")

# #         student.city = request.POST.get("city")

# #         student.save()

# #         return redirect("/student/" + str(id) + "/")

# #     context = {
# #         "student": student
# #     }

# #     return render(request, "student_edit.html", context)


# # # DELETE STUDENT
# # def student_delete(request, id):

# #     student = get_object_or_404(Student, id=id)

# #     student.delete()

# #     return redirect("/")


# # from django.shortcuts import render, get_object_or_404, redirect
# # from student.models import Student
# # from student.forms import StudentForm


# # # HOME + REGISTER + SEARCH
# # def home(request):

# #     if request.method == "POST":

# #         form = StudentForm(request.POST)

# #         if form.is_valid():

# #             form.save()

# #             return redirect("home")

# #     else:

# #         form = StudentForm()


# #     search = request.GET.get("search")


# #     if search:

# #         students = Student.objects.filter(
# #             name__icontains=search
# #         )

# #     else:

# #         students = Student.objects.all()


# #     context = {
# #         "form": form,
# #         "students": students
# #     }


# #     return render(
# #         request,
# #         "home.html",
# #         context
# #     )


# # # STUDENT DETAILS
# # def student_detail(request, id):

# #     student = get_object_or_404(
# #         Student,
# #         id=id
# #     )

# #     return render(
# #         request,
# #         "student_detail.html",
# #         {
# #             "student": student
# #         }
# #     )


# # # EDIT STUDENT
# # def student_edit(request, id):

# #     student = get_object_or_404(
# #         Student,
# #         id=id
# #     )


# #     if request.method == "POST":

# #         student.name = request.POST.get("name")

# #         student.age = request.POST.get("age")

# #         student.city = request.POST.get("city")

# #         student.save()

# #         return redirect(
# #             "student_detail",
# #             id=student.id
# #         )


# #     return render(
# #         request,
# #         "edit.html",
# #         {
# #             "student": student
# #         }
# #     )


# # # DELETE STUDENT
# # def student_delete(request, id):

# #     student = get_object_or_404(
# #         Student,
# #         id=id
# #     )

# #     student.delete()

# #     return redirect("home")



# ## Using Commit = False

# # from django.shortcuts import render, get_object_or_404, redirect
# # from student.models import Student
# # from student.forms import StudentForm


# # # HOME + REGISTER + SEARCH
# # def home(request):

# #     if request.method == "POST":

# #         form = StudentForm(request.POST)

# #         if form.is_valid():

# #             # Create Student object but don't save yet
# #             student = form.save(commit=False)

# #             # Change all three fields before saving

# #             student.name = student.name.title()

# #             student.age = student.age + 1

# #             student.city = student.city.title()

# #             # Now save to database
# #             student.save()

# #             return redirect("home")

# #     else:

# #         form = StudentForm()


# #     # SEARCH
# #     search = request.GET.get("search")


# #     if search:

# #         students = Student.objects.filter(
# #             name__icontains=search
# #         )

# #     else:

# #         students = Student.objects.all()


# #     context = {
# #         "form": form,
# #         "students": students
# #     }


# #     return render(
# #         request,
# #         "home.html",
# #         context
# #     )


# # # STUDENT DETAILS
# # def student_detail(request, id):

# #     student = get_object_or_404(
# #         Student,
# #         id=id
# #     )

# #     return render(
# #         request,
# #         "student_detail.html",
# #         {
# #             "student": student
# #         }
# #     )


# # # EDIT STUDENT
# # def student_edit(request, id):

# #     student = get_object_or_404(
# #         Student,
# #         id=id
# #     )

# #     if request.method == "POST":

# #         student.name = request.POST.get("name")

# #         student.age = request.POST.get("age")

# #         student.city = request.POST.get("city")

# #         student.save()

# #         return redirect(
# #             "student_detail",
# #             id=student.id
# #         )

# #     return render(
# #         request,
# #         "edit.html",
# #         {
# #             "student": student
# #         }
# #     )


# # # DELETE STUDENT
# # def student_delete(request, id):

# #     student = get_object_or_404(
# #         Student,
# #         id=id
# #     )

# #     student.delete()

# #     return redirect("home")




# # from django.shortcuts import render, get_object_or_404, redirect
# # from student.models import Student
# # from student.forms import StudentForm




# # HOME + REGISTER + SEARCH
# # def home(request):

# #     if request.method == "POST":

# #         form = StudentForm(request.POST)

# #         if form.is_valid():

# #             student = form.save(commit=False)

# #             student.name = student.name.title()
# #             student.age = student.age + 1
# #             student.city = student.city.title()

# #             student.save()

# #             return redirect("home")

# #     else:

# #         form = StudentForm()

# #     search = request.GET.get("search")

# #     if search:

# #         students = Student.objects.filter(
# #             name__icontains=search
# #         )

# #     else:

# #         students = Student.objects.all()

# #     context = {
# #         "form": form,
# #         "students": students
# #     }

# #     return render(
# #         request,
         
# #         "home.html",
# #         context
# #     )


# # # STUDENT DETAILS
# # def student_detail(request, id):

# #     student = get_object_or_404(
# #         Student,
# #         id=id
# #     )

# #     return render(
# #         request,
# #         "student_detail.html",
# #         {
# #             "student": student
# #         }
# #     )


# # # EDIT STUDENT
# # def student_edit(request, id):

# #     student = get_object_or_404(
# #         Student,
# #         id=id
# #     )

# #     if request.method == "POST":

# #         student.name = request.POST.get("name")
# #         student.age = request.POST.get("age")
# #         student.city = request.POST.get("city")

# #         student.save()

# #         return redirect(
# #             "student_detail",
# #             id=student.id
# #         )

# #     return render(
# #         request,
# #         "student_edit.html",
# #         {
# #             "student": student
# #         }
# #     )


# # # DELETE STUDENT    1
# # def student_delete(request, id):

# #     student = get_object_or_404(
# #         Student,
# #         id=id
# #     )

# #     student.delete()

# #     return redirect("home")





# ### CACHE example
# from django.http import HttpResponse
# from django.core.cache import cache

# def cache_test(request):

#     value = cache.get("message")

#     if value is None:

#         value = "Hello from database/server"

#         cache.set("message", value, 60)

#         print("CACHE MISS")

#     else:

#         print("CACHE HIT")

#     return HttpResponse(value)







from django.shortcuts import render, get_object_or_404, redirect
from student.models import Student
from student.forms import StudentForm
from django.db import transaction


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

## Transaction test

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



## Transaction test with Exceptional Handling     





def transaction_test(request):

    try:

        with transaction.atomic():

            student = Student.objects.create(
                name="Transaction Test",
                age=20,
                city="Vizag"
            )

            print("Student created inside transaction")

            raise Exception("Something went wrong")

    except Exception as e:

        print("Transaction failed")
        print("Error:", e)

        return HttpResponse(
            "Transaction failed. Changes were rolled back."
        )

    return HttpResponse("Transaction successful")