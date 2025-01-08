from .models import Comment
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Row, Column
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.layout = Layout(
            Row(Column('body', css_class='form-group col-12')),
        )
        self.fields['body'].widget.attrs = {
            'rows': 5,
            'class': 'dark-bg'
            }