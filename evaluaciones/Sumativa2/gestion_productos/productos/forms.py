from django import forms
from .models import Producto, Categoria, Marca, Caracteristica

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['codigo', 'nombre', 'precio', 'marca', 'categoria', 'caracteristicas', 'fecha_vencimiento', 'imagen']
        widgets = {
            'fecha_vencimiento': forms.DateInput(attrs={'type': 'date'}),
            'caracteristicas': forms.CheckboxSelectMultiple(),
            'precio': forms.NumberInput(attrs={'step': '0.01', 'min': '0'}),
            'imagen': forms.FileInput(attrs={'class': 'form-control', 'accept': 'image/*'})
        }
        labels = {
            'codigo': 'Código del Producto',
            'nombre': 'Nombre del Producto',
            'precio': 'Precio ($)',
            'marca': 'Marca',
            'categoria': 'Categoría',
            'caracteristicas': 'Características',
            'fecha_vencimiento': 'Fecha de Vencimiento',
            'imagen': 'Imagen del Producto'
        }

class CaracteristicaForm(forms.ModelForm):
    class Meta:
        model = Caracteristica
        fields = ['nombre']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Ingrese el nombre de la característica'})
        }
        labels = {
            'nombre': 'Nombre de la Característica'
        }

    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        if nombre:
            nombre = nombre.strip()
            if len(nombre) < 2:
                raise forms.ValidationError('El nombre debe tener al menos 2 caracteres.')
        return nombre