from django.shortcuts import render
from django.views import generic
from catalog.models import Author,Book,BookInstance,Genre
# Create your views here.


def index(request):
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    num_authors = Author.objects.count()

    context = {
        'num_books': num_books,
        'num_instances':num_instances,
        'num_instances_available':num_instances_available,
        'num_authors':num_authors,
    }

    return render(request,'index.html',context=context)

class BookListView(generic.ListView):
    model = Book

    def get_context_data(self,**kwargs):
        context = super(BookListView,self).get_context_data(**kwargs)
        context['some_data'] = 'This is just some data'
        return context



class BookDetailView(generic.DetailView):
    model = Book
