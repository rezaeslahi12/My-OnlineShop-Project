from django import forms
class addpostform (forms.Form):
    P_name = forms.CharField(label='Productname',max_length=200)
    discrption = forms.CharField(label='discrption',widget=forms.Textarea)
    price = forms.IntegerField(label='price')
    image = forms.ImageField()