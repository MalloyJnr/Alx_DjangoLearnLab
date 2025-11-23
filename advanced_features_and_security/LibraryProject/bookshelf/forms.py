from django import forms


class ExampleForm(forms.Form):
    """
    Example form for demonstrating CSRF protection and safe form handling.
    """
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)


class SearchForm(forms.Form):
    """
    Search form with user input validation to prevent injection attacks.
    """
    query = forms.CharField(required=False, max_length=100)
