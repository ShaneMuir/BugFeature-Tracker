from django.contrib import admin
from .models import Bug, BugComment

# Register your models here.

class BugAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'status', 'creator',
                    'created_date', 'bug_upvotes']
    list_filter = ('status',)
    
class BugCommentAdmin(admin.ModelAdmin):
    list_display = ['bug', 'comment', 'creator']
    list_filter = ('bug',)

admin.site.register(Bug, BugAdmin)
admin.site.register(BugComment, BugCommentAdmin)