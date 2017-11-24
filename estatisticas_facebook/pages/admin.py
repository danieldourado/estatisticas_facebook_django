from django.contrib import admin
from pages.models import Page, PageInsights

class PageAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)

class PageInsightsAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)

# Register your models here.
admin.site.register(Page,PageAdmin)
admin.site.register(PageInsights, PageInsightsAdmin)
