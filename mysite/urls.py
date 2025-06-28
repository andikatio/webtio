# mysite/urls.py

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# Impor semua view yang dibutuhkan dari file views.py di folder mysite
from .views import (
    welcome, 
    store, 
    kontak, 
    not_found_artikel, 
    detail_artikel,
    dashboard
)
# Impor view otentikasi
from .authentication import login, logout, registrasi

urlpatterns = [
    # URL Admin
    path('admin/', admin.site.urls),

    # URL Halaman Utama & Statis
    path('', welcome, name="welcome"),
    path('store/', store, name="store"),
    path('kontak/', kontak, name="kontak"),
    path('artikel-not-found/', not_found_artikel, name="not_found_artikel"),

    # URL Dinamis untuk Detail Artikel
    path('artikel/<int:id>/', detail_artikel, name='detail_artikel'),

    # URL Dashboard
    path('dashboard/', dashboard, name='dashboard'),

    # URL Otentikasi
    path('auth-login/', login, name='login'),
    path('auth-logout/', logout, name='logout'),
    path('auth-registrasi/', registrasi, name='registrasi'),

    # URL untuk Tools Pihak Ketiga (API & Editor)
    path('api-auth/', include('rest_framework.urls')),
    path("ckeditor5/", include('django_ckeditor_5.urls')),

    # Menghubungkan ke semua URL dari aplikasi 'artikel'
    path('', include('artikel.urls')),
]

# Konfigurasi untuk menyajikan file media (gambar) saat development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)