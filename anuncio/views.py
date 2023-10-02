from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView,UpdateView,DeleteView,FormView
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.db.models import Q
from .models import Automovel, Carroceria, Room, Message, Itens_veiculo, Cor, Cambio, Combustivel, TipoAutomovel, MarcaAutomovel
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
def homepage(request):
    title = 'Homepage'
    pesquisa = request.GET.get('search-area')
    if pesquisa:
        automoveis = Automovel.objects.filter(Q(nome__icontains=pesquisa))
    else:
        automoveis = Automovel.objects.all().order_by('data_criado')
    carroceria = Carroceria.objects.all()
    for automovel in automoveis:
        automovel.vezes_na_lista += 1
        automovel.save()
    return render(request,'homepage.html',{'automoveis':automoveis,'title':title,'carroceria':carroceria})


def automovel_detalhe(request,id):
    automoveis = Automovel.objects.filter(id=id)
    title = f'Anúncio - {automoveis}'
    for automovel in automoveis:
        automovel.viram_anuncio += 1
        automovel.save()
    return render(request,'automoveis_detalhe.html',{'automoveis':automoveis,'title':title})
         

@login_required(login_url='/register/')
def favoritos(request,id):
    favorito = get_object_or_404(Automovel,id=id)
    if favorito.favoritos.filter(id=request.user.id).exists():
        favorito.favoritos.remove(request.user)
    else:
        favorito.favoritos.add(request.user)
    return HttpResponseRedirect(request.META['HTTP_REFERER'])   


@login_required(login_url='/register/')
def meus_favoritos(request):
    favoritos = Automovel.objects.filter(favoritos=request.user)
    print(favoritos)
    return render(request,'anuncio/meus_favoritos.html',{'favoritos':favoritos})


def automovel_categoria(request,categoria):
    carroceria = Carroceria.objects.filter(carroceria=categoria).first()
    automoveis = Automovel.objects.all().filter(carroceria=carroceria)
    print(carroceria)
    title = f'Categorias - {carroceria}'
    return render(request, 'automovel_categoria.html',{'automoveis':automoveis,'carroceria':carroceria,'title':title})


class AutomovelList(ListView):
    model = Automovel
    context_object_name = 'automoveis'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #context['automoveis'] = context['automoveis'].filter(login=self.request.user)
        '''acima vai fazer o botao listar só automoveis do usuario logado'''

        context['automoveis'] = context['automoveis']
        context['itens_veiculo'] = Itens_veiculo.objects.all()
        context['cor_veiculo'] = Cor.objects.all()
        context['carroceria_veiculo'] = Carroceria.objects.all()
        context['combustivel_veiculo'] = Combustivel.objects.all()
        context['cambio_veiculo'] = Cambio.objects.all()
        context['tipo_automovel'] = TipoAutomovel.objects.all()
        context['marca_automovel'] = MarcaAutomovel.objects.all()
        
        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['automoveis'] = context['automoveis'].filter(nome__icontains=search_input)
        context['search-input'] = search_input

        itens_veiculo = self.request.GET.get('search_itens_veiculo') or ''
        if itens_veiculo:
            context['automoveis'] = context['automoveis'].filter(itens_veiculo=itens_veiculo)

        cor_veiculo = self.request.GET.get('search_cor_veiculo') or ''
        if cor_veiculo:
            context['automoveis'] = context['automoveis'].filter(cor=cor_veiculo)

        carroceria_veiculo = self.request.GET.get('search_carroceria_veiculo') or ''
        if carroceria_veiculo:
            context['automoveis'] = context['automoveis'].filter(carroceria=carroceria_veiculo)

        combustivel_veiculo = self.request.GET.get('search_combustivel_veiculo') or ''
        if combustivel_veiculo:
            context['automoveis'] = context['automoveis'].filter(combustivel=combustivel_veiculo)

        cambio_veiculo = self.request.GET.get('search_cambio_veiculo') or ''
        if cambio_veiculo:
            context['automoveis'] = context['automoveis'].filter(cambio=cambio_veiculo)
        
        tipo_automovel = self.request.GET.get('search_tipo_automovel') or ''
        if tipo_automovel:
            context['automoveis'] = context['automoveis'].filter(tipo_automovel=tipo_automovel)

        marca_automovel = self.request.GET.get('search_marca_automovel') or ''
        if marca_automovel:
            context['automoveis'] = context['automoveis'].filter(marca=marca_automovel)

        return context
     
    
class MeusAutomoveis(LoginRequiredMixin, ListView):
    model = Automovel
    context_object_name = 'automoveis'
    template_name = 'anuncio/meus_automoveis.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['automoveis'] = context['automoveis'].filter(login=self.request.user)
        '''acima vai fazer o botao listar só automoveis do usuario logado'''
        
        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['automoveis'] = context['automoveis'].filter(nome__icontains=search_input)
        context['search-input'] = search_input
        
        return context


class CadastrarAutomovel(LoginRequiredMixin, CreateView):
    template_name = 'cadastrar_automovel.html'
    model = Automovel
    #fields = '__all__'
    fields = ['nome','tipo_automovel','valor','versao_carro','marca','cidade',
              'estado','ano','km','placa','nome_loja','ipva_pago',
              'sobre_automovel','cambio','carroceria','combustivel',
              'cor','aceita_troca','licenciado',
              'foto1','foto2','foto3','foto4','foto5','itens_veiculo',
              'contato','status_anuncio']
    success_url = reverse_lazy('homepage')

    #
    # Aqui abaixo em form_valid estou restringindo a class CriarAutomovel
    # a ter por padrão selecionado o usuário logado, mas para isso
    # é preciso usar os fields selecionados como está acima,
    # diferente de chamar todos, como fields = '__all__'
    #  #
    def form_valid(self, form):
        form.instance.login = self.request.user
        return super(CadastrarAutomovel,self).form_valid(form)  
    
    #Esse override é APENAS para alterar o título da página
    def get_context_data(self, **kwargs):
        context = super(CadastrarAutomovel,self).get_context_data(**kwargs)
        context['title'] = 'Criar Automovel'
        return context
    

class UpdateAutomovel(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name = 'update_automovel.html'
    model = Automovel
    #fields = '__all__'
    fields = ['nome','tipo_automovel','valor','versao_carro','marca','cidade',
              'estado','ano','km','placa','nome_loja','ipva_pago',
              'sobre_automovel','cambio','carroceria','combustivel',
              'cor','aceita_troca','licenciado',
              'foto1','foto2','foto3','foto4','foto5','itens_veiculo',
              'contato','status_anuncio']
    success_url = reverse_lazy('homepage')

    def form_valid(self, form):
        form.instance.login = self.request.user
        return super(UpdateAutomovel,self).form_valid(form)
    
    #Esse override é APENAS para alterar o título da página
    def get_context_data(self, **kwargs):
        context = super(UpdateAutomovel,self).get_context_data(**kwargs)
        context['title'] = 'Atualizar Automovel'
        return context    
    
    #Para não permitir usuário criar/editar/excluir post de outros
    def test_func(self):
        automovel = self.get_object()
        if self.request.user == automovel.login:
            return True
        return False
    
class DeleteAutomovel(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Automovel
    template_name = 'delete_automovel.html'
    context_object_name = 'delete_automovel_obj'
    success_url = reverse_lazy('homepage')

    #Para não permitir usuário criar/editar/excluir post de outros
    def test_func(self):
        automovel = self.get_object()
        if self.request.user == automovel.login:
            return True
        return False    

class CustomLoginView(LoginView):
    template_name = 'login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('homepage')   

class RegisterPage(FormView):
    template_name = 'register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('homepage')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request,user)
        return super(RegisterPage,self).form_valid(form)    
  

#Mensagens    
@login_required(login_url='/login/')
def room(request, room):
    username = request.GET.get('username')
    room_details = Room.objects.get(name=room)
    return render(request, 'chat.html', {
        'username': username,
        'room': room,
        'room_details': room_details
    })


@login_required(login_url='/login/')
def checkview(request):
    receiver = request.POST['room_name']
    room = request.POST['room_name']
    username = request.POST['username']
    carro = request.POST['carro']
    
    room1 = room + username
    room2 = username + room
    
    if Room.objects.filter(name=room1).exists():
        return redirect('/'+room1+'/?username='+username)
    elif Room.objects.filter(name=room2).exists():
        return redirect('/'+room2+'/?username='+username)   
    else:
        new_room = Room.objects.create(name=room1,created_by=username,receiver=receiver,carro=carro)
        new_room.save()
        return redirect('/'+room1+'/?username='+username)


def send(request):
    message = request.POST['message']
    username = request.POST['username']
    room_id = request.POST['room_id']

    new_message = Message.objects.create(value=message, user=username, room=room_id)
    new_message.save()
    return HttpResponse('Message sent successfully')


def getMessages(request, room):
    room_details = Room.objects.get(name=room)
    messages = Message.objects.filter(room=room_details.id)
    return JsonResponse({"messages":list(messages.values())})   


def minhas_conversas(request,room):
    mensagens = Message.objects.filter().all()
    salas = Room.objects.filter().all()
    carros = Automovel.objects.filter().all()
    print(mensagens)
    print(salas)
    return render(request, 'minhas_conversas.html', {'mensagens': mensagens,'salas': salas,'carros':carros})