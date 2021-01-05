from django import forms
from .models import ThQuestion

class ThQuestionForm(forms.ModelForm):

    class Meta:
        model = ThQuestion
        fields = [field.name for field in ThQuestion._meta.get_fields()]

