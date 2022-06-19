from django.db import models

class Code1(models.Model):
    code1_text = models.CharField(max_length=512)
    
    def __str__(self):
        return self.code1_text
    
class Code2(models.Model):
    code2_text = models.CharField(max_length=512)
    
    def __str__(self):
        return self.code2_text
    
class similarity(models.Model):
    similarity_int = models.IntegerField(default=0)
    
    def __str__(self):
        return self.similarity_int