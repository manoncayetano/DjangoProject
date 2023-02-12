from django.views import generic
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.contrib import messages
from django.contrib.auth.models import User

from trouvetonchamp.forms.product import ProductForm
from trouvetonchamp.forms.register import RegisterForm
from trouvetonchamp.models import Product
from django.urls import reverse_lazy, reverse


class Index(ListView):
    template_name = 'index.html'
    queryset = Product.objects.order_by('-date_pub')


class ProductsUser(ListView):
    template_name = 'product_user.html'
    model = Product


class UpdateProduct(UpdateView):
    template_name = 'product_update.html'
    model = Product
    fields = ['name', 'summary', 'content', 'img1', 'img2', 'img3', 'banner', 'categories']

    def get_success_url(self):
        return reverse('product_user')


class Products(DetailView):
    objects = None
    template_name = 'product.html'
    model = Product


class CreateProduct(CreateView):
    template_name = 'create_Product.html'
    form_class = ProductForm
    success_url = reverse_lazy('index')


class RegisterFormView(generic.FormView):
    template_name = 'register_form.html'
    form_class = RegisterForm

    def form_valid(self, form):
        username = form.cleaned_data['username']
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        try:
            User.objects.create_user(username=username, email=email, password=password)
            messages.add_message(self.request, messages.INFO, 'User created successfully')
        except Exception as e:
            form.add_error(None, "Unexpected error")
            return super().form_invalid(form)
        return super().form_valid(form)

    def get_success_url(self):

        return reverse('index')


class ProductSearchView(ListView):
    template_name = 'index.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        result = super().get_context_data(object_list=object_list, **kwargs)
        result['description_results'] = \
            "Search result of product with name '{}'".format(self.kwargs['search'])
        return result

    def get_queryset(self):
        return Product.objects.filter(name__icontains=self.kwargs['search'])