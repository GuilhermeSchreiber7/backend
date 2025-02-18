from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Livro
from .models import Aluno
from .models import Emprestimo

admin.site.register(Livro)
admin.site.register(Aluno)
admin.site.register(Emprestimo)