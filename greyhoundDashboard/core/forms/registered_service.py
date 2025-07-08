
from django import forms
from django.forms import ModelForm
from django.utils.safestring import mark_safe

from core.models import RegisteredService

class URLInputWithHint(forms.URLInput):
    def render(self, name, value, attrs=None, renderer=None):
        original = super().render(name, value, attrs, renderer)
        extra = '<div id="url-helper" class="form-text tool-description ">Enter a full URL including https:// or http://</div>'
        return mark_safe(original + extra)

class ServiceTypeInputWithDescriptionDiv(forms.Select):
    def render(self, name, value, attrs=None, renderer=None):

        attrs = attrs or {}

        # Inject your HTMX attributes into the <select>
        attrs.update({
            'hx-get': mark_safe('/component/service-description'),
            'hx-trigger': 'change',
            'hx-target': '#description-helper',
        })

        original = super().render(name, value, attrs, renderer)
        extra = '<div id="description-helper" class="form-text tool-description ">Enter a full URL including https:// or http://</div>'
        return mark_safe(original + extra)

class NewRegisteredServiceForm(ModelForm):
    class Meta:
        model = RegisteredService
        fields = ['id', 'name', 'service_type', 'url']
        widgets = {
            'id': forms.HiddenInput(),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'service_type': ServiceTypeInputWithDescriptionDiv(attrs={'class': 'form-control'}),
            'url': URLInputWithHint(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def is_valid(self):
        is_valid = super().is_valid()

        # check url to make sure it is a valid pattern
        if is_valid:
            url = self.cleaned_data.get('url')
            if not url.startswith(('http://', 'https://')):
                self.add_error('url', 'URL must start with http:// or https://')
                is_valid = False

        return is_valid