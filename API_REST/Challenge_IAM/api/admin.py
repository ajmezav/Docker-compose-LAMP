from django.contrib import admin
from .models import Permission
from .models import User

# Register your models here.

admin.site.register(Permission)
admin.site.register(User)