from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile, Categoty, Product, Slide



class SignUpForm( UserCreationForm ):

    class Meta:
        model = User
        fields = ('username','password1', 'password2',)


class UpdateProfile(forms.ModelForm):

    # course = forms.ModelMultipleChoiceField(queryset=Course.objects.all(), widget=forms.CheckboxSelectMultiple)
    is_super = forms.BooleanField(required=False)

    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'email','phone' ,'country', 'city', 'picture','user', )


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user'].widget.attrs.update({'hidden': True})
        self.fields['first_name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'First Name'})
        self.fields['last_name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Last Name'})
        self.fields['email'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Email'})
        self.fields['country'].widget.attrs.update({'class': 'form-control'})
        self.fields['city'].widget.attrs.update({'class': 'form-control', 'placeholder': 'City'})
        self.fields['phone'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Phone'})


class BookForm(forms.ModelForm):
   
    class Meta:
        model: Product
        fields = ['categoty', 'name', 'image','image1','description','specification','seller','pub_date','available',]
       


class EditBookForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ['categoty', 'name', 'image','description','specification','seller','available'] 


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['categoty'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Category'})
        self.fields['name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Name'})
        self.fields['description'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Description'})
        self.fields['specification'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Specification'})
        self.fields['image'].widget.attrs.update({'class': 'form-control'})
        self.fields['seller'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Seller'})
        self.fields['available'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Available'})
