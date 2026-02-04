from django.views.generic import TemplateView, View
from django.shortcuts import render
from .models import Product


# =========================
# HOME
# =========================
class HomePageView(TemplateView):
    template_name = 'pages/home.html'


# =========================
# ABOUT
# =========================
class AboutPageView(TemplateView):
    template_name = 'pages/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "title": "About us - Online Store",
            "subtitle": "About us",
            "description": "This is an about page ...",
            "author": "Developed by: Miguel",
        })
        return context


# =========================
# PRODUCT MODEL 
# =========================

# =========================
# PRODUCT LIST
# =========================
class ProductIndexView(View):
    def get(self, request):
        products = Product.objects.all()
        return render(request, "products/index.html", {
            "products": products
        })


# =========================
# PRODUCT DETAIL
# =========================
class ProductShowView(View):
    def get(self, request, id):
        product = Product.objects.get(id=id)

        return render(request, "products/show.html", {
            "product": product
        })
