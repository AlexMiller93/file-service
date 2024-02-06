from django.contrib import admin
from api.models import File


# Register your models here.
class FileAdmin(admin.ModelAdmin):
    list_display = ('file', 'uploaded_at', 'processed')
    
admin.site.register(File, FileAdmin)