from django.db import models


class Livro(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=70)
    autor = models.CharField(max_length=70)
    ano_publicacao = models.IntegerField()
    editora = models.CharField(max_length=70)

    def __str__(self):
        return f"{self.titulo} - ({self.autor})"


class Aluno(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=70)
    matricula = models.IntegerField()
    curso = models.CharField(max_length=70)

    def __str__(self):
        return f"{self.nome} - ({self.matricula})"


class Emprestimo(models.Model):
    id = models.AutoField(primary_key=True)
    id_livro = models.ForeignKey(Livro, on_delete=models.PROTECT)
    id_aluno = models.ForeignKey(Aluno, on_delete=models.PROTECT)
    data_emprestimo = models.DateField()
    data_devolucao = models.DateField()

    def __str__(self):
        return f"{self.id_livro} - {self.id_aluno} - {self.data_emprestimo} - {self.data_devolucao}"
