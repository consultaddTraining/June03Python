from django.urls import path
from myapp import views

urlpatterns = [
    path('about/', views.about, name="About"),
    path('home/', views.homepage, name="homepage"),
    path('contact/', views.contact, name="Contact"),
    path('custom/', views.custom, name="Custom"),
    path('login/', views.login_form, name="Form"),
    # path('bookview/', views.BooksPage, name="Form"),
    path('api/', views.LoginList.as_view()),






]
