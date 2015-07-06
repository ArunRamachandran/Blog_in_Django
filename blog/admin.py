from django.contrib import admin

# Register your models here.
from .models import Post

admin.site.register(Post) # Register the model with admin,To make our blog visible on the admin page
 