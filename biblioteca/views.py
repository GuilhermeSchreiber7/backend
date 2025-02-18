from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Livro
from .models import Aluno
from .models import Emprestimo
from .serializer import LivroSerializer
from .serializer import AlunoSerializer
from .serializer import EmprestimoSerializer

# Create your views here.

class LivroViewSet(ModelViewSet):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer

class AlunoViewSet(ModelViewSet):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer

class EmprestimoViewSet(ModelViewSet):
    queryset = Emprestimo.objects.all()
    serializer_class = EmprestimoSerializer
    