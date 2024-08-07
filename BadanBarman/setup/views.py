from django.shortcuts import render
from django.http import HttpResponse
from .models import Websites,Research_Scholars, Invited_Lectures, Projects, Awards, Presentation, Articles_In_Journals, Chapters_In_Edited_Books, Books, Periodicals

# Create your views here.
def index(request):
    return render(request, 'index.html')


def more_about(request):
    return render(request, 'more_about.html')


def websites(request):
    websites = Websites.objects.all()
    return render(request, 'websites.html',{ 'websites': websites })


def research_scholars(request):
    research_scholars = Research_Scholars.objects.all()  
    return render(request, 'research_scholars.html',{ 'scholars': research_scholars })


def invited_lectures(request):
    invited_lectures = Invited_Lectures.objects.all()
    return render(request, 'invited_lectures.html',{ 'lectures': invited_lectures })


def projects(request):
    projects = Projects.objects.all()
    return render(request, 'projects.html',{ 'projects': projects })


def awards(request):
    awards = Awards.objects.all().order_by("-id")
    return render(request, 'awards.html',{ 'awards': awards })


def ppts(request):
    presentations = Presentation.objects.all().order_by("id")
    return render(request, 'ppts.html', { 'presentations': presentations })


def articles(request):
    articles_list = Articles_In_Journals.objects.all().order_by("-id")
    return render(request, 'articles_in_journals.html', {'articles': articles_list})


#! The page is under maintenance...
def conference_papers(request):
    # conference_papers = Articles_In_Journals.objects.all().order_by("-id")    , {'cpapers': conference_papers}
    return render(request, 'conference_papers.html')


def chapters_in_edited_books(request):
    chapters_in_edited_books = Chapters_In_Edited_Books.objects.all().order_by("-id")
    return render(request, 'chapters_in_edited_books.html', {'chapters': chapters_in_edited_books})


def books(request):
    books = Books.objects.all().order_by("-priority")
    return render(request, 'books.html',{'books': books})


def book_details(request, pk):
    book_details = Books.objects.get(pk=pk)
    if book_details.original_price>book_details.sale_price:
        calc = { "save" : book_details.original_price - book_details.sale_price, "percentage" : int(((book_details.original_price - book_details.sale_price)/book_details.original_price)*100)}
    else:
        calc = { "save" : 0, "percentage" : 0}
    return render(request, './slug/book_details.html',{'details': book_details, 'calculation' : calc})



def book_buying(request, pk):
    buying_details = Books.objects.get(pk=pk)
    return render(request, './slug/book_buying.html',{'buying': buying_details, 'pk':pk})



def periodicals(request):
    periodicals = Periodicals.objects.all().order_by("-id")
    return render(request, 'periodicals.html',{'periodicals': periodicals})


def periodical_details(request, pk):
    periodical_details = Periodicals.objects.get(pk=pk)
    return render(request, './slug/periodical_details.html',{'details': periodical_details})