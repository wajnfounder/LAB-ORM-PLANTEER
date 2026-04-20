from django.db import models

class Plant(models.Model):

    class Category(models.TextChoices):
       TR = 'TR', 'Tropical'
       SU = 'SU', 'Succulents'
       HE = 'HE', 'Herbs'
       FE = 'FE', 'Ferns'
       FL = 'FL', 'Flowering'
       TRS = 'TRS', 'Trees'

    name = models.CharField(max_length=200)
    about = models.TextField()
    used_for = models.TextField()
    image = models.ImageField(upload_to='plants/', null=True, blank=True)
    category = models.CharField(max_length=20, choices=Category.choices)
    is_edible = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Comment(models.Model):
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.plant.name}"