from django.contrib import admin
from .models import Feature, FeatureComment

# Register your models here.
class FeatureAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'status', 'creator',
                    'created_date', 'feature_upvotes']
    list_filter = ('status',)
    
class FeatureCommentAdmin(admin.ModelAdmin):
    list_display = ['feature', 'comment', 'creator', 'created_date']
    list_filter = ('feature', 'creator')

admin.site.register(Feature, FeatureAdmin)
admin.site.register(FeatureComment, FeatureCommentAdmin)