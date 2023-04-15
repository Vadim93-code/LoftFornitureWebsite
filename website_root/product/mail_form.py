from .models import FormForEmail as Form
from django.forms import ModelForm, TextInput, Textarea


class EmailForm(ModelForm):
    class Meta:
        model = Form
        fields = ["user_name", "user_email", "user_message"]
        widgets = {
            "user_name": TextInput(attrs={
             "class": "user_name_input"
            }),
            "user_email": TextInput(attrs={
                "class": "user_email_input"
            }),
            "user_message": Textarea(attrs={
                "class": "user_email_input"
            }),
        }