from django.db import models


# Create your models here.
class Series(models.Model):
    Name=models.CharField(max_length=100,unique=True)
    Seasons=models.IntegerField()
    Episodes=models.IntegerField()
    Genre=models.CharField(max_length=100,)
   



class Movies(models.Model):
        Name=models.CharField(max_length=100,unique=True)
        Genre=models.CharField(max_length=100)



class Anime(models.Model):
    Name=models.CharField(max_length=100,unique=True)
    Season=models.IntegerField()
    Episodes=models.IntegerField()

    


class Sitcom(models.Model):
      Name=models.CharField(max_length=100,unique=True)
      Seasons=models.IntegerField()
      Episodes=models.IntegerField()
      


class Cartoon(models.Model):
    Name= Name=models.CharField(max_length=100,unique=True)
    Seasons=models.IntegerField()  
    Episodes=models.IntegerField()
        
      



      


    





  
