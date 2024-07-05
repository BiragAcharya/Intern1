# from django.db import models

# # Create your models here.

# class Blogs(models.Model):
#     title = models.CharField(max_length=100)
#     subtitle = models.CharField(max_length=100)
#     description = models.TextField()
#     image = models.ImageField(upload_to='blog')

#     def __str__(self):
#         return str.title


from django.db import models

class BlogEntry(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='blogs')

    def __str__(self):
        return self.title

