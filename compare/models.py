from django.db import models

class Code1(models.Model):
    code1_text = models.CharField(max_length=512)
    
class Code2(models.Model):
    code2_text = models.CharField(max_length=512)
    
class similarity(models.Model):
    similarity_int = models.IntegerField(default=0)