from django import forms
   
# creating a form 
# class BookOrder(forms.Form):
   
#     Book_name = forms.CharField(max_length = 200)
#     Book_qty = forms.CharField(max_length = 200)
#     Address = forms.CharField(max_length=100)
#     Pincode = forms.IntegerField(help_text = "Enter 6 digit of Pincode")
#     password = forms.CharField(widget = forms.PasswordInput())

# print(BookOrder())
# class StudentForm(forms.Form):
   
#     first_name = forms.CharField(max_length = 200)
#     last_name = forms.CharField(max_length = 200)
#     roll_number = forms.IntegerField(help_text = "Enter 6 digit roll number")
#     password = forms.CharField(widget = forms.PasswordInput())

# print(StudentForm())

from django import forms
   

class Lib_login(forms.Form):
   
    first_name = forms.CharField(max_length = 200)
    
    mobile_number = forms.IntegerField(help_text = "Enter 6 digit roll number")
    password = forms.CharField(widget = forms.PasswordInput())


print(Lib_login())