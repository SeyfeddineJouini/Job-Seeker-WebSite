from django import forms
from .models import formations,categories,files,seeker,programme,month

class dateinput(forms.DateInput):
    input_type = "date"
class formationForm(forms.ModelForm):
    class Meta:
        model = formations
        fields = "__all__"

class catform(forms.ModelForm):
    class Meta:
        model = categories
        fields = "__all__"
class docform(forms.ModelForm):
    class Meta:
        model = files
        fields = "__all__"

class seekerform(forms.ModelForm):
    class Meta:
        model = seeker
        fields = "__all__"

class progform(forms.ModelForm):
    class Meta:
        model=programme
        fields ="__all__"

class monthform(forms.ModelForm):
    class Meta:
        model=month
        fields="__all__"