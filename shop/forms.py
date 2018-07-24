from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('name', 'amount')
        widgets = {
            'name': forms.TextInput(attrs={'readonly': 'readonly'}),    # 읽기 전용 속성으로 만듦
            'amount': forms.TextInput(attrs={'readonly': 'readonly'}),
        }
