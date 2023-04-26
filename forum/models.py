from django.db import models
from account.models import User
# Create your models here.

"""
Forum: This model represents a forum category. It has a name, description, and timestamps for creation and update.

"""


class Forum(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


"""
Thread: This model represents a thread or topic inside a forum. It has a title, content, timestamps for creation and update, and foreign keys to the user who created the thread and the forum it belongs to.

"""


class Thread(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    forum = models.ForeignKey(Forum, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


""" 
Post: This model represents a post or comment inside a thread. It has a content, timestamps for creation and update, and foreign keys to the user who created the post and the thread it belongs to.
"""


class ThreadPost(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE)

    def __str__(self):
        return self.content
