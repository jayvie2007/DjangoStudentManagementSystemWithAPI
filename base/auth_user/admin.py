from django.contrib import admin
from .models import CustomUser, UserData

# Register your models here.
admin.site.register(CustomUser)

@admin.register(UserData)
class UserDataAdmin(admin.ModelAdmin):
    readonly_fields = ('student_number',)