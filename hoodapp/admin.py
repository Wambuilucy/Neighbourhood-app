from django.contrib import admin
from .models import User, Post , Business, Neighbourhood, Profile

admin.site.register(Post)
admin.site.register(Business)
admin.site.register(Neighbourhood)
admin.site.register(Profile)