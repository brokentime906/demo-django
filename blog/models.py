from django.db import models

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now= True)

    class Meta:
        abstract =True
# Create your models here.

class Post(BaseModel):
    title = models.CharField(max_length=100)
    content = models.TextField()
    
    