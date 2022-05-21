from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    age=models.IntegerField(null=True,blank=True)
    gender=models.CharField(max_length=10 )

    # ! db Tablosunu vsCode da console da veya /admin de nasil segileyecegimizi belirtiyoruz:
    # * id-name-age seklinde tablo gorunecek
    def __str__(self):
        return "{}  {} {} {} ".format(self.id,self.name, self.surname, self.age )

class Publisher(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return "{}".format(self.name)

class Book(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    def __str__(self):
        return "{} {}".format(self.name,self.author)




class Person1(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    def __str__(self):
        return "{}  {} ".format(self.name, self.surname )
class Person2(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    def __str__(self):
        return "{}  {} {} ".format(self.name, self.surname )
class Person3(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    def __str__(self):
        return "{}  {} {} ".format(self.name, self.surname )