from django.db import models


class Theme(models.Model):
    name = models.CharField(max_length=256)
    
    
    def __str__(self) -> str:
        return self.name



class Word(models.Model):
    korean = models.CharField(max_length=256)
    uzbek = models.CharField(max_length=256)
    
    theme = models.ForeignKey(Theme, on_delete=models.CASCADE, related_name='words')
    
    
    
    def __str__(self) -> str:
        return self.uzbek    