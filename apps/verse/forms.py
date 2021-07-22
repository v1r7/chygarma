from django.forms import ModelForm

from apps.verse.models import Category


# class CategoryForm(ModelForm):
#
#     def __init__(self, *args, **kargs):
#         super(CategoryForm, self).__init__(*args, **kargs)
#
#
#     class Meta:
#         model = Category
#         fields = '__all__'