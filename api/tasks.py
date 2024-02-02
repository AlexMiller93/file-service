from celery import shared_task
from .models import File

@shared_task
def process_file(file_id):
    file = File.objects.get(id=file_id)
    
    # обрабоотка файлов
    
    file.processed = True
    file.save()