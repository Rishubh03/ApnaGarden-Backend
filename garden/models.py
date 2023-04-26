from enum import auto
from pydoc import describe
from tkinter import CASCADE
from django.db import models
import datetime
from account.models import User

def upload_to(instance, filename):
    return 'images/{filename}'.format(filename=filename)

class Ward(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    ward_name = models.CharField(max_length=100, unique=True)
    ward_description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.ward_name

    class Meta:
        verbose_name_plural = "Wards"


class Garden(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    garden_name = models.CharField(max_length=100)
    garden_description = models.TextField(blank=True)
    open_time = models.TimeField(default=datetime.time(5, 00))
    close_time = models.TimeField(default=datetime.time(20, 00))
    address = models.TextField()
    ward_id = models.ForeignKey(Ward,on_delete=models.CASCADE)
    image_url = models.ImageField(upload_to=upload_to, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.garden_name

    class Meta:
        verbose_name_plural = "Gardens"

class Ratings(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    rating = models.IntegerField()
    comment = models.TextField(blank=True)
    image_url = models.ImageField(upload_to=upload_to, blank=True, null=True)
    garden_id = models.ForeignKey('Garden', on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    rated = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def calculate_rating(garden_id):
        try:
            rating_obj = Ratings.objects.filter(garden_id=garden_id)
            total_rating = 0
            total_count = rating_obj.count()
            print(rating_obj)
            for rating in rating_obj:
                total_rating += rating.rating
        
            return round(total_rating/total_count,1)
        except ZeroDivisionError:
            return 0
    
    def save(self, *args, **kwargs):
        if not self.rated:
            self.rated = True
        super(Ratings, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Ratings"