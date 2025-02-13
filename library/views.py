from django.shortcuts import render
from .models import *
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from .serializers import *
# Create your views here.
from django.http import JsonResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

def view_all_books(request):
   all_books = Book.objects.all()
   return render(request, 'all_books.html', {'books': all_books})

def view_single_book(request, book_id):
   single_book = get_object_or_404(Book, id=book_id)
   return render(request, 'single_book.html', {'book': single_book})

def view_books_by_category(request, category):
   books_by_category = Book.objects.filter(category=category)
   return render(request, 'books_by_category.html', {'books': books_by_category})

def api_add(request):
   num1 = float(request.GET.get('num1', 1)) #1 is the default
   num2 = float(request.GET.get('num2', 1))
   added = num1 + num2

   resp_dict = {'result': added}
   return JsonResponse(resp_dict)

def subtract(request):
   num1 = float(request.GET.get('num1', 1))
   num2 = float(request.GET.get('num2', 1))
   subtracted = num1 - num2
   resp_dict = {'result': subtracted}
   return JsonResponse(resp_dict)

def multiply(request):
   num1 = float(request.GET.get('num1', 1))
   num2 = float(request.GET.get('num2', 1))
   multiplied = num1 * num2
   resp_dict = {'result': multiplied}
   return JsonResponse(resp_dict)

def divide(request):
   num1 = float(request.GET.get('num1', 1))
   num2 = float(request.GET.get('num2', 1))
   if num2 == 0:
      return JsonResponse({'result': 'Error: Division by zero'})
   divided = num1 / num2
   resp_dict = {'result': divided}
   return JsonResponse(resp_dict)

def exponential(request):
   num1 = float(request.GET.get('num1', 1))
   num2 = float(request.GET.get('num2', 1))
   exponential = num1 ** num2
   resp_dict = {'result': exponential}
   return JsonResponse(resp_dict)

## viewset for customers
class BookViewSet(viewsets.ModelViewSet):
	serializer_class = BookSerializer
	queryset = Book.objects.all()
