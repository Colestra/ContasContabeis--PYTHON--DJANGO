
from django.urls import path
from .views import index, empresa, contas, speech_to_text

urlpatterns = [
    path('', index, name='index'),
    path('empresa/', empresa, name='empresa'),
    path('contas/<int:pk>', contas, name='contas'),
    path('speech_to_text/', speech_to_text, name='speech_to_text')

]

