from django.db import models
from datetime import datetime

# Create your models here.
class Snippet(models.Model):
    snippet_title = models.CharField(max_length = 200)
    snippet_type = models.CharField(max_length = 20)
    snippet_content = models.TextField()
    snippet_published = models.DateTimeField('date published', default=datetime.now())

    def __str__(self):
        return self.snippet_title + '-' + self.snippet_type
