from django.contrib import admin
from .models import Author,Member,Book,BookMember,Librarian

admin.site.register(Author)
admin.site.register(Member)
admin.site.register(Book)
admin.site.register(Librarian)
