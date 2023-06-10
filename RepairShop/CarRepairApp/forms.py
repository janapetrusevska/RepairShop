from django import forms
from .models import *

class RepairForm(forms.ModelForm):
    code = forms.CharField(max_length=5)

    def __init__(self, *args, **kwargs):
        super(RepairForm, self).__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs["class"] = "form-control"

    class Meta:
        model = ScheduledRepair
        exclude = ("user",)