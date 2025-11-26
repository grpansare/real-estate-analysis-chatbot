from django.contrib import admin
from .models import RealEstateData


@admin.register(RealEstateData)
class RealEstateDataAdmin(admin.ModelAdmin):
    list_display = ['area', 'year', 'price_per_sqft', 'demand_score', 'transactions']
    list_filter = ['area', 'year']
    search_fields = ['area']
    ordering = ['area', 'year']
