from django import forms

from .models import Articles


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'content']

    def clean(self):
        data = self.cleaned_data
        title = data.get('title')
        qs = Articles.objects.filter(title__icontains=title)
        if qs.exists():
            self.add_error("title", f"{title}" "is already in use. Please add "
                                    "another title.")
        return data


class ArticleFormOld(forms.Form):
    title = forms.CharField()
    content = forms.CharField()

    def clean_title(self):
        cleaned_data = self.cleaned_data
        print("cleaned data", cleaned_data)
        title = cleaned_data.get('title')
        print("title", title)
        return title

