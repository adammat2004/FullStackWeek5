from django.urls import path, include
from . import views
from rest_framework import routers
#create and define our router
router = routers.DefaultRouter()
router.register(r'books', views.BookViewSet)
urlpatterns = [
   path('', views.index, name="index"),
   path('all_books/', views.view_all_books, name="all_books"),
   path('single_book/<int:book_id>/', views.view_single_book, name="single_book"),
   path('books_by_category/<str:category>/', views.view_books_by_category, name="books_by_category"),
   path('add', views.api_add, name='api_add'),
   path('subtract', views.subtract, name='subtract'),
   path('multiply', views.multiply, name='multiply'),
   path('divide', views.divide, name='divide'),
   path('exponential', views.exponential, name='exponential'),
   path('api_auth/', include('rest_framework.urls')),
   path('api/', include(router.urls)),
]