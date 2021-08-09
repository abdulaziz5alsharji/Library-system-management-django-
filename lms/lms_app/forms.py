from django.forms import widgets
from .models import Book, Category
from django import forms

class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = ["name"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"})
        }


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = [
            "title",
            "author",
            "photo_book",
            "photo_author",
            "pages",
            "price",
            "retal_price_day",
            "retal_period",
            "total_retal",
            "status",
            "category"
        ]
        widgets = {
            "title": forms.TextInput(attrs={"class":"form-control"}),
            "author": forms.TextInput(attrs={"class":"form-control"}),
            "photo_book": forms.FileInput(attrs={"class":"form-control"}),
            "photo_author": forms.FileInput(attrs={"class":"form-control"}),
            "pages": forms.NumberInput(attrs={"class":"form-control"}),
            "price": forms.NumberInput(attrs={"class":"form-control"}),
            "retal_price_day": forms.NumberInput(attrs={"class":"form-control", "id": "retal-price"}),
            "retal_period": forms.NumberInput(attrs={"class":"form-control", "id": "retal-day"}),
            "total_retal": forms.NumberInput(attrs={"class":"form-control", "id": "total-retal"}),
            "status": forms.Select(attrs={"class":"form-control"}),
            "category": forms.Select(attrs={"class":"form-control"}),
        }
