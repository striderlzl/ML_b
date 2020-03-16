from django import forms
from .models import Video

class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = [
            'title',
            'description',
            'video',
        ]

    def clean_video(self, *args, **kargs):
        video = self.cleaned_data.get('video')
        if video is None:
            raise forms.ValidationError("please attach video")
        return video