from django.contrib import admin
from .models import Choice, Question

# Register your models here.
# This tells admin that Question objects have an admin interface.

class QuestionAdmin(admin.ModelAdmin):
    fieldset = [(None, {'fields': ['question_text']}),
                ('Date information', {'fields': ['pub_date']}),]

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
