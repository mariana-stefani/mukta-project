from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic import CreateView, UpdateView, DeleteView
from .models import Product, Category


def all_products(request):
    """ A view to display all products, including sorting and search queries """

    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "Please enter a search criteria.")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(
                description__icontains=query)
            products = products.filter(queries)

    currrent_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'currrent_sorting': currrent_sorting,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to display details for a single product """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product-detail.html', context)


class ProductCreateView(UserPassesTestMixin, CreateView):
    """ A view to create a new product on product-form page """
    model = Product
    template_name = 'products/product-form.html'
    context_object_name = 'product-create'
    fields = ['category', 'sku', 'name',
              'description', 'has_option', 'price', 'image_url', 'image']
    success_url = '/products'

    def test_func(self):
        return self.request.user.is_superuser


class ProductUpdateView(UserPassesTestMixin, UpdateView):
    """ A view to update an existing product on product-form page """
    model = Product
    template_name = 'products/product-form.html'
    context_object_name = 'product-update'
    fields = ['category', 'sku', 'name',
              'description', 'has_option', 'price', 'image_url', 'image']
    success_url = '/products'

    def test_func(self):
        return self.request.user.is_superuser


class ProductDeleteView(UserPassesTestMixin, DeleteView):
    """ A view to delete a product on product-delete page """
    model = Product
    template_name = 'products/product-delete.html'
    context_object_name = 'product-delete'
    success_url = '/products'

    def test_func(self):
        return self.request.user.is_superuser
