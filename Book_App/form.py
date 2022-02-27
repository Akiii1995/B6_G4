from django import forms
from Book_App.models import Book
   
 
class StudentForm(forms.Form):
   
    first_name = forms.CharField(max_length = 200)
    last_name = forms.CharField(max_length = 200)
    roll_number = forms.IntegerField(help_text = "Enter 6 digit roll number")
    password = forms.CharField(widget = forms.PasswordInput())

print(StudentForm())


class StudentForm(forms.ModelForm):
    Keep_Logged_in = forms.BooleanField()
    Remeber_Password = forms.BooleanField()
    Upload_Image = forms.FileField()
    class Meta:
        model = Book
        # fields = ("Name","Price","Qty")
        fields = "__all__"
        # exclude = ("Price",)