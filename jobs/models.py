from django.db import models
from django import forms

# Create your models here.

class Tag(models.Model):
    title = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.title}"

class Job(models.Model):
    name = models.CharField(max_length=100)
    tags = models.ManyToManyField(Tag)
    place = models.CharField(max_length=200)
    mission = models.CharField(max_length=1000)
    email = models.EmailField(max_length=254)
    date = models.DateTimeField(auto_now_add=True, blank=True)

    def get_tags(self):
        return ",".join([str(p) for p in self.tags.all()])

    def __str__(self):
        return f"{self.name}"

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        exclude = ('tags', 'place', 'mission', 'email', 'date')