from django.urls import path
from .views import DetailAuthor, DetailBook, DetailBookMember, DetailMember, ListAuthor, ListBook, ListBookMember, ListLibrarian, DetailLibrarian, ListMember
urlpatterns= [
    path('librarian/<int:pk>/',DetailLibrarian.as_view()),
    path('librarian',ListLibrarian.as_view()),
    path('member/<int:pk>/',DetailMember.as_view()),
    path('member',ListMember.as_view()),
    path('author/<int:pk>/',DetailAuthor.as_view()),
    path('author',ListAuthor.as_view()),
    path('book/<int:pk>/',DetailBook.as_view()),
    path('book',ListBook.as_view()),
    path('bookmember/<int:pk>/',DetailBookMember.as_view()),
    path('bookmember',ListBookMember.as_view()),
]