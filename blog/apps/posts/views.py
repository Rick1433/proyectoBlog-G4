from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy

from .models import Post, Categoria, Comentario


from django.views.generic import DeleteView, UpdateView

from .forms import Formulario_Modificacion


def home_post(request):
    return render(request, "home.html")


def post(request):
    return render(request, "post.html")


def post_realizado(request):
    id_categoria = request.GET.get("id", None)
    antiguedad = request.GET.get("orden", None)
    alfabetico = request.GET.get("orden", None)
    ctx = {}

    if id_categoria:
        posteos = Post.objects.filter(categoria_post=id_categoria)
    else:
        if antiguedad == "asc":
            posteos = Post.objects.all().order_by("fecha_creacion")
        elif alfabetico == "a":
            posteos = Post.objects.all().order_by("titulo")
        elif alfabetico == "z":
            posteos = Post.objects.all().order_by("-titulo")
        else:
            posteos = Post.objects.all().order_by("-fecha_creacion")


    categorias = Categoria.objects.all()
    ctx["posteos"] = posteos
    ctx["categorias"] = categorias
    return render(
        request,
        "posts/post.html",
        {"ctx": ctx, "posteos": posteos, "categorias": categorias},
    )


def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    ctx = {"post": post}
    return render(request, "posts/post_detail.html", ctx)


def comentar_posteo(request):
    comentario = request.POST.get("comentario", None)
    usuario = request.user
    post = request.POST.get("id_post", None)
    posteo = Post.objects.get(id=post)
    setear_comentario = Comentario.objects.create(
        usuario=usuario, post=posteo, texto=comentario
    )
    return redirect("posts:post_detail", post_id=post)


class Borrar_Comentario(DeleteView):
    model = Comentario
    template_name = "comentarios/confirm_delete.html"
    success_url = reverse_lazy("posts:post_realizado")


class Modificar_Comentario(UpdateView):
    model = Comentario
    form_class = Formulario_Modificacion
    template_name = "comentarios/modificar.html"
    success_url = reverse_lazy("posts:post_realizado")
    
