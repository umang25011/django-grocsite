from django import forms
from .models import OrderItem

class BookForm(forms.Form):
    title = forms.CharField(label="Title", max_length=100)
    kind = forms.ChoiceField(label="Kind", choices=[("pdf", "PDF"), ('printed', 'Printed')])

class OrderItemForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        fields = ["item", "client", "no_of_items"]
        widgets = {
            "client": forms.RadioSelect
        }
        labels = {
            "client" : "Client Name",
            "no_of_items" : "Quantity"
        }

class InterestedForm(forms.Form):
    interested = forms.RadioSelect(choices=[(1, "Yes"), (0, "No")])
    quantity = forms.IntegerField(min_value=1, initial=1)
    comments = forms.CharField(label="Additional Comments", widget=forms.Textarea, required=False)