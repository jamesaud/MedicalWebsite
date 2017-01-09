
"""
Returns a list of field names in the model.
"""
def get_field_names(model):
    return [f.name for f in model._meta.fields]
