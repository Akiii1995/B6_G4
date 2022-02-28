from django.db import models

# Create your models here.
print("in models.py")
class Book(models.Model):
    Name = models.CharField(max_length=100)
    Price = models.IntegerField()
    Qty = models.IntegerField()
    Is_Active = models.BooleanField(default=True)

    class Meta:
        db_table = "book"


    def __str__(self):
        return f"{self.Name}"




# import the standard Django Model
# from built-in library
from django.db import models
  
# declare a new model with a name "GeeksModel"
class GeeksModel(models.Model):
        # fields of the model
    title = models.CharField(max_length = 200)
    description = models.TextField()
    last_modified = models.DateTimeField(auto_now_add = True)
    img = models.ImageField(upload_to = "images/")
  
        # renames the instances of the model
        # with their title name
    def __str__(self):
        return self.title

