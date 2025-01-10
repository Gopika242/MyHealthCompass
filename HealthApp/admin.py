from django.contrib import admin
from HealthApp.models import ShopCategoryDb,ShopProductDb,MealPlansDb,videoDb,WorkoutPlansDb


# Register your models here.
admin.site.register(ShopCategoryDb)
admin.site.register(ShopProductDb)
admin.site.register(MealPlansDb)
admin.site.register(videoDb)
admin.site.register(WorkoutPlansDb)
