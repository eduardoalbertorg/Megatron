from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Employee


class UserRegisterForm(UserCreationForm):
    # Default is required=True
    email = forms.EmailField()
    first_name = forms.CharField(max_length=100, label="Nombres")
    last_name = forms.CharField(max_length=100, label="Apellidos")

    class Meta:
        model = User
        # fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        if not commit:
            raise NotImplementedError("Can't create User and Employee without database save")
        full_name = '%s %s' % (self.cleaned_data['last_name'], self.cleaned_data['first_name'])
        user = super(UserRegisterForm, self).save(commit=True)
        employee = Employee(user=user, full_employee_name=full_name)
        employee.save()
        return user, employee

    def clean_email(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if email and User.objects.filter(email=email).exclude(username=username).exists():
            raise forms.ValidationError(u'Ya existe un registro con esta cuenta de correo.')
        return email

    def clean(self):
        clean_data = super(UserRegisterForm, self).clean()
        full_name = '%s %s' % (self.cleaned_data['last_name'], self.cleaned_data['first_name'])
        if full_name is "":
            raise forms.ValidationError(u'Alguno de los campos de nombre se encuentra vacio.')
        if full_name and Employee.objects.filter(full_employee_name=full_name).exists():
            raise forms.ValidationError(u'Ya existe un usuario con tu nombre, contacta al administrador.')
        return clean_data
