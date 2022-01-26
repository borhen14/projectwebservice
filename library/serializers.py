
from rest_framework import serializers
from .models import BookMember, Librarian,Book,Author,Member

class LibrarianSerializer(serializers.ModelSerializer):
    class Meta:
        model = Librarian
        fields = '__all__'
    
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
    
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'
    
class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = '__all__'
class BookMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookMember
        fields = '__all__'
    