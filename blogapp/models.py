from django.db import models
from datetime import datetime  


class Posts(models.Model):
	author = models.CharField(max_length = 40)
	title = models.CharField(max_length = 120)
	text = models.TextField()
	time = models.DateTimeField(default=datetime.now, editable=False,)

