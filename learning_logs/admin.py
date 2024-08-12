from django.contrib import admin
from .models import Topic, Entry


class TopicAdmin(admin.ModelAdmin):
    list_display = ('text', 'date_added')


class EntryAdmin(admin.ModelAdmin):
    list_display = ('topic', 'date_added', 'get_short_description')


    def get_short_description(self, obj):
        return obj.get_short_description()
    get_short_description.short_description = 'Описание'


admin.site.register(Topic, TopicAdmin)
admin.site.register(Entry, EntryAdmin)