from django.shortcuts import render
from django.contrib import messages
from .forms import EmpresaNomeModelForm
from .models import EmpresaNome, Contas
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.template import loader
import speech_recognition as sr
import wikipedia

def index(request):
    empresas = EmpresaNome.objects.all()
    context = {
        'empresas': empresas
    }
    return render(request, 'index.html', context)

def empresa(request):
    if str(request.user) != 'AnonymousUser':
        if str(request.method) == 'POST':
            form = EmpresaNomeModelForm(request.POST)
            if form.is_valid():

                form.save()

                messages.success(request, 'Empresa salvo com sucesso!')
                form = EmpresaNomeModelForm()
            else:
                messages.error(request, 'Erro ao salvar empresa')
        else:
            form = EmpresaNomeModelForm()
        context = {
            'form': form
        }
        return render(request, 'empresa.html', context)
    else:
        return redirect('index')


def contas(request, pk):
    empr = get_object_or_404(EmpresaNome, id=pk)
    #print(f'PK: {pk}')
    contacontabil = Contas.objects.filter(empresa=pk)
    data = request.POST.get('record')

    # get audio from the microphone
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak:")
        audio = r.listen(source)

    try:
        output = " " + r.recognize_google(audio)
    except sr.UnknownValueError:
        output = "Could not understand audio"
    except sr.RequestError as e:
        output = "Could not request results; {0}".format(e)
    data = output
    context = {
        'empresanome': empr,
        'contacontabil': contacontabil,
        'data':data,

    }

    return render(request, 'contas.html', context)


def error404(request, ex):
    template = loader.get_template('404.html')
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf8', status=404)

def error500(request):
    template = loader.get_template('500.html')
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf8', status=500)

def speech_to_text(request):
    data = request.POST.get('record')


    # get audio from the microphone
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak:")
        audio = r.listen(source)

    try:
        output = " " + r.recognize_google(audio)
    except sr.UnknownValueError:
        output = "Could not understand audio"
    except sr.RequestError as e:
        output = "Could not request results; {0}".format(e)
    data =output

    return render(request,'speech_to_text.html',{'data':data})
