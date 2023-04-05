from django.shortcuts import render, redirect
from .models import Products
from django.core.paginator import Paginator
# Create your views here.

def index(request):
	product_objects = Products.objects.all()
	 #search code
	item_name = request.GET.get('item_name')
	if item_name != '' and item_name is not None:
		product_objects = product_objects.filter(title__icontains=item_name)

	 #paginator code
	paginator = Paginator(product_objects,10)
	page = request.GET.get('page')
	product_objects = paginator.get_page(page)


	return render (request,'website/index.html',{'product_objects':product_objects})

def detail(request,id):
	product_object = Products.objects.get(id=id)
	return render(request,'website/detail.html',{'product_object':product_object})

# def login_user(request):
# 	if request.method == "POST":
# 		username = request.POST['username']
# 		password = request.POST['password']
# 		user = authenticate(request, username=username, password=password)
# 		if user is not NONE:
# 			login(request, user)
# 			messages.success(request, "You Have Been Logged In!  Woohoo!")
# 			return redirect('index')
# 		else:
# 			messages.success(request, "Error Logging In. Please Try Again...")
# 			return redirect('index')
# 	else:
# 		return render(request, 'index.html', {})

# def logout_user(request):
# 	logout(request)
# 	messages.success(request, "You Have Been Logged Out... Have A Nice Day!")
# 	return redirect('index')


# def register_user(request):
# 	if request.method == "POST":
# 		form = SignUpForm(request.POST)
# 		if form.is_valid():
# 			form.save()
# 			username = form.cleaned_data['username']
# 			password = form.cleaned_data['password1']
# 			user = authenticate(username=username, password=password)
# 			login(request, user)
# 			messages.success(request, "You Have Registered...Congrats!!")
# 			return redirect('index')

# 	else:
# 		form = SignUpForm()

# 	return render(request, 'register.html', {"form": form})
