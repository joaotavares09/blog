from django import forms
from .models import Noticia, Area

class PostForm(forms.ModelForm):
	class Meta:
		model = Noticia
		fields = ('author','area', 'photo', 'title', 'text',)
class AreaForm(forms.ModelForm):
	class Meta:
		model = Area
		fields = ('descricao', 'cor', 'status',)