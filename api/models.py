from django.db import models


class File(models.Model):
    file = models.FileField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    processed = models.BooleanField(default=False)
    
    def __str__(self):
        return f"File {self.file.name} uploads at {self.uploaded_at}, processed - {self.processed}"
    
    class Meta:
        ordering = ['-uploaded_at'], ['processed']

