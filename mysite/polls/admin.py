from django.contrib import admin
from .models import Question

# Register your models here.
# This tells admin that Question objects have an admin interface.

class QuestionAdmin(admin.ModelAdmin):
    fiels = ['pub_date', 'question_text']

admin.site.register(Question, QuestionAdmin)
