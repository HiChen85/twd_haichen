from django import forms
from rango.models import Category, Page

class CategoryForm(forms.ModelForm):
    name = forms.CharField(max_length=128, help_text='Please enter the category name.', label='Name')
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Category
        fields = ('name',)



class PageForm(forms.ModelForm):
    title = forms.CharField(max_length=128, help_text='Please enter the title of the page.')
    url = forms.URLField(max_length=200, help_text='Please enter the url of the page.')
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

    class Meta():
        model = Page
        exclude = ('category',)

    def clean(self):
        cleaned_data = self.cleaned_data
        url = cleaned_data.get('url')
        if url:
            if url.startswith('http://') or url.startswith('https://'):
                print(url)
                return cleaned_data
            else:
                url  = 'http://' + url
                cleaned_data['url'] = url
                print("不是以 http 或 https 开头的最终数据:", cleaned_data['url'])
                return cleaned_data
