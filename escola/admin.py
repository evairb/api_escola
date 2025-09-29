from django.contrib import admin
from escola.models import Aluno, Curso, Matricula


@admin.register(Aluno)
class Alunos(admin.ModelAdmin):
    list_display = ('id', 'nome', 'rg', 'cpf', 'data_nascimento')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)
    list_per_page = 20


@admin.register(Curso)
class Cursos(admin.ModelAdmin):
    list_display = (
        'id', 'codigo_curso', 'descricao', 'nivel'
    )
    list_display_links = ('id', 'descricao')
    search_fields = ('codigo_curso', 'descricao')
    list_per_page = 20


@admin.register(Matricula)
class Matriculas(admin.ModelAdmin):
    list_display = ('id', 'aluno', 'curso', 'periodo')
    list_display_links = ('id', 'aluno')
    search_fields = ('aluno', 'curso', 'periodo')
    list_per_page = 20
