from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(default='') 
    city = models.CharField(max_length=255)
    address = models.TextField(default='') 
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Company"
        verbose_name_plural = "Companies"

class Vacancy(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(default='') 
    salary = models.FloatField(default=0.0) 
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='vacancies')

    def __str__(self):
        return f"{self.name} ({self.company.name})"

    class Meta:
        verbose_name = "Vacancy"
        verbose_name_plural = "Vacancies"
        
class List(models.Model):
    name=models.CharField(max_length=255)
    description=models.TextField(default='')

    def __str__ (self):
        return self.name 
    
    class Meta :
        verbose_name = "list"
    
    
