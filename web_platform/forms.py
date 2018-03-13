from django import forms
class devices_list(forms.Form):
    devices_list_and=forms.IntegerField()
    devices_list_ios=[]
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)