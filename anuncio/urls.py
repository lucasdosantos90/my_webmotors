from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
     path('',views.homepage,name='homepage'),
     path('favoritos/<int:id>/',views.favoritos,name='favoritos'),
     path('automovel_list/',views.AutomovelList.as_view(),name='automovel_listar'),
     path('meus_automoveis/',views.MeusAutomoveis.as_view(),name='meus_automoveis'),
     path('meus_favoritos/',views.meus_favoritos,name='meus_favoritos'),
     path('automovel_detalhe/<int:id>/',views.automovel_detalhe,name='automovel_detalhe'),
     path('automovel_categoria/<int:categoria>/',views.automovel_categoria,name='automovel_categoria'),
     path('cadastrar_automovel/',views.CadastrarAutomovel.as_view(),name='cadastrar_automovel'),
     path('update_automovel/<int:pk>/',views.UpdateAutomovel.as_view(),name='update_automovel'),
     path('delete_automovel/<int:pk>/',views.DeleteAutomovel.as_view(),name='delete_automovel'),
     path('login/',views.CustomLoginView.as_view(),name='login'),
     path('logout/',LogoutView.as_view(next_page='login'),name='logout'),
     path('register/',views.RegisterPage.as_view(),name='register'),

     path('<str:room>/', views.room, name='room'),
     path('checkview', views.checkview, name='checkview'),
     path('send', views.send, name='send'),
     path('getMessages/<str:room>/', views.getMessages, name='getMessages'),  
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)