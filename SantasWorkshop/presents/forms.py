from django import forms
from SantasWorkshop.presents.models import Present
# Create your views here.

class PresentBaseForm(forms.ModelForm):
    class Meta:
        model = Present
        fields = ('name', 'description', 'image')


class PresentAddForm(PresentBaseForm):
    pass


class PresentEditForm(PresentBaseForm):
    pass

class PhotoDeleteForm(PresentBaseForm):
    pass