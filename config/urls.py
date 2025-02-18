from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from biblioteca.views import LivroViewSet
from biblioteca.views import AlunoViewSet
from biblioteca.views import EmprestimoViewSet

router = DefaultRouter()
router.register(r'livros', LivroViewSet)
router.register(r'alunos', AlunoViewSet)
router.register(r'emprestimos', EmprestimoViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
