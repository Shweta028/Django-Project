from django import forms
from django.contrib.auth.models import User
from .models import DeviceGroup, Device

# Create your models here.

class UserForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(), max_length=20, required=True)
    email = forms.EmailField(widget=forms.EmailInput(), required=True)
    password = forms.CharField(widget=forms.PasswordInput(), min_length=4, required=True)
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class LoginForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(), max_length=20, required=True)
    password = forms.CharField(widget=forms.PasswordInput(), min_length=4, required=True)
    class Meta:
        model = User
        fields = ['username', 'password']

class devicegroup_form(forms.ModelForm):
    groupname = forms.CharField(widget=forms.TextInput(), max_length=20, required=True)
    description = forms.CharField(widget=forms.TextInput(), max_length=200, required=False)

    class Meta():
        model = DeviceGroup
        fields = ['groupname', 'description']


class device_form(forms.ModelForm):
    IP_Address = forms.GenericIPAddressField(widget=forms.GenericIPAddressField, required=True)
    hostname = forms.CharField(widget=forms.TextInput(), max_length=30, required=True)
    devicegroups = forms.ModelMultipleChoiceField(widget=forms.CheckboxInput(), required=False, queryset=DeviceGroup.objects.all())

    class Meta():
        model = Device
        fields = ['IP_Address', 'hostname', 'devicegroups']

    def __init__(self, *args, **kwargs):
        self.fields['devicegroups'] = forms.ModelMultipleChoiceField(queryset=DeviceGroup.objects.all(), widget=forms.CheckboxInput, required=False )
        if kwargs.get('instance'):
            initial = kwargs.setdefault('initial', {})
            if kwargs['instance'].devicegroups.all():
                initial['devicegroups'] = kwargs['instance'].devicegroups.all()
            else:
                initial['devicegroups'] =None

        forms.ModelForm.__init__(self, *args, **kwargs)

    def save(self):
        IP_Address = self.cleaned_data.pop('IP_Address')
        hostname = self.cleaned_data.pop('hostname')
        group = self.cleaned_data.pop('group')
        u = super().save()
        u.devicegroups.add([group])
        u.set_ipaddress(IP_Address)
        u.set_hostname(hostname)
        u.save()
        return u





