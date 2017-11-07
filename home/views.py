from django.shortcuts import render,redirect
from django.db import connection
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.views import generic
from django.views.generic import View
from django.contrib import auth
from .forms import UserForm, productForm
from django.core.files.storage import FileSystemStorage
import datetime


# Create your views here.
def dictfetchall(cursor): 
    desc = cursor.description 
    return [dict(zip([col[0] for col in desc], row)) for row in cursor.fetchall()]

def index(request):
	return render(request,'home/index.html')

# def save_img(img):
# 	fs = FileSystemStorage()
# 	path_to_img = str('product')+str(datetime.datetime.now())
# 	f_n = fs.save(path_to_img, img)
# 	up_f = fs.url(f_n)
# 	return up_f



class UserFormView(View):
	form_class = UserForm
	template_name = 'home/register.html'

	#isplaying black form for new coming user

	def get(self, request):
		form = self.form_class(None)
		return render(request, self.template_name, {'form':form})

	#process for data

	def post(self, request):
		form = self.form_class(request.POST)

		if form.is_valid():

			user = form.save(commit=False)

			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			first_name = form.cleaned_data['first_name']
			last_name = form.cleaned_data['last_name']
			user.set_password(password)
			user.save()

			address = request.POST.get('address')
			phone = request.POST.get('phone')
			state = request.POST.get('state')
			city = request.POST.get('city')
			pincode = request.POST.get('pincode')

			#db=MySQLdb.connect('localhost','root','zetaro@123','testdatabase')
			cursor=connection.cursor()
			cursor.execute("select id from auth_user where username = '" + username+ "';")

			userid=cursor.fetchone()
			userid=int(userid[0])

			cursor.execute(
				"insert ignore into user_address values  (" + str(pincode) + ",'" + str(city) + "','" + str(state) + "');")

			cursor.execute("insert into customer (ID,address,phone,pincode) values (" +str(userid)+ ",'" +str(address)+ "','"+ str(phone)+ "'," +str(pincode) +");")

			#authenticating user
			user = authenticate(username=username,password=password)

			if user is not None:

				if user.is_active:
					login(request)
					return redirect('index')
		return render(request, self.template_name, {'form':form})



def login(request):
		if request.POST:
			username = request.POST.get('username')
			password = request.POST.get('password')
			user = auth.authenticate(username=username, password=password)
			args = {'username':username}

			if user is not None:
				auth.login(request,user)
				if request.user.is_superuser:
					return render(request, 'home/admin.html',args)
				else:
				 	return redirect('showproduct')

			else:
				return render(request, 'home/index.html')
		else:
			return render(request,'home/login.html')




def addproduct(request):
	if request.POST:
		if request.user.is_superuser:
			price = request.POST.get('price')
			company = request.POST.get('company')
			image = request.POST.get('image')
			

			cursor=connection.cursor()
			cursor.execute("insert into product (price,company,image_path) values (" +str(price)+ ",'" + str(company) + "','" + str(image)+ "');")
	return render(request,'home/addpdt.html')





def showproduct(request):
	cursor=connection.cursor()
	cursor.execute("select * from product;")
	product=dictfetchall(cursor)
	context={'product':product}
	return render(request,'home/product.html',context)


def productadd(request):
	return render(request,'home/product_add.html')