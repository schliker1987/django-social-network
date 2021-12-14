from django.contrib import admin
from django.contrib.auth.models import User

# Register your models here.

#admin.site.register(User)

@admin.register(User)
class User(admin.ModelAdmin):

    def has_change_permission(self, request, obj=None):
        return True

    def has_delete_permission(self, request, obj=None):
        return False

    # to disable view and add you can do this 
    def has_view_permission(self, request, obj=None):
        return True

    def has_add_permission(self, request):
        return True
