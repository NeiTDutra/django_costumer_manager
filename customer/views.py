from django.views.generic import ListView, CreateView
from customer.models import Customer
from customer.forms import CustomerForm
from django.urls import  reverse


class CustomerListView(ListView):
    template_name = 'customer-list.html'
    model = Customer
    queryset = Customer.objects.all()


class CustomerCreateView(CreateView):
    template_name = 'customer-create.html'
    form_class = CustomerForm

    def form_valid(self, form):
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('customer:customer-list')
