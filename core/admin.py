from django.contrib import admin


from .models import EmpresaNome, Contas

@admin.register(EmpresaNome)
class EmpresaNomeAdmin (admin.ModelAdmin):
    list_display = ('nome','cnpj','criado', 'modificado','ativo')

@admin.register(Contas)
class ContasNomeAdmin (admin.ModelAdmin):
    list_display = ('codigo','descricao','credito','empresa','criado', 'modificado','ativo')

''