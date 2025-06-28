# mysite/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.contrib.auth.models import User

# Impor model dari aplikasi 'artikel'
from artikel.models import Kategori, ArtikelBlog

# View untuk halaman depan (Welcome Page)
def welcome(request):
    template_name = "landingpage/index.html"
    kategori = Kategori.objects.all()
    artikel = ArtikelBlog.objects.all().order_by('-created_at')
    top_artikel = ArtikelBlog.objects.all().order_by('-created_at')[:3]

    context = {
        "title": "Selamat Datang",
        "kategori": kategori,
        "artikel": artikel,
        "top_artikel": top_artikel,
    }
    return render(request, template_name, context)

# View untuk halaman detail artikel
def detail_artikel(request, id):
    template_name = "landingpage/detail.html"
    artikel = get_object_or_404(ArtikelBlog, id=id)
    artikel_lainya = ArtikelBlog.objects.exclude(id=id).order_by('?')[:5]
    
    context = {
        "title": artikel.judul,
        "artikel": artikel,
        "artikel_lainya": artikel_lainya,
    }
    return render(request, template_name, context)

# View untuk halaman artikel tidak ditemukan
def not_found_artikel(request):
    template_name = "not-found-artikel.html"
    return render(request, template_name)

# View untuk halaman statis
def store(request):
    template_name = "store.html"
    context = {"title": "Halaman Store"}
    return render(request, template_name, context)

def kontak(request):
    template_name = "kontak.html"
    context = {"title": "Kontak"}
    return render(request, template_name, context)

# View untuk halaman dashboard
@login_required(login_url='login')
def dashboard(request):
    template_name = "dashboard/index.html"

    # 1. Data untuk Statistik Umum
    total_articles = ArtikelBlog.objects.count()
    total_categories = Kategori.objects.count()
    total_users = User.objects.count()
    total_categories_used = ArtikelBlog.objects.values('kategori').distinct().count()

    # 2. Data untuk Tabel Artikel Terbaru (ambil 5 terbaru)
    recent_articles = ArtikelBlog.objects.order_by('-created_at')[:5]

    # ===================================================================
    # 3. Data untuk Pie Chart Kategori (PENDEKATAN BARU YANG LEBIH KUAT)
    # ===================================================================
    # Mengelompokkan artikel berdasarkan nama kategori dan menghitungnya
    kategori_counts = ArtikelBlog.objects.values('kategori__nama').annotate(
        jumlah_artikel=Count('id')
    ).order_by('-jumlah_artikel')

    # Menyiapkan data untuk dikirim ke JavaScript
    # Hasil query adalah: [{'kategori__nama': 'earphone', 'jumlah_artikel': 1}, ...]
    category_labels = [item['kategori__nama'] for item in kategori_counts]
    article_counts = [item['jumlah_artikel'] for item in kategori_counts]
    
    # Kirim semua data ke template melalui context
    context = {
        "title": "Dashboard",
        "total_articles": total_articles,
        "total_categories": total_categories,
        "total_users": total_users,
        "total_categories_used": total_categories_used,
        "recent_articles": recent_articles,
        # Variabel 'categories' ini untuk check {% if categories %} di template agar lolos
        "categories": kategori_counts,
        "category_labels": category_labels,
        "article_counts": article_counts,
    }
    return render(request, template_name, context)