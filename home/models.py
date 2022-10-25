from django.db import models

# Create your models here.
class Register(models.Model):
      name = models.CharField(max_length=200)
      email = models.CharField(max_length=600)
      number= models.CharField(max_length=600)
      
      def _str_(self):
             return self.name
      
      class Meta:
            verbose_name = ('Register')
            verbose_name_plural = ('Register')
     
      
     
     
     
     
     
class Pitch(models.Model):
      name = models.CharField(max_length=200)
      pitch = models.TextField()
      
      class Meta:
            verbose_name = ('Pitch')
            verbose_name_plural = ('Pitch')
     
      def _str_(self):
         return self.name     