from django import forms

from .models import Product


class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True


class MultipleFileField(forms.FileField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", MultipleFileInput())
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        single_file_clean = super().clean
        if isinstance(data, (list, tuple)):
            result = [single_file_clean(d, initial) for d in data]
        else:
            result = [single_file_clean(data, initial)]
        return result

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "name", "price", "description", "discount", "preview"

    images = MultipleFileField(
        required=False,
        label="Изображения товара",
        help_text="Выберите одно или несколько изображений"
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['images'].widget.attrs.update({'class': 'file-input'})


class CSVImportForm(forms.Form):
    csv_field = forms.FileField()


class JSONImportForm(forms.Form):
    json_field = forms.FileField(label="Выберите JSON-файл")
