from django.db import models

    
class Trainer(models.Model):
    nametrainer = models.CharField(max_length=30, null=False)
    lastname = models.CharField(max_length=30, null=False)
    level = models.IntegerField(null=False)
    birthday = models.DateField(null=False)
    picture = models.ImageField(upload_to='pokemon_pictures/', null=True, blank=True)
    def __str__(self):
        return self.nametrainer
        

class Pokemon(models.Model):
    POKEMON_TYPES = [
        ('Acero', '🛡️ Acero'),
        ('Agua', '💧 Agua'),
        ('Eléctrico', '⚡ Eléctrico'),
        ('Fantasma', '👻 Fantasma'),
        ('Fuego', '🔥 Fuego'),
    ]
    name = models.CharField(max_length=100, null=False)
    type = models.CharField(max_length=140, null=False, choices=POKEMON_TYPES)
    weight = models.IntegerField(null=False)
    height = models.IntegerField(null=False)
    picture = models.ImageField(upload_to='pokemon_pictures/', null=True, blank=True)
    
    def __str__(self):
        return self.name
    

        
    