from django.views.generic import TemplateView

from .models import Product


class ProductView(TemplateView):
    template_name = 'products/list.html'

    def get_context_data(self, **kwargs):
        context = super(ProductView, self).get_context_data(**kwargs)
        context['products'] = Product.objects.all()

        return context
