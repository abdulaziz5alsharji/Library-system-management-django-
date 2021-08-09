from django.shortcuts import render, get_object_or_404
from . models import Book, Category
from . forms import BookForm, CategoryForm
from django.http import HttpResponseRedirect
from django.urls import reverse 
# Create your views here.


def index(request):
    books = Book.objects.all()
    Categories = Category.objects.all()
    sold = Book.objects.filter(status="sold").exclude(price=None)
    rental = Book.objects.filter(status="rental").exclude(total_retal=None)
    sold_price = [price.price for price in sold]
    rental_price = [price.total_retal for price in rental]
    total = sum(sold_price) + sum(rental_price)
    if request.method == "POST":
        form = BookForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("index"))
        category_form = CategoryForm(request.POST or None)
        if category_form.is_valid():
            category_form.save()
            return HttpResponseRedirect(reverse("index"))
    return render(request, "lms_app/pages/index.html", context={
        "books": books,
        "categories": Categories,
        "form": BookForm(),
        "category_form": CategoryForm(),
        "books_count": Book.objects.filter(active=True).count(),
        "books_available": Book.objects.filter(status="available").count(),
        "books_sold": Book.objects.filter(status="sold").count(),
        "books_rental": Book.objects.filter(status="rental").count(),
        "total": total,
        "total_sold": sum(sold_price),
        "total_rental": sum(rental_price),
    })


def books(request):
    Categories = Category.objects.all()
    if "search_name" in request.GET:
        title = request.GET["search_name"]
        if title:
            books = Book.objects.filter(title__icontains=title)
            return render(request, "lms_app/pages/books.html", context={
                "books": books,
                "categories": Categories,
                "category_form": CategoryForm(),
                })
        else:
            return render(request, "lms_app/pages/books.html", context={
                "books": Book.objects.all(),
                "categories": Categories,
                "category_form": CategoryForm(),
                })

    return render(request, "lms_app/pages/books.html", context={
        "books": Book.objects.all(),
        "categories": Categories,
        "category_form": CategoryForm(),
    })



def update(request, book_id):
    book = Book.objects.get(pk=book_id)
    if request.method == "POST":
        form = BookForm(request.POST or None, request.FILES or None, instance=book)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("index"))

    form = BookForm(instance=book)
    return render(request, "lms_app/pages/update.html", context={
        "form": form
    })


def delete(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == "POST":
        book.delete()
        return HttpResponseRedirect(reverse("index"))
    return render(request, "lms_app/pages/delete.html", context={
        
    })