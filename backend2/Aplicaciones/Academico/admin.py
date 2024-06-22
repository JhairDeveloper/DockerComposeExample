from django.contrib import admin
from .models import Curso
from .models import Item
from .models import Docentes
# Register your models here.

admin.site.register(Curso)
admin.site.register(Item)
admin.site.register(Docentes)
