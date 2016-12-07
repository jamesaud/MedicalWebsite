from django import forms

# REMOVE the ":" from the labels
class NoColonForm(forms.Form):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')
        super(NoColonForm, self).__init__(*args, **kwargs)


class AutoPlaceholderForm(forms.Form):
    excluded_placeholder_fields = set()
    def __init__(self, *args, **kwargs):
        super(AutoPlaceholderForm, self).__init__(*args, **kwargs)
        for field_name in self.fields:
            field = self.fields.get(field_name)
            # It's important to check if field.label exists to ensure no errors
            if field.label and (field.label.lower() not in self.excluded_placeholder_fields):
                    field.widget = forms.TextInput(attrs={'placeholder': field.label})
