from django import forms
from customer.models import Customer


class DateInput(forms.DateInput):
    input_type = 'date'


class CustomerForm(forms.ModelForm):
    first_name = forms.CharField(label='Nome')
    last_name = forms.CharField(label='Sobrenome')
    email = forms.EmailField(label='Email')
    birth_date = forms.DateField(label='Data de nascimento', widget=DateInput())
    area_code = forms.RegexField(
            label='Area',
            regex=r'^\+?1?[0-9]{2}$',
            error_messages={'invalid':'Código de área inválido'}
        )
    phone_number = forms.RegexField(
            label='Telefone',
            regex=r'^\+?1?[0-9]{8,15}$',
            error_messages={'invalid':'Número de telefone inválido'}
        )
    country = forms.CharField(label='País')
    state = forms.CharField(label='Estado')
    city = forms.CharField(label='Cidade')

    class Meta:
        model = Customer
        fields = (
            'first_name',
            'last_name',
            'email',
            'birth_date',
            'area_code',
            'phone_number',
            'country',
            'state',
            'city'
        )