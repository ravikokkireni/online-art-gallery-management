from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.main, name='main'),
    path('register_user/', views.register_user, name='register_user'),
    path('login_user/', views.login_user, name='login_user'),
    path('register_artist/', views.register_artist, name='register_artist'),
    path('artist_login/', views.artist_login, name='artist_login'),
    # path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart, name='cart'),
    path('home/', views.home, name='home'),
    path('video/', views.home, name='video'),
    path('profile/', views.profile, name='profile'),
    path('ordercon/', views.ordercon, name='ordercon'),
    path('checkout/', views.checkout, name='checkout'),
    path('purchase/', views.purchase, name='purchase'),
    path('myorders/', views.myorders, name='myorders'),
    # path('ordercon/', views.OrderConfirmationView.as_view(), name='ordercon'),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),  # Ensure this line is present
    path('submit_review/<int:product_id>/', views.submit_review, name='submit_review'),
    path('exhibitions/', views.exhibitions, name='exhibitions'), 
    path('watch-video/<int:product_id>/', views.watch_video, name='watch_video'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)