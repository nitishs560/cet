from django.contrib import admin
from .models import physics, chemistry, math, student, question_answers, results

# Register your models here.

admin.site.register(physics)
admin.site.register(chemistry)
admin.site.register(math)
admin.site.register(student)
admin.site.register(question_answers)
admin.site.register(results)
