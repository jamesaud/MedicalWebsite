from django.shortcuts import render
from django.contrib.staticfiles.templatetags.staticfiles import static
from config.static_file_locations import SLIDESHOW_SLIDER_IMAGES as SLIDER_IMAGES
from config.static_file_locations import SLIDESHOW_SLIDER_PATH as SLIDER_PATH

def index(request):
    context = {
        'image_paths': SLIDER_IMAGES,
        'location_to_slider': SLIDER_PATH,
    }

    return render(request, 'pages/home.html', context)

