from django.contrib import admin

from garden.models import Garden, Ward, Ratings


# Register your models here.
@admin.register(Ward)
class gardenAdmin(admin.ModelAdmin):
    list_display = ['id','ward_name', 'ward_description']
    ordering = ['id']


@admin.register(Garden)
class gardenAdmin2(admin.ModelAdmin):
    list_display = ['garden_name', 'open_time', 'close_time', 'ward_id']
    ordering = ['garden_name']

@admin.register(Ratings)
class ratingsAdmin(admin.ModelAdmin):
    list_display = ['id', 'rating', 'comment', 'garden_id','user']
    ordering = ['created_at']

    def user(self, obj):
        return obj.user_id.firstname + obj.user_id.lastname



