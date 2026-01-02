from django.db import models

# Create your models here.
#DataBse Design
class Todo(models.Model):
    #Task title
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)



    def __str__(self):
        return self.title
     