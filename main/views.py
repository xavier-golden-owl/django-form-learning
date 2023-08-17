from django.shortcuts import render
from django.views import generic
from django.http import HttpResponseRedirect
from django.views.generic.edit import FormView
from django.urls import reverse
from django.contrib import messages

from .models import Book, Chapter
from .forms import BookForm, ChapterForm

# Create your views here.
class DashboardView(generic.ListView):
	model = Book
	template_name = 'dashboard.html'

	context_object_name = 'books'

class BookDetailView(generic.DetailView):
	model = Book
	template_name = 'detail.html'


def addBook(request):
	form = BookForm(request.POST or None)
	if form.is_valid():
		form.save()
		messages.success(request, f'Add book {form.cleaned_data["name"]} successfully')

		return HttpResponseRedirect(reverse('dashboard'))
	return render(request, 'add-book.html', {'form': form})


class ChapterDetailView(generic.DetailView):
	model = Chapter
	template_name = 'chapter-detail.html'

	context_object_name = 'chapter'


def addChapter(request, pk):
	book = Book.objects.get(pk=pk)

	form = ChapterForm(request.POST or None)
	if form.is_valid():
		chapter = form.save(commit=False)
		chapter.book = book
		chapter.save()
		messages.success(request, f'Add chapter {chapter.name} successfully')
		return HttpResponseRedirect(reverse('detail', args=[pk]))
	
	return render(request, 'add-chapter.html', {'form': form, 'book': book})