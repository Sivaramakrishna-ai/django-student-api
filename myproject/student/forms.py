# from django import forms
# from .models import Student


# class StudentForm(forms.ModelForm):

#     class Meta:

#         model = Student

#         fields = [
#             "name",
#             "age",
#             "city"
#         ]


#     def clean_age(self):

#         age = self.cleaned_data["age"]

#         if age < 18:

#             raise forms.ValidationError(
#                 "Age must be 18 or above."
#             )

#         return age









# from django import forms
# from .models import Student


# class StudentForm(forms.ModelForm):

#     class Meta:
#         model = Student

#         fields = [
#             "name",
#             "age",
#             "city"
#         ]

#     def clean_age(self):

#         age = self.cleaned_data["age"]

#         if age < 18:
#             raise forms.ValidationError(
#                 "Age must be 18 or above."
#             )

#         return age

#     def clean_name(self):

#         name = self.cleaned_data["name"]

#         if not name.replace(" ", "").isalpha():
#             raise forms.ValidationError(
#                 "Name should contain only letters."
#             )

#         return name





# from django import forms
# from .models import Student


# class StudentForm(forms.ModelForm):

#     class Meta:
#         model = Student

#         fields = [
#             "name",
#             "age",
#             "city"
#         ]

#     def clean_name(self):

#         name = self.cleaned_data["name"]

#         if not name.replace(" ", "").isalpha():
#             raise forms.ValidationError(
#                 "Name should contain only letters."
#             )

#         return name

#     def clean_age(self):

#         age = self.cleaned_data["age"]

#         if age < 18:
#             raise forms.ValidationError(
#                 "Age must be 18 or above."
#             )

#         return age

#     def clean_city(self):

#         city = self.cleaned_data["city"]

#         if len(city) < 2:
#             raise forms.ValidationError(
#                 "City name must contain at least 2 characters."
#             )

#         return city

#     def clean(self):

#         cleaned_data = super().clean()

#         name = cleaned_data.get("name")
#         age = cleaned_data.get("age")

#         if name and age:

#             if name.lower() == "siva" and age < 21:

#                 raise forms.ValidationError(
#                     "Siva must be at least 21 years old."
#                 )

#         return cleaned_data



# from django import forms
# from .models import Student


# class StudentForm(forms.ModelForm):

#     class Meta:
#         model = Student

#         fields = [
#             "name",
#             "age",
#             "city"
#         ]

#         widgets = {
#             "name": forms.TextInput(
#                 attrs={
#                     "placeholder": "Enter your name"
#                 }
#             ),

#             "age": forms.NumberInput(
#                 attrs={
#                     "placeholder": "Enter your age"
#                 }
#             ),

#             "city": forms.TextInput(
#                 attrs={
#                     "placeholder": "Enter your city"
#                 }
#             ),
#         }

#     def clean_name(self):

#         name = self.cleaned_data["name"]

#         if not name.replace(" ", "").isalpha():
#             raise forms.ValidationError(
#                 "Name should contain only letters."
#             )

#         return name

#     def clean_age(self):

#         age = self.cleaned_data["age"]

#         if age < 18:
#             raise forms.ValidationError(
#                 "Age must be 18 or above."
#             )

#         return age

#     def clean_city(self):

#         city = self.cleaned_data["city"]

#         if len(city) < 2:
#             raise forms.ValidationError(
#                 "City name must contain at least 2 characters."
#             )

#         return city

#     def clean(self):

#         cleaned_data = super().clean()

#         name = cleaned_data.get("name")
#         age = cleaned_data.get("age")

#         if name and age:

#             if name.lower() == "siva" and age < 21:
#                 raise forms.ValidationError(
#                     "Siva must be at least 21 years old."
#                 )

#         return cleaned_data




## Adding CSS classes and IDs using Django Form widgets.
# from django import forms
# from .models import Student


# class StudentForm(forms.ModelForm):

#     class Meta:
#         model = Student

#         fields = [
#             "name",
#             "age",
#             "city"
#         ]

#         widgets = {

#             "name": forms.TextInput(
#                 attrs={
#                     "placeholder": "Enter your name",
#                     "class": "student-input",
#                     "id": "student-name"
#                 }
#             ),

#             "age": forms.NumberInput(
#                 attrs={
#                     "placeholder": "Enter your age",
#                     "class": "student-input",
#                     "id": "student-age"
#                 }
#             ),

#             "city": forms.TextInput(
#                 attrs={
#                     "placeholder": "Enter your city",
#                     "class": "student-input",
#                     "id": "student-city"
#                 }
#             ),

#         }


#     def clean_name(self):

#         name = self.cleaned_data["name"]

#         if not name.replace(" ", "").isalpha():

#             raise forms.ValidationError(
#                 "Name should contain only letters."
#             )

#         return name


#     def clean_age(self):

#         age = self.cleaned_data["age"]

#         if age < 18:

#             raise forms.ValidationError(
#                 "Age must be 18 or above."
#             )

#         return age


#     def clean_city(self):

#         city = self.cleaned_data["city"]

#         if len(city) < 2:

#             raise forms.ValidationError(
#                 "City name must contain at least 2 characters."
#             )

#         return city


#     def clean(self):

#         cleaned_data = super().clean()

#         name = cleaned_data.get("name")

#         age = cleaned_data.get("age")


#         if name and age:

#             if name.lower() == "siva" and age < 21:

#                 raise forms.ValidationError(
#                     "Siva must be at least 21 years old."
#                 )


#         return cleaned_data




### Adding DjangoForm error messages

from django import forms
from .models import Student


class StudentForm(forms.ModelForm):

    class Meta:

        model = Student

        fields = [
            "name",
            "age",
            "city"
        ]

        labels = {
            "name": "Student Name",
            "age": "Student Age",
            "city": "Student City",
        }

        error_messages = {

            "name": {
                "required": "Please enter the student's name.",
            },

            "age": {
                "required": "Please enter the student's age.",
                "invalid": "Please enter a valid number.",
            },

            "city": {
                "required": "Please enter the student's city.",
            },
        }

        widgets = {

            "name": forms.TextInput(
                attrs={
                    "placeholder": "Enter student name",
                    "class": "student-input",
                    "id": "student-name",
                }
            ),

            "age": forms.NumberInput(
                attrs={
                    "placeholder": "Enter student age",
                    "class": "student-input",
                    "id": "student-age",
                }
            ),

            "city": forms.TextInput(
                attrs={
                    "placeholder": "Enter student city",
                    "class": "student-input",
                    "id": "student-city",
                }
            ),
        }


    def clean_name(self):

        name = self.cleaned_data["name"]

        if not name.replace(" ", "").isalpha():

            raise forms.ValidationError(
                "Name should contain only letters."
            )

        return name


    def clean_age(self):

        age = self.cleaned_data["age"]

        if age < 18:

            raise forms.ValidationError(
                "Age must be 18 or above."
            )

        return age


    def clean_city(self):

        city = self.cleaned_data["city"]

        if len(city) < 2:

            raise forms.ValidationError(
                "City name must contain at least 2 characters."
            )

        return city


    def clean(self):

        cleaned_data = super().clean()

        name = cleaned_data.get("name")

        age = cleaned_data.get("age")


        if name and age:

            if name.lower() == "siva" and age < 21:

                raise forms.ValidationError(
                    "Siva must be at least 21 years old."
                )


        return cleaned_data