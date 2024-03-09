from django.shortcuts import render, redirect
from .models import *


def image_gallery(request):
    msg = ''
    collections = ImageCollection.objects.all()
    if request.method == 'POST':
        images = request.FILES.getlist('images')
        collection = request.POST.get('collection')
        for image in images:
            new_image = ImageGallery(image=image, collection_id=collection)
            new_image.save()
        msg = 'Images uploaded successfully'
    context = {"msg": msg, "collections": collections}
    return render(request, 'files/image_gallery.html', context)


def collection_gallery_view(request):
    collections = ImageCollection.objects.all()
    images = ImageGallery.objects.all()
    context = {"images": images, "collections": collections}
    return render(request, 'files/collection_gallery.html', context)


def image_detail_view(request, image_id):
    image = ImageGallery.objects.get(id=image_id)
    context = {"image": image}
    return render(request, 'files/image_detail.html', context)


def file_uploads_view(request):
    msg, new_file, file = '', '', ''
    categories = MediaCategory.objects.all()
    if request.method == 'POST':
        file = request.FILES.get('files')
        print(file)
        category = request.POST.get('category')
        description = request.POST.get('description')
        _date = request.POST.get('_date')
        new_file = MediaLibrary.objects.create(
            file=file, category_id=category, _date=_date, description=description)
        return redirect('file_uploads')
        if new_file:
            msg = 'Images uploaded successfully'
        else:
            msg = 'Failed'
    context = {"msg": msg, "categories": categories}
    return render(request, 'files/file_upload.html', context)
