from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User, Group

from artikel.models import Kategori, ArtikelBlog
from artikel.forms import KategoriForms, ArtikelForms

from django.db.models import Count
from django.shortcuts import render
import json

# Create your views here.
def in_operator(user):
    get_user = user.groups.filter(name='Operator').count()
    if get_user == 0:
        return False
    else:
        return True

######################## user biasa ###########################
@login_required(login_url='/auth-login')
def artikel_list(request):
    template_name = "dashboard/pengguna/artikel_list.html"
    artikel = ArtikelBlog.objects.filter(created_by=request.user)
    context = {
        "artikel": artikel
    }
    return render(request, template_name, context)

@login_required(login_url='/auth-login')
def artikel_tambah(request):
    template_name = "dashboard/admin/artikel_forms.html"
    if request.method == "POST":
        forms = ArtikelForms(request.POST, request.FILES)
        if forms.is_valid():
            pub = forms.save(commit=False)
            pub.created_by = request.user
            pub.save()
            messages.success(request, 'berhasil tambah artikel')
        return redirect(artikel_list)
    forms = ArtikelForms()
    context = {
        "forms":forms
    }
    return render(request, template_name, context)

@login_required(login_url='/auth-login')
def artikel_update(request, id_artikel):
    template_name = "dashboard/artikel_forms.html"
    try:
        artikel = ArtikelBlog.objects.get(id=id_artikel, created_by=request.user)
    except:
        messages.warning(request, "halaman yang diminta tidak ditemukan")
        return redirect("/")
    if request.method == "POST":
        forms = ArtikelForms(request.POST, request.FILES, instance=artikel)
        if forms.is_valid():
            pub = forms.save(commit=False)
            pub.created_by = request.user
            pub.save()
            messages.success(request, 'berhasil melakukan update artikel')
        return redirect(artikel_list)
    forms = ArtikelForms(instance=artikel)
    context = {
        "forms":forms
    }
    return render(request, template_name, context)

@login_required(login_url='/auth-login')
def artikel_delete(request, id_artikel):
    try:
        ArtikelBlog.objects.get(id=id_artikel, created_by=request.user).delete()
        messages.success(request, 'berhasil delete artikel')
    except:
        messages.error(request, 'gagal delete artikel')
    
    return redirect(artikel_list)


###################### ADMIN #########################
@login_required(login_url='/auth-login')
@user_passes_test(in_operator, login_url='/')
def admin_kategori_list(request):
    template_name = "dashboard/admin/kategori_list.html"
    kategori = Kategori.objects.all()
    context = {
        "kategori":kategori
    }
    return render(request, template_name, context)

@login_required(login_url='/auth-login')
@user_passes_test(in_operator, login_url='/')
def admin_kategori_tambah(request):
    template_name = "dashboard/admin/kategori_forms.html"
    if request.method == "POST":
        forms = KategoriForms(request.POST)
        if forms.is_valid():
            pub = forms.save(commit=False)
            pub.created_by = request.user
            pub.save()
            messages.success(request, 'berhasil tambah kategori')
        return redirect(admin_kategori_list)
    forms = KategoriForms
    context = {
        "forms":forms
    }
    return render(request, template_name, context)

@login_required(login_url='/auth-login')
@user_passes_test(in_operator, login_url='/')
def admin_kategori_update(request, id_kategori):
    template_name = "dashboard/admin/kategori_forms.html"
    kategori = Kategori.objects.get(id=id_kategori)
    if request.method == "POST":
        forms = KategoriForms(request.POST, instance=kategori)
        if forms.is_valid():
            pub = forms.save(commit=False)
            pub.created_by = request.user
            pub.save()
            messages.success(request, 'berhasil update kategori')
        return redirect(admin_kategori_list)
    forms = KategoriForms(instance=kategori)
    context = {
        "forms":forms
    }
    return render(request, template_name, context)

@login_required(login_url='/auth-login')
@user_passes_test(in_operator, login_url='/')
def admin_kategori_delete(request, id_kategori):
    try:
        Kategori.objects.get(id=id_kategori).delete()
        messages.success(request, 'berhasil delete kategori')
    except:
        messages.error(request, 'gagal delete kategori')
    
    return redirect(admin_kategori_list)

############## Artikel Blog ##################
@login_required(login_url='/auth-login')
@user_passes_test(in_operator, login_url='/')
def admin_artikel_list(request):
    template_name = "dashboard/admin/artikel_list.html"
    artikel = ArtikelBlog.objects.all()
    context = {
        "artikel":artikel
    }
    return render(request, template_name, context)

@login_required(login_url='/auth-login')
@user_passes_test(in_operator, login_url='/')
def admin_artikel_tambah(request):
    template_name = "dashboard/admin/artikel_forms.html"
    if request.method == "POST":
        forms = ArtikelForms(request.POST, request.FILES)
        if forms.is_valid():
            pub = forms.save(commit=False)
            pub.created_by = request.user
            pub.save()
            messages.success(request, 'berhasil tambah artikel')
        return redirect(admin_artikel_list)
    forms = ArtikelForms()
    context = {
        "forms":forms
    }
    return render(request, template_name, context)

@login_required(login_url='/auth-login')
@user_passes_test(in_operator, login_url='/')
def admin_artikel_update(request, id_artikel):
    template_name = "dashboard/admin/artikel_forms.html"
    artikel = ArtikelBlog.objects.get(id=id_artikel)
    if request.method == "POST":
        forms = ArtikelForms(request.POST, request.FILES, instance=artikel)
        if forms.is_valid():
            pub = forms.save(commit=False)
            pub.created_by = request.user
            pub.save()
            messages.success(request, 'berhasil melakukan update artikel')
        return redirect(admin_artikel_list)
    forms = ArtikelForms(instance=artikel)
    context = {
        "forms":forms
    }
    return render(request, template_name, context)

@login_required(login_url='/auth-login')
@user_passes_test(in_operator, login_url='/')
def admin_artikel_delete(request, id_artikel):
    try:
        ArtikelBlog.objects.get(id=id_artikel).delete()
        messages.success(request, 'berhasil delete artikel')
    except:
        messages.error(request, 'gagal delete artikel')
    
    return redirect(admin_artikel_list)


def detail_artikel(request, id):
    template_name = "landingpage/detail_artikel.html"
    try:
        artikel = ArtikelBlog.objects.get(id=id)
    except ArtikelBlog.DoesNotExist:
        return redirect(not_found_artikel)
    
    artikel_lainnya = ArtikelBlog.objects.all().exclude(id=id)
    
    context = {
        "title":"Artikel",
        "artikel": artikel,
        "artikel_lainnya":artikel_lainnya
    }
    return render(request, template_name, context)

################### Management User Oleh Operator ###################

@login_required(login_url='/auth-login')
@user_passes_test(in_operator, login_url='/')
def admin_management_user_list(request):
    template_name = "dashboard/admin/user_list.html"  # Assuming a common template naming convention
    daftar_user = User.objects.all()
    context = {
        "daftar_user": daftar_user
    }
    return render(request, template_name, context)

@login_required(login_url='/auth-login')
@user_passes_test(in_operator, login_url='/')
def admin_management_user_edit(request, user_id):
    template_name = "dashboard/admin/user_edit.html"
    user = get_object_or_404(User, pk=user_id)  # Ambil objek user berdasarkan ID, atau 404 jika tidak ditemukan

    all_groups = Group.objects.all()
    group_user = []
    for group in user.groups.all():
        group_user.append(group.name)

    if request.method == 'POST':
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        is_staff_input = request.POST.get("is_staff")  # Renamed to avoid conflict with user.is_staff
        groups_checked = request.POST.getlist('groups')

        if is_staff_input is None:
            is_staff = False
        else:
            is_staff = True

        user.first_name = first_name
        user.last_name = last_name
        user.is_staff = is_staff
        user.groups.set(Group.objects.filter(id__in=groups_checked))
        user.save()

        messages.success(request, f"Berhasil update user {user.username}")
        return redirect('admin_management_user_list')  # Redirect ke halaman daftar user setelah berhasil

    context = {
        'user': user,
        'all_groups': all_groups,
        'group_user': group_user,
        
    }
    return render(request, template_name, context)

    # Contoh di dalam views.py Anda



def dashboard_view(request):
    # Mengambil kategori dan jumlah artikel di dalamnya
    categories_with_counts = Category.objects.annotate(article_count=Count('artikel')).filter(article_count__gt=0)

    # Data untuk Chart.js
    category_labels = [cat.name for cat in categories_with_counts]
    article_counts = [cat.article_count for cat in categories_with_counts]

    # Statistik Umum
    total_articles = Article.objects.count()
    total_categories = Category.objects.count()
    # total_comments = ... (hitung komentar Anda)

    # Artikel Terbaru
    recent_articles = Article.objects.order_by('-publish_date')[:5]

    context = {
        'categories': categories_with_counts,
        'recent_articles': recent_articles,
        'total_articles': total_articles,
        'total_categories': total_categories,
        # 'total_comments': total_comments,

        # Data untuk JavaScript, diubah ke format JSON
        'category_labels': json.dumps(category_labels),
        'article_counts': json.dumps(article_counts),
    }

    return render(request, 'dashboard/your_template_name.html', context)
