from django.db import models
from django.utils import timezone
from account.models import User
from garden.models import Garden
 
# Create your models here.
def upload_to(instance, filename):
    return 'images/{filename}'.format(filename=filename)

class Complaint(models.Model):
    garden = models.ForeignKey(Garden, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, verbose_name= 'Enter your complaint')
    details = models.TextField(verbose_name= 'Explain in more detail')
    image_url = models.ImageField(upload_to=upload_to, blank=True, null=True)
    date_posted = models.DateTimeField(default=timezone.now)
    status_choices = [
        (1, 'Pending'),
        (2, 'Solved')
    ]
    status = models.IntegerField(choices=status_choices, default=1)
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Feedback(models.Model):
    complaint = models.ForeignKey(Complaint, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(max_length=120)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return '{}-{}'.format(self.complaint.title, str(self.user.name))
