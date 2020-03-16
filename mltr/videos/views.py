from django.shortcuts import render,get_object_or_404
from .models import Video
from .forms import VideoForm
import cv2
from .CarmaCam.model._yolo import YoloDetector
from django.conf import settings
from PIL import Image
import json
import os

# Create your views here.
def  video_detail_view(request, video_id):
    obj = get_object_or_404(Video, id=video_id)
    context = {
        "object": obj
    }
    return render(request, "video/detail.html", context)


def video_update_view(request, video_id):
    obj = get_object_or_404(Video, id=video_id)
    form = VideoForm(request.POST or None, request.FILES or None,instance=obj)
    if form.is_valid():
        form.save()
    context = {
        "form":form
    }
    return render(request, "video/create.html", context)


def video_create_view(request):
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES)
        uploaded_file = request.FILES
        if form.is_valid():
            form.save()

            # model_instance.name = uploaded_file['image'].name
            # model_instance.save()
    else:
        form = VideoForm()
    context = {
        "form":form
    }

    return render(request, "video/create.html", context)


def video_list_view(request):
    queryset = Video.objects.all()
    context = {
        "object_list": queryset
    }
    return render(request, "video/show.html", context)


def  video_yolo_view(request, video_id):
    obj = get_object_or_404(Video, id=video_id)
    inputfilename = obj.video
    path = settings.MEDIA_ROOT+'/result_json/'+obj.title+'.json'
    if not os.path.isfile(path):
        vidcap = cv2.VideoCapture(settings.MEDIA_ROOT+'/'+str(inputfilename))
        success, image = vidcap.read()
        i = 0
        res={}
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Be sure to use lower case
        print(image.shape)
        detector = YoloDetector((720., 960.))
        print(type(image))
        while success:
            img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            print(type(img))
            im_pil = Image.fromarray(img)
            # out_scores, out_boxes, out_classes, image = detector.detect(im_pil)
            # res[i] = {'out_scores': out_scores.tolist(), 'out_boxes': out_boxes.tolist(),
            #           'out_classes': out_classes.tolist()}
            i+=1
        with open(settings.MEDIA_ROOT+'/result_json/'+obj.title+'.json', 'w') as fp:
            json.dump(res, fp)
    context = {
        "path": path
    }
    return render(request, "video/yolo.html", context)

