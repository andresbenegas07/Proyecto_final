#from curses import nocbreak
from django.shortcuts import render
from AppCoder.models import Curso, Avatar   
from AppCoder.models import Alumno
from AppCoder.models import Profesor 
from django.http import HttpResponse
from django.template import loader
from AppCoder.forms import Curso_formulario, UserEditForm
from AppCoder.forms import Alumno_formulario 
from AppCoder.forms import Profesor_formulario
from django.contrib.auth.forms import AuthenticationForm , UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required  




def inicio(request):
    avatares = Avatar.objects.filter(user=request.user.id)
    return render(request, "padre.html", {"url":avatares[0].imagen.url} )



def ver_cursos(request):
    cursos = Curso.objects.all()
    avatares = Avatar.objects.filter(user=request.user.id)
    
    return render(request , "cursos.html", {"url":avatares[0].imagen.url , "cursos": cursos })


@login_required
def ver_profesor(request):
    profesor = Profesor.objects.all()
    avatares = Avatar.objects.filter(user=request.user.id)
    
    return render(request , "profesor.html", {"url":avatares[0].imagen.url , "profesor": profesor })



def ver_alumno(request):
    alumno = Alumno.objects.all()
    avatares = Avatar.objects.filter(user=request.user.id)
    
    return render(request , "alumnos.html", {"url":avatares[0].imagen.url , "alumno": alumno })





def curso_formulario(request):
    avatares = Avatar.objects.filter(user=request.user.id)
    if request.method == "POST":
        mi_formulario = Curso_formulario(request.POST)

        if mi_formulario.is_valid():
           avatares = Avatar.objects.filter(user=request.user.id)
           datos = mi_formulario.cleaned_data 
           curso = Curso(nombre=request.POST["nombre"], camada=request.POST["camada"])
           curso.save()
           return render(request, "formulario.html", {"url":avatares[0].imagen.url})
    
    
    return render(request, "formulario.html", {"url":avatares[0].imagen.url})



def alumnos(request):
    avatares = Avatar.objects.filter(user=request.user.id)
    
    return render(request , "alumnos.html", {"url":avatares[0].imagen.url})


def alumno_formulario(request):
    avatares = Avatar.objects.filter(user=request.user.id)
    if request.method == "POST":

        mi_formulario_alumno = Alumno_formulario(request.POST)

        if mi_formulario_alumno.is_valid():
           avatares = Avatar.objects.filter(user=request.user.id)
           datos = mi_formulario_alumno.cleaned_data 
           alumno = Alumno(nombre=datos["nombre"], camada=datos["camada"])
           alumno.save()
           return render(request, "alumno_form.html", {"url":avatares[0].imagen.url})
    
    
    return render(request, "alumno_form.html", {"url":avatares[0].imagen.url}) 





def profesor(request):
    avatares = Avatar.objects.filter(user=request.user.id)
    
    return render(request , "profesor.html", {"url":avatares[0].imagen.url})



def profesor_formulario(request):
    avatares = Avatar.objects.filter(user=request.user.id)
    if request.method == "POST":

        mi_formulario_profesor = Profesor_formulario(request.POST)

        if mi_formulario_profesor.is_valid():
           avatares = Avatar.objects.filter(user=request.user.id)
           datos = mi_formulario_profesor.cleaned_data 
           profesor = Profesor(nombre=datos["nombre"], camada=datos["camada"])
           profesor.save()
           return render(request, "profesor_form.html",{"url":avatares[0].imagen.url}   )
    
    
    return render(request, "profesor_form.html",{"url":avatares[0].imagen.url}) 






def buscar_curso(request):

    return render(request, "buscar_curso.html")



def buscar(request):
     
    if request.GET["nombre"]:
        nombre = request.GET["nombre"]
        cursos = Curso.objects.filter(nombre__icontains= nombre)
        return render(request,"resultado_busqueda.html", {"cursos":cursos})
    else:    
        return HttpResponse("Ingrese el nombre del curso")




def buscar_alumno_r(request):
    avatares = Avatar.objects.filter(user=request.user.id)
    
    return render(request , "buscar_alumno_r.html", {"url":avatares[0].imagen.url})


def buscar_alumno(request):

    if request.GET["nombre"]:
        nombre = request.GET["nombre"]
        alumno = Alumno.objects.filter(nombre__icontains= nombre)
        return render(request,"resultado_busqueda_alumno.html", {"alumno":alumno})
    else:    
        return HttpResponse("Ingrese el nombre del alumno")



####



def elimina_curso(request,id):
    curso = Curso.objects.get(id=id)
    curso.delete()
    cursos = Curso.objects.all()

    

    return render(request , "cursos.html" , {"cursos":cursos})

def elimina_alumno(request,id):
    alumno = Alumno.objects.get(id=id)
    alumno.delete()
    alumnos = Alumno.objects.all()

    

    return render(request , "alumnos.html" , {"alumno":alumno})

def elimina_profesor(request,id):
    profesor = Profesor.objects.get(id=id)
    profesor.delete()
    profesores = Profesor.objects.all()

    

    return render(request , "profesor.html" , {"profesor":profesor})



def editar(request,id):

    curso = Curso.objects.get(id=id)
    avatares = Avatar.objects.filter(user=request.user.id)
    if request.method == "POST":

        mi_formulario = Curso_formulario( request.POST )
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            curso.nombre = datos["nombre"]
            curso.camada = datos["camada"]
            curso.save()

            curso = Curso.objects.all()

            return render(request , "cursos.html" , {"cursos":curso, "url":avatares[0].imagen.url})


        
    else:
        mi_formulario = Curso_formulario(initial={"nombre":curso.nombre , "camada":curso.camada})
        avatares = Avatar.objects.filter(user=request.user.id)
    return render( request , "editar_curso.html" , {"mi_formulario": mi_formulario , "curso":curso, "url":avatares[0].imagen.url})






def editar_alumno(request,id):

    alumno = Alumno.objects.get(id=id)
    avatares = Avatar.objects.filter(user=request.user.id)
    if request.method == "POST":

        mi_formulario = Alumno_formulario(request.POST)
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            alumno.nombre = datos["nombre"]
            alumno.camada = datos["camada"]
            alumno.save()

            alumno = Alumno.objects.all()

            return render(request , "alumnos.html" , {"alumnos":alumno})


        
    else:
        mi_formulario = Alumno_formulario(initial={"nombre":alumno.nombre , "camada":alumno.camada})
        avatares = Avatar.objects.filter(user=request.user.id)
    
    return render( request , "editar_alumno.html" , {"mi_formulario": mi_formulario , "alumno":alumno, "url":avatares[0].imagen.url })


def editar_profesor(request,id):

    profesor = Profesor.objects.get(id=id)
    avatares = Avatar.objects.filter(user=request.user.id)
    if request.method == "POST":

        mi_formulario = Profesor_formulario( request.POST )
        
        
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            
            profesor.nombre = datos["nombre"]
            profesor.camada = datos["camada"]
            profesor.save()

            profesor = Curso.objects.all()

            return render(request , "profesor.html" , {"profesor":profesor, "url":avatares[0].imagen.url})


        
    else:

        mi_formulario = Profesor_formulario(initial={"nombre":profesor.nombre , "camada":profesor.camada})
        avatares = Avatar.objects.filter(user=request.user.id) 
    return render( request , "editar_profesor.html" , {"mi_formulario": mi_formulario , "profesor":profesor, "url":avatares[0].imagen.url })




def login_request(request):

    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():

            usuario = form.cleaned_data.get("username")
            contra = form.cleaned_data.get("password")

            user = authenticate(username=usuario , password=contra)

            if user is not None:
                login(request , user )
                avatares = Avatar.objects.filter(user=request.user.id)
                return render( request , "inicio.html" , {"url":avatares[0].imagen.url})
            else:
                return HttpResponse(f"Usuario no encontrado")
        else:
            return HttpResponse(f"FORM INCORRECTO {form}")


    form = AuthenticationForm()
    return render( request , "login.html" , {"form":form})




def register(request):
    
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        avatares = Avatar.objects.filter(user=request.user.id)
        if form.is_valid():
            form.save()
            avatares = Avatar.objects.filter(user=request.user.id)
            return HttpResponse("Usuario creado", {"url":avatares[0].imagen.url})

    else:
        form = UserCreationForm()
        avatares = Avatar.objects.filter(user=request.user.id)
    return render(request , "registro.html" , {"form":form, "url":avatares[0].imagen.url })




def editarPerfil(request):

    usuario = request.user

    if request.method == "POST":
        
        mi_formulario = UserEditForm(request.POST)

        if mi_formulario.is_valid():

            informacion = mi_formulario.cleaned_data
            usuario.email = informacion["email"]
            password = informacion["password1"]
            usuario.set_password(password)
            usuario.save()
            return render(request , "inicio.html")

    else:
        miFormulario = UserEditForm(initial={"email":usuario.email})
    
    return render( request , "editar_perfil.html", {"miFormulario":miFormulario, "usuario":usuario})
