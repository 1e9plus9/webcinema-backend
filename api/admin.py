from django.contrib import admin
from .models import User, Comment, Movie, Genre

# Register your models here.
admin.site.register(User)
admin.site.register(Comment)
admin.site.register(Movie)
admin.site.register(Genre)
