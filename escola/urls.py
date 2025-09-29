from django.urls import path, include
from escola import views
from rest_framework import routers


app_name = 'escola'

router = routers.DefaultRouter()

router.register('alunos', views.AlunosViewSet, basename='Alunos')
router.register('cursos', views.CursoViewSet, basename='Cursos')
router.register('matricula', views.MatriculasViewSet, basename='Matricula')

urlpatterns = [
    path('', include(router.urls)),
    path('aluno/<int:pk>/matriculas/', views.ListaMatriculasAluno.as_view()),
    path('curso/<int:pk>/matriculas/', views.ListaAlunosMatriculados.as_view())
]
