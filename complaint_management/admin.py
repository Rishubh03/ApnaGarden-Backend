from django.contrib import admin
from .models import Complaint, Feedback
# Register your models here.

@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    list_display = ('title','garden','user_id','date_posted','status')
    ordering = ['date_posted']


admin.site.register(Feedback)