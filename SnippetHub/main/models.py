from django.db import models

# Create your models here.
class Snippet(models.Model):
    snippet_title = models.CharField(max_length = 200)
    snippet_content = models.TextField()
    snippet_published = models.DateTimeField('date published')

    def __str__(self):
        return self.snippet_title
