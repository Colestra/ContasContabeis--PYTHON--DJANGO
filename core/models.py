from django.db import models

from stdimage .models import StdImageField
#SIGNALS

from django.db.models import signals
from django.template.defaultfilters import slugify

class Base(models.Model):
    criado = models.DateField('Data de Criação', auto_now=True)
    modificado = models.DateField('Data de Atualização', auto_now=True)
    ativo = models.BooleanField('Ativo?', default=True)

    class Meta:
        abstract = True

class EmpresaNome(Base):
    nome = models.CharField('Nome', max_length=100)
    cnpj = models.CharField('CNPJ', max_length=100)
    slug = models.SlugField('Slug', max_length=100, blank=True, editable=False)

    def __str__(self):
        return self.nome

def empresanome_pre_save (signal, instance, sender, **kwargs):
    instance.slug = slugify(instance.nome)

signals.pre_save.connect(empresanome_pre_save,sender=EmpresaNome)




class Contas(Base):
    codigo = models.CharField('Codigo', max_length=100)
    descricao = models.CharField('Descrição',max_length=100)
    credito = models.CharField('Credito', max_length=45)
    empresa = models.IntegerField('Empresa')
    iva = models.CharField('IVA', max_length=100, null=True)
    slugc = models.SlugField('Slug', max_length=100, blank=True, editable=False)



    def __str__(self):
        return self.descricao

def contas_pre_save (signal, instance, sender, **kwargs):
    instance.slug = slugify(instance.descricao)
signals.pre_save.connect(contas_pre_save,sender=Contas)