from django.db import models


class Restaurant (models.Model):
    category_select = (
        ('Restaurant', 'Restaurant'),
        ('"Fast Food"', '"Fast Food"'),
        ('Coffee/Bakery', 'Coffee/Bakery'),
        ('Dessert', 'Dessert'),
    )

    name = models.CharField(max_length=100)
    map_link = models.URLField()
    district = models.CharField(max_length=50)
    description = models.TextField()
    visited = models.BooleanField(default=False)
    rate = models.CharField(max_length=10, blank=True, null=True)
    category = models.CharField(max_length=100, choices=category_select)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['category']
