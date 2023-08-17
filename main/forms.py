from django import forms
from .models import Book, Chapter

class BookForm(forms.ModelForm):
	class Meta:
		model = Book
		fields = '__all__'

		widgets = {
			'name': forms.TextInput(attrs={'class': 'form-control'}),
			'abstract': forms.Textarea(attrs={'class': 'form-control'})
		}


class ChapterForm(forms.ModelForm):
	class Meta:
		model = Chapter
		fields = ['name', 'abstract']

		widgets = {
			'name': forms.TextInput(attrs={'class': 'form-control'}),
			'abstract': forms.Textarea(attrs={'class': 'form-control'})
		}

	