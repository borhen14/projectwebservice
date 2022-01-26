
from django.db import models

# Create your models here.


class User(models.Model):
    first_name= models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    class Meta:
        abstract = True
    def __str__(self) : 
        return self.first_name+" "+ self.last_name
class Author(User):
    bio = models.CharField(max_length=255)
class Librarian(User):
    departement= models.CharField(max_length=50)    
class Member(User):
    cin = models.CharField(max_length=8)
    address = models.CharField(max_length=50)
class Book(models.Model):
    title= models.CharField(max_length=70)
    quantity=models.IntegerField()
    publication_date= models.DateField()
    isbn=models.CharField(max_length=20)
    author = models.ForeignKey(Author,on_delete=models.CASCADE)
    members = models.ManyToManyField('Member',through="BookMember")
    def __str__(self) :
        return self.title
class BookMember(models.Model):
    book= models.ForeignKey(Book,on_delete=models.CASCADE)
    member = models.ForeignKey(Member,on_delete=models.CASCADE)
    dateIn = models.DateField()
    dateOut = models.DateField()
    