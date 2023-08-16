from django.shortcuts import render
from django.views import generic
from django.http import HttpResponseRedirect
from django.views.generic.edit import FormView
from django.urls import reverse

from .models import Book
from .forms import BookForm

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
		return HttpResponseRedirect(reverse('dashboard'))
	return render(request, 'add-book.html', {'form': form})