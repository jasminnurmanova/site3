from django.db import models

# Create your models here.
class Category(models.Model):
    type=models.CharField(max_length=30)

    def __str__(self):
        return self.type

class Markazlar(models.Model):
    name=models.CharField(max_length=200)
    desc=models.TextField()
    created_at=models.DateField()
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    location=models.CharField(max_length=200)
    image=models.ImageField(upload_to='markazlar_images/',blank=True,null=True)
    def __str__(self):
        return self.name


