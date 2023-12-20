from django.urls import path

from . import views

app_name = "posts"

urlpatterns = [
    path("", views.home_post, name="home_posts"),
    path("categorias", views.categorias_post, name="categorias_posts"),
    path("posteos", views.post_realizado, name="post_realizado"),
    path("post_detail/<int:post_id>", views.post_detail, name="post_detail"),
    path("comentario", views.comentar_posteo, name="comentar"),
    # url borrar comentario
    path(
        "Borrar/<int:pk>",
        views.Borrar_Comentario.as_view(),
        name="borrar_comentario",
    ),
    path(
        "Modificar/<int:pk>",
        views.Modificar_Comentario.as_view(),
        name="modificar_comentario",
    ),
]