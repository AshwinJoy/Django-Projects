from django import forms


class VideoForm(forms.Form):
    videoname = forms.CharField(max_length=25,
        widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'Name of video',
        'id':'inputName'
        }))

    videodesc = forms.CharField(widget=forms.Textarea(attrs={
        'class':'form-control',
        'placeholder':'comment',
        'id':'comment',
        'rows':'5'
        }))
