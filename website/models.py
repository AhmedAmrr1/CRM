from django.db import models

# no comma in the models
# Django best practice is to use lowercase field names

BRANCH_CHOICES = [
    ('sm' , 'Smouha'),
    ('bo','Boukla'),
    ('mi' ,'Miami'),
]

class Record(models.Model):
    first_name = models.TextField(max_length=64)
    last_name = models.TextField(max_length=64)
    email = models.EmailField(max_length=64)
    phone_number = models.CharField(max_length=32)
    city = models.CharField(max_length=64)
    address = models.CharField(max_length=128)
    branch = models.CharField(max_length=32, choices=BRANCH_CHOICES , null= True , blank= True)
    items = models.IntegerField(default=0) 
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):  # converting from object to readible string & readable representation of a model  identify objects clearly
        return f"{self.first_name} {self.last_name}"
