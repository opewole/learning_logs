from django.contrib import admin
from learning_logs.models import Topic, Entry

# Register your models here.
class EntryAdmin(admin.ModelAdmin):
    list_display = ('text','date_add','topic')
    list_filter = ('topic',)
    search_fields = ['topic','text']

admin.site.register(Topic)
admin.site.register(Entry,EntryAdmin)
