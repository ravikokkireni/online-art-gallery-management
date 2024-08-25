from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Cart, CartProduct
from .forms import UserRegistrationForm
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Product, Artist
from .forms import ArtistRegistrationForm, ProductForm
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from .models import OrderProduct, Product, Cart, CartProduct, Order
from .forms import UserRegistrationForm, ProductForm
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.shortcuts import render
from .models import Product
# from django.http import HttpResponseRedirect
# from django.urls import reverse
from .models import Product, Review
from .forms import ReviewForm
from django.shortcuts import render
from .models import Exhibition
from .models import Order



def profile(request):
    return render(request,'profile.html')

def video(request):
    return render(request,'video.html')

def exhibitions(request):
    exhibitions = Exhibition.objects.all()
    return render(request, 'exhibitions.html', {'exhibitions': exhibitions})


def artist_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if hasattr(user, 'artist'):
                login(request, user)
                return redirect('add_product')
            else:
                messages.error(request, "You are not registered as an artist.")
        else:
            messages.error(request, "Invalid username or password.")
    return render(request, 'login_artist.html')


def register_user(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.artist = request.user.artist
            product.save()
            return redirect('home')
    else:
        form = ProductForm()
    return render(request, 'add_product.html', {'form': form})

def home(request):
    products = Product.objects.all()
    reviews = Review.objects.all() 
    return render(request, 'home.html', {'products': products,'reviews': reviews})

from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Cart, CartProduct

def add_to_cart(request, product_id):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')  # Get the selected product_id from POST data
        # from .models import Product, Cart, CartProduct
        product = get_object_or_404(Product, id=product_id)
        cart, created = Cart.objects.get_or_create(user=request.user)
        cart_product, cart_product_created = CartProduct.objects.get_or_create(cart=cart, product=product)

        if not cart_product_created:
            cart_product.quantity += 1
            cart_product.save()
        
        return redirect('cart')
    
    return redirect('home')


def cart(request):
    cart = Cart.objects.get(user=request.user)
    return render(request, 'cart.html', {'cart': cart})

@login_required
def checkout(request):
    cart = Cart.objects.get(user=request.user)
    
    # Calculate total amounts for each cart product
    for cart_product in cart.cartproduct_set.all():
        cart_product.total_price = cart_product.product.price * cart_product.quantity
    
    return render(request, 'checkout.html', {'cart': cart})

def calculate_total(cart):
    total = 0
    for item in cart.cartproduct_set.all():
        total += item.product.price * item.quantity
    return total




@login_required
def purchase(request):
    # Logic to process the purchase (e.g., update orders, process payment)
    cart = Cart.objects.get(user=request.user)
    cart.cartproduct_set.all().delete()  # Example: Clear the cart after purchase

    # Redirect to a thank you page or another appropriate URL
    return redirect('purchase')


def ordercon(request):
    return render(request,"ordercon.html")




def artist_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if hasattr(user, 'artist'):
                login(request, user)
                return redirect('add_product')
            else:
                messages.error(request, "You are not registered as an artist.")
        else:
            messages.error(request, "Invalid username or password.")
    return render(request, 'login_artist.html')


def artist_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None and hasattr(user, 'artist'):
            login(request, user)
            return redirect('add_product')
    return render(request, 'login_artist.html')

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.artist = request.user.artist
            product.save()
            return redirect('home')
    else:
        form = ProductForm()
    return render(request, 'add_product.html', {'form': form})


def remove_from_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart = Cart.objects.get(user=request.user)
    cart_product = CartProduct.objects.get(cart=cart, product=product)

    if cart_product.quantity > 1:
        cart_product.quantity -= 1
        cart_product.save()
    else:
        cart_product.delete()

    return redirect('cart')





def register_user(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserRegistrationForm()
    return render(request, 'register_user.html', {'form': form})





def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
    return render(request, 'login_user.html')


def register_artist(request):
    if request.method == 'POST':
        form = ArtistRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            Artist.objects.create(user=user)
            return redirect('artist_login')
    else:
        form = ArtistRegistrationForm()
    return render(request, 'register_artist.html', {'form': form})





def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})




def main(request):
    return render(request, 'main.html')





def submit_review(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.product = product
            review.save()
            return redirect('home')  # Redirect to home or any other page after submission
    else:
        form = ReviewForm()
    return render(request, 'submit_review.html', {'form': form, 'product': product})



from django.contrib.auth.decorators import login_required

@login_required
def profile_view(request):
    user = request.user
    context = {
        'username': user.username,
        'email': user.email,
        'user_img_url': user.profile.image.url if user.profile.image else 'https://media.istockphoto.com/id/1327592506/vector/default-avatar-photo-placeholder-icon-grey-profile-picture-business-man.jpg?s=612x612&w=0&k=20&c=BpR0FVaEa5F24GIw7K8nMWiiGmbb8qmhfkpXcp1dhQg='
    }
    return render(request, 'profile.html', context)



@login_required
def myorders(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'myorders.html', {'orders': orders})





def watch_video(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    context = {'product': product}
    return render(request, 'video.html', context)