from django.db import models


class RealEstateData(models.Model):
    """Model to store real estate data from Excel file"""
    year = models.IntegerField()
    area = models.CharField(max_length=200)
    price_per_sqft = models.DecimalField(max_digits=10, decimal_places=2)
    demand_score = models.IntegerField()
    avg_size_sqft = models.IntegerField()
    transactions = models.IntegerField()
    
    class Meta:
        ordering = ['area', 'year']
        verbose_name = 'Real Estate Data'
        verbose_name_plural = 'Real Estate Data'
    
    def __str__(self):
        return f"{self.area} - {self.year}"
