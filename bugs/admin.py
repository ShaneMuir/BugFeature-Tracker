from django.contrib import admin
from .models import Bug, BugComment, upVotes

# Register your models here.

class BugAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'status', 'creator',
                    'created_date', 'bug_upvotes']
    list_filter = ('status',)
    
class BugCommentAdmin(admin.ModelAdmin):
    list_display = ['bug', 'comment', 'creator', 'created_date']
    list_filter = ('bug', 'creator')

admin.site.register(Bug, BugAdmin)
admin.site.register(BugComment, BugCommentAdmin)
admin.site.register(upVotes)