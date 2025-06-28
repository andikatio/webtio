from django import forms 
from django_ckeditor_5.widgets import CKEditor5Widget
from artikel.models import Kategori, ArtikelBlog

class KategoriForms(forms.ModelForm):
    class Meta:
        model = Kategori
        fields = ['nama',]
        widgets = {
            'nama': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'required': True
                }
            ),
        }
        
class ArtikelForms(forms.ModelForm):
    class Meta:
        model = ArtikelBlog
        fields = ['kategori', 'judul', 'konten', 'gambar', 'status']
        widgets = {
            'kategori': forms.Select(
                attrs={
                    'class': 'form-control',
                    'required': True,
                }
            ),
            'judul': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'required': True
                }
            ),
            'konten': CKEditor5Widget(
                  attrs={"class": "django_ckeditor_5"},
                  config_name="extends"
              ),
        }