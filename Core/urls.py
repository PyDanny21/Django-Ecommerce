from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',views.index,name='index'),
    path('related/<int:pk>/',views.related,name='related'),
    path('search/',views.search,name='search'),
    path('details/<int:pk>/',views.details,name='details'),
    path('cart/add/<int:pk>/',views.add_cart,name='add_cart'),
    path('cart/view/',views.view_cart,name='view_cart'),
    path('auth/signin/',views.signin,name='signin'),
    path('auth/signup/',views.signup,name='signup'),
    path('auth/logout/',views.logout,name='logout'),
    path('cart/remove/<int:cart_item_id>/',views.remove,name='remove'),
    path('cart/delete_all/',views.delete,name='delete'),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
