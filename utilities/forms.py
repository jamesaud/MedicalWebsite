from django import forms

EMPTY_LABEL_DEFAULT = '-----'

class NoColonForm(forms.Form):
    """
    Remove ":" character from labels, which are default in Django.
    """
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')
        super(NoColonForm, self).__init__(*args, **kwargs)


class AutoPlaceholderForm(forms.Form):
    """
    Makes all placeholders default to the label of its field.
    Is overwritten by specifying placeholder manually in attrs.
    """
    def __init__(self, *args, **kwargs):
        super(AutoPlaceholderForm, self).__init__(*args, **kwargs)
        for field_name in self.fields:
            field = self.fields.get(field_name)

            if field_name and not field.widget.attrs.get('placeholder'):
                    field.widget.attrs.update({'placeholder': field.label})


# Taken from https://gist.github.com/davidbgk/651080
class EmptyChoiceField(forms.ChoiceField):
    """
    Provides a default empty label in a choice field without having to specify it in the Model.
    Specify the 'empty_label' argument to set a custom empty label.
    """
    def __init__(self, choices=(), help_text=None, empty_label=None, required=False, widget=None, label=None,
                 initial=None, *args, **kwargs):
        # prepend an empty label if it exists (and field is not required!)
        if empty_label is None:
            choices = tuple([(u'', EMPTY_LABEL_DEFAULT)] + list(choices))
        else:
            choices = tuple([(u'', empty_label)] + list(choices))

        super(EmptyChoiceField, self).__init__(choices=choices, required=required, widget=widget, label=label,
                                        initial=initial, help_text=help_text, *args, **kwargs)



class EmptyTextarea(forms.Textarea):
    """
    Removes Django's default text area cols and rows.
    """
    def __init__(self, *args, **kwargs):
        # Update the attrs
        if kwargs.get('attrs'):
            kwargs['attrs'].update({'rows': '0', 'cols': '0'})
        else:
            kwargs['attrs'] = {'rows': '0', 'cols': '0'}
        super(EmptyTextarea, self).__init__(*args, **kwargs)

