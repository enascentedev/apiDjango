from django.contrib import admin

# importando models
from .models import User
admin.site.register(User)
#modelo não sera usado admin.site.register(UserTasks)



# Register your models here.
