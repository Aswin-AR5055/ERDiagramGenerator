from django import forms

class ERInputForm(forms.Form):
    er_text = forms.CharField(
    label='Enter ER Diagram Description',
    widget=forms.Textarea(attrs={
        'rows': 10,
        'cols': 60,
        'placeholder': 'Customer(id:int, name:string, email:string)\nOrder(id:int, date:string, amount:int)\nCustomer -> Order'
    }),
)
