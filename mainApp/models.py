from django.db import models
import uuid


class SolutionDetail(models.Model):
    heading = models.CharField(max_length=400)


    def __str__(self):return self.heading


class SolutionDetailParagraph(models.Model):
    paragraph = models.TextField()
    solution_detail = models.ForeignKey(SolutionDetail,on_delete=models.CASCADE)




class ParthershipNetwork(models.Model):
    name =models.CharField(max_length=300)
    email = models.EmailField()
    phone_number = models.CharField(max_length=300)

    def __str__(self): return '${self.name}'

class WorkWithus(models.Model):
    name =models.CharField(max_length=300)
    email = models.EmailField()
    phone_number = models.CharField(max_length=300)
    upload_cv = models.FileField(upload_to='emtrics_cv/')

    def __str__(self):return f'{self.name}'


class Contact(models.Model):
    name =models.CharField(max_length=300)
    phone_number = models.CharField(max_length=300)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):return f'{self.name}'


class ContinentLocation(models.Model):
    slug = models.CharField(max_length=100,)
    name = models.CharField(max_length=300)

    def __str__(self):
        return f'{self.name}'



class CountryLocation(models.Model):
    slug = models.CharField(max_length=100)
    continent_location = models.ForeignKey(ContinentLocation,on_delete=models.CASCADE)
    name = models.CharField(max_length=300)

    def __str__(self):
        return f'{self.name}'

class countryAddress(models.Model):
    state = models.CharField(max_length=300,default="..")
    phone = models.CharField(max_length=300)
    address = models.TextField()
    country_location = models.ForeignKey(CountryLocation,on_delete=models.CASCADE)


    def __str__(self):return f'{self.country_location.name}'

    
