from django.contrib import admin
from .models import Questions, Choice

admin.site.site_header = "Pollstar Admin"
admin.site.site_title = "Pollstar Admin Area"
admin.site.index_title = "Welcome to Pollstar Admin Area"

class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['question_text']}), ('Date Information', {
        'fields': ['pub_date'], 'classes': ['collapse']}), ]
    inlines = [ChoiceInLine]
  
  
admin.site.register(Question, QuestionAdmin)
