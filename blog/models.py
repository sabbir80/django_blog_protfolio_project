from django.db import models

class Category(models.Model):
    category_name= models.CharField(max_length=100)

    def __str__(self):
        return self.category_name

class Post(models.Model):
    title= models.CharField(max_length=255)
    body= models.TextField(blank= True, null=True )
    create_on= models.DateTimeField(auto_now_add=True)
    last_modifie= models.DateTimeField(auto_now= True)
    image = models.FileField(blank=True, null= True)
    category= models.ManyToManyField('Category', related_name='posts')
    def __str__(self):
        return self.title
class Comment(models.Model):
    author= models.CharField(max_length=20)
    body= models.TextField( blank= True, null= True)
    create_on= models.DateTimeField(auto_now_add= True)
    post= models.ForeignKey('Post', on_delete= models.CASCADE)


