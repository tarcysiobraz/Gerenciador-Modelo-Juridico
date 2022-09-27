from django import forms
from peticao.models import Peticao
from django_summernote.widgets import SummernoteWidget


class PeticaoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PeticaoForm, self).__init__(*args, **kwargs)
   
    class Meta:
        model = Peticao
        fields = ['body', 'name', 'category', 'description']
        widgets = {
            'body': SummernoteWidget(),
            'name': forms.TextInput(attrs={'placeholder': 'nome da Petição',}),
            'category':forms.TextInput(attrs={'placeholder': 'nome da categoria da petição',}),
            'description':forms.TextInput(attrs={'placeholder': 'descrição da petição'}),

        }
