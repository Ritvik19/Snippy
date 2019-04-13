from django.contrib import admin
from .models import Snippet
from tinymce.widgets import TinyMCE
from django.db import models

# Register your models here.
class SnippetAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Title/date", {'fields': ["snippet_title", "snippet_type", "snippet_published"]}),
        ("Content", {"fields": ["snippet_content"]})
    ]
    formfield_overrides = {
        models.TextField : {'widget': TinyMCE()}
    }

admin.site.register(Snippet, SnippetAdmin)
