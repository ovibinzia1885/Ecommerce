from django.urls import path

from . import views

urlpatterns = [
	#Leave as empty string for base url
	path('', views.store, name="store"),
	path('cart/', views.cart, name="cart"),
	path('cheekout/', views.cheekout, name="cheekout"),
	path('update_Item/', views.updateItem, name="update_Item"),
	path('ProcessOrder/', views.ProcessOrder, name="ProcessOrder"),


]
