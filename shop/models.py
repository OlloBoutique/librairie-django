from django.db import models
class Livre(models.Model):
    titre = models.CharField(max_length=200)
    prix = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to ='livres/')
    pdf = models.FileField(upload_to='pdf/')


class Livre(models.Model):
    titre = models.CharField(max_length=200)
    prix = models.IntegerField()
    image = models.ImageField(upload_to='livres/', null=True, blank=True)


class Livre(models.Model):
    titre = models.CharField(max_length=200)
    prix = models.IntegerField()
    image = models.ImageField(upload_to='livres/', null=True, blank=True)
    pdf = models.FileField(upload_to='pdfs/', null=True, blank=True)

   
    def __str__(self):
        return self.titre