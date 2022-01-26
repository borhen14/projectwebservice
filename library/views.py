from django.shortcuts import render


# Create your views here.
from rest_framework import generics
from .models import BookMember, Librarian,Book,Author,Member
from .serializers import BookMemberSerializer, LibrarianSerializer,BookSerializer,AuthorSerializer,MemberSerializer

class ListLibrarian(generics.ListCreateAPIView):
    queryset= Librarian.objects.all()
    serializer_class = LibrarianSerializer

class DetailLibrarian(generics.RetrieveUpdateDestroyAPIView):
    queryset = Librarian.objects.all()
    serializer_class= LibrarianSerializer

class ListBook(generics.ListCreateAPIView):
    queryset= Book.objects.all()
    serializer_class = BookSerializer

class DetailBook(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class= BookSerializer

class ListAuthor(generics.ListCreateAPIView):
    queryset= Author.objects.all()
    serializer_class = AuthorSerializer

class DetailAuthor(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class= AuthorSerializer

class ListMember(generics.ListCreateAPIView):
    queryset= Member.objects.all()
    serializer_class = MemberSerializer

class DetailMember(generics.RetrieveUpdateDestroyAPIView):
    queryset = Member.objects.all()
    serializer_class= MemberSerializer

class ListBookMember(generics.ListCreateAPIView):
    queryset= BookMember.objects.all()
    serializer_class = BookMemberSerializer

class DetailBookMember(generics.RetrieveUpdateDestroyAPIView):
    queryset = BookMember.objects.all()
    serializer_class= BookMemberSerializer