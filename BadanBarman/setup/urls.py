from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path("", views.index, name='index'),
    path("more_about/", views.more_about, name='more_about'),
    path("websites/", views.websites, name='websites'),
    path("books/", views.books, name='books'),
    path("research_scholars/", views.research_scholars, name='research_scholars'),
    path("invited_lectures/", views.invited_lectures, name='invited_lectures'),
    path("projects/", views.projects, name='projects'),
    path("awards/", views.awards, name='awards'),
    path("ppts/", views.ppts, name='ppts'),
    path("articles/", views.articles, name='articles'),
    path("conference_papers/", views.conference_papers, name='conference_papers'),
    path("chapters_in_edited_books/", views.chapters_in_edited_books, name='chapters_in_edited_books'),
    path('book_details/<int:pk>/', views.book_details, name='book_details'),
    path('book_buying/<int:pk>/', views.book_buying, name='book_buying'),
    path('periodicals/', views.periodicals, name='periodicals'),
    path('periodical_details/<int:pk>/', views.periodical_details, name='periodical_details'),
]
