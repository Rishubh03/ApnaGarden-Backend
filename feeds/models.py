from django.db import models
from django.utils.text import slugify
from account.models import User

class Post(models.Model):
	id = models.AutoField(primary_key=True)
	user_id = models.ForeignKey(User, on_delete=models.CASCADE)
	title = models.CharField(max_length=200)
	slug = models.SlugField(max_length=200, unique=True)
	body = models.TextField()
	image = models.ImageField(upload_to='images/', blank = True)
	pub_date = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	def __str__(self):
		return str(self.title)[:20]

	def save(self,*args, **kwargs):
		if not self.slug:
			self.slug = slugify(self.title)
		return super().save(*args, **kwargs)

class PostComment(models.Model):
	id = models.AutoField(primary_key=True)
	post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
	user_id = models.ForeignKey(User, on_delete=models.CASCADE)
	comment = models.TextField()
	pub_date = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	def __str__(self):
		return str(self.comment)[:20]

class PostLike(models.Model):
	id = models.AutoField(primary_key=True)
	post_id = models.OneToOneField(Post, on_delete=models.CASCADE)
	user_id = models.ManyToManyField(User)

	def countLikes(self,post_id):
		obj = self.post_id
		return obj.user_id.count()

	def __str__(self):
		return str(self.post_id.title)[:20]

