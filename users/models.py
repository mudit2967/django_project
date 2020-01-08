from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Profile(models.Model):
	user= models.OneToOneField(User, on_delete=models.CASCADE)
	image=models.ImageField(default='default.jpg', upload_to='profile_pics')

	def __str__(self):
		return f'{self.user.username} Profile'



class Private(models.Model):
	user= models.OneToOneField(User, on_delete=models.CASCADE)
	title=models.CharField(max_length=100)
	content=models.TextField()
	date_posted=models.DateTimeField(default=timezone.now)

	def __str__(self):
		return f'{self.user.username}"s Private Notes'
