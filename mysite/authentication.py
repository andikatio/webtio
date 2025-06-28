from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout

def login (request):
    template_name = "login.html"
    pesan = ""
    if request.method == "POST":
        username = request.POST.get ('username')
        password = request.POST.get ('password')
        if not username or not password:
            pesan = "Username dan Password wajib diisi"
        
        else:
            user = authenticate (username = username, password = password)
            if user is not None:
                auth_login(request, user)
                pesan : "berhasillogin"
                return redirect('/')
            else:
                pesan = "username atau password salah"

    context = {
        'pesan':pesan
    }
    return render(request, template_name, context)

def registrasi (request):
    template_name = "registrasi.html"
    pesan = ""
    if request.method == "POST":
        username = request.POST.get ('username')
        nama_depan = request.POST.get ('nama_depan')
        nama_belakang = request.POST.get ('nama_belakang')
        password1 = request.POST.get ('password1')
        password2 = request.POST.get ('password2')

        print(username, nama_depan, nama_belakang, password1, password2)

        if not username or not nama_depan or not nama_belakang or not password1 or not password2:
            pesan = "Semua data wajib wajib diisi yaaa"
        else:
            if password1 != password2:
                pesan = "password 1 dan 2 tidak sama"
            else:
                 user = User.objects.filter(username=username)
                 if user.exists():
                    pesan = "username sudah digunakan!"
                 else :
                    user = User.objects.create(
                        username = username,
                        first_name = nama_depan,
                        last_name = nama_belakang,
                        )
                    user.set_password(password1)
                    user.save()
                    return redirect('/')
    context = {
        'pesan': pesan
    }
    return render(request, template_name, context)

def logout(request):
    auth_logout(request)
    return redirect('/')
