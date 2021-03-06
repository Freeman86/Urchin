from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from authapp.models import UrchinUser
import django.forms as forms

class ShopUserLoginForm(AuthenticationForm):
    class Meta:
        model = UrchinUser
        fields = ('username', 'password')


class ShopUserRegisterForm(UserCreationForm):
    class Meta:
        model = UrchinUser
        fields = ('username', 'first_name', 'password1', 'password2', 'email',
                  'age', 'avatar')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''

    def clean_age(self):
        data = self.cleaned_data['age']
        if data < 18:
            raise forms.ValidationError("Вы слишком молоды!")

        return data