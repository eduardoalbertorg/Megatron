from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Employee


class UserRegisterForm(UserCreationForm):
    # Default value is required=True
    email = forms.EmailField(label="Correo electronico")
    first_name = forms.CharField(max_length=100, label="Nombres")
    last_name = forms.CharField(max_length=100, label="Apellidos")
    employee_code = forms.CharField(max_length=10, label="Codigo de empleado")

    class Meta:
        model = User
        # fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']
        fields = ['username', 'email', 'password1', 'password2']
        labels = {
            'email': 'Correo electronico',
            'username': 'Nombre de usuario',
            'password': 'Contraseña',
        }

    def save(self, commit=True):
        if not commit:
            raise NotImplementedError("Can't create User and Employee without database save")
        full_name = '%s %s' % (self.cleaned_data['last_name'], self.cleaned_data['first_name'])
        user = super(UserRegisterForm, self).save(commit=True)
        employee_code = self.cleaned_data['employee_code']
        employee = Employee(user=user, full_name=full_name, code=employee_code)
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
        first_name = self.cleaned_data['first_name']
        last_name = self.cleaned_data['last_name']
        employee_code = self.cleaned_data['employee_code']
        if first_name is "" or last_name is "":
            raise forms.ValidationError(u'Alguno de los campos de nombre se encuentra vacio.')
        if full_name and Employee.objects.filter(full_name=full_name).exists():
            raise forms.ValidationError(u'Ya existe un usuario con tu nombre, contacta al administrador.')
        if employee_code and Employee.objects.filter(code=employee_code).exists():
            raise forms.ValidationError(u'Ya existe un usuario con tu codigo de empleado, contacta al administrador.')
        return clean_data
