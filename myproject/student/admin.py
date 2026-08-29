# from django.contrib import admin
# from .models import Student

# admin.site.register(Student)



# from django.contrib import admin
# from .models import Student, Course


# admin.site.register(Student)

# admin.site.register(Course)



## Adding Profile
# from django.contrib import admin
# from .models import Student, Course, StudentProfile


# admin.site.register(Student)

# admin.site.register(Course)

# admin.site.register(StudentProfile)



## ManhyToManyFields
from django.contrib import admin
from .models import Student, Course, StudentProfile, Subject


admin.site.register(Student)

admin.site.register(Course)

admin.site.register(StudentProfile)

admin.site.register(Subject)
