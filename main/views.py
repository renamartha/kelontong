import datetime
import json
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseNotFound, HttpResponseRedirect, JsonResponse
from main.forms import ProductForm
from django.urls import reverse
from main.forms import Item
from django.http import HttpResponse
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages  
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

@login_required(login_url='/login')
def show_main(request):
   products = Item.objects.filter(user=request.user)

   context = {
      'username': request.user.username,
      'nama' : 'Rena Martha Ulima',
      'class': 'PBP E',
      'products': products,
      'total_products': products.__len__(),
      'last_login': request.COOKIES['last_login'],
   }
   
   return render(request, "main.html", context)

def create_product(request):
   form = ProductForm(request.POST or None)

   if form.is_valid() and request.method == "POST":
      product = form.save(commit=False)
      product.user = request.user
      product.save()
      return HttpResponseRedirect(reverse('main:show_main'))

   context = {'form': form}
   return render(request, "create_product.html", context)

@csrf_exempt
def register(request):
   form = UserCreationForm()

   if request.method == "POST":
      form = UserCreationForm(request.POST)
      if form.is_valid():
         form.save()
         messages.success(request, 'Akun Anda berhasil dibuat!')
         return redirect('main:login')
   context = {'form':form}
   return render(request, 'register.html', context)

@csrf_exempt
def login_user(request):
   if request.method == 'POST':
      username = request.POST.get('username')
      password = request.POST.get('password')
      user = authenticate(request, username=username, password=password)
      if user is not None:
         login(request, user)
         response = HttpResponseRedirect(reverse("main:show_main")) 
         response.set_cookie('last_login', str(datetime.datetime.now()))
         return response
      else:
         messages.info(request, 'Sorry, incorrect username or password. Please try again.')
   context = {}
   return render(request, 'login.html', context)

def logout_user(request):
   logout(request)
   response = HttpResponseRedirect(reverse('main:login'))
   response.delete_cookie('last_login')
   return redirect('main:login')

def tambah_jumlah_item(request, id_item):
   product = get_object_or_404(Item, pk=id_item, user=request.user) #get_object_or_404 merupakan fungsi bawaan Django yang digunakan untuk mencari objek berdasarkan model tertentu, jika tidak ditemukan maka menampilkan halaman 404
   product.amount += 1
   product.save()
   return HttpResponseRedirect(reverse('main:show_main'))

def kurangi_jumlah_item(request, id_item):
   product = get_object_or_404(Item, pk=id_item, user=request.user)
   if product.amount > 0:
      product.amount -= 1
      product.save()
   else:
      messages.info(request, f'Jumlah {product.name} sudah 0, tidak bisa melakukan pengurangan!')
   return HttpResponseRedirect(reverse('main:show_main'))

def hapus_item(request, id_item):
   product = get_object_or_404(Item, pk=id_item, user=request.user)
   product.delete()
   return HttpResponseRedirect(reverse('main:show_main'))

def edit_product(request, id):
   product = Item.objects.get(pk = id)

   form = ProductForm(request.POST or None, instance=product)

   if form.is_valid() and request.method == "POST":
      form.save()
      return HttpResponseRedirect(reverse('main:show_main'))

   context = {'form': form}
   return render(request, "edit_product.html", context)

def show_xml(request):
   data = Item.objects.all()
   return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
   data = Item.objects.all()
   return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
   data = Item.objects.filter(pk=id)
   return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
   data = Item.objects.filter(pk=id)
   return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def get_product_json(request):
   product_item = Item.objects.filter(user=request.user)
   return HttpResponse(serializers.serialize('json', product_item))

@csrf_exempt
def add_product_ajax(request):
   if request.method == 'POST':
      name = request.POST.get("name")
      amount = request.POST.get("amount")
      harga = request.POST.get("harga")
      description = request.POST.get("description")
      user = request.user

      new_product = Item(name=name, amount=amount, harga=harga, description=description, user=user)
      new_product.save()

      return HttpResponse(b"CREATED", status=201)

   return HttpResponseNotFound()

@csrf_exempt
def delete_ajax(request):
   if request.method == 'DELETE':
      id_Item = request.GET.get("id")
      user = request.user
      product = Item.objects.get(pk=id_Item, user=user)
      product.delete()
      return HttpResponse(b"DELETED", status=204)
   return HttpResponseNotFound()

@csrf_exempt
def create_product_flutter(request):
   if request.method == 'POST':
      
      data = json.loads(request.body)

      new_product = Item.objects.create(
         user = request.user,
         name = data["name"],
         amount = int(data["amount"]),
         harga = int(data["harga"]),
         description = data["description"]
      )

      new_product.save()

      return JsonResponse({"status": "success"}, status=200)
   else:
      return JsonResponse({"status": "error"}, status=401)
# Create your views here.
