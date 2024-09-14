from django.shortcuts import render, redirect
from django.db.models import Q

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
    msg, file = '', ''
    categories = MediaCategory.objects.all()
    if request.method == 'POST':
        file = request.FILES.get('files')
        category = request.POST.get('category')
        description = request.POST.get('description')
        file_date = request.POST.get('_date')
        MediaLibrary.objects.create(
            file=file, category_id=category, file_date=file_date, description=description)
        msg = 'Images uploaded successfully'
        return redirect('file_uploads')
    context = {"msg": msg, "categories": categories}
    return render(request, 'files/file_upload.html', context)


def file_list_view(request):
    size = 0
    try:
        query = request.GET.get('q')
    except:
        query = None
    lookups = (Q(file__icontains=query) | Q(file_date__month__iexact=query) |
               Q(file_date__year__iexact=query)) | Q(description__icontains=query)
    if query:
        files = MediaLibrary.objects.filter(lookups).distinct()
        for file in files:
            size = float(file.file.size) / 1048 / 1000
        context = {'files': files, 'size': size, 'query': query}
    else:
        files = MediaLibrary.objects.all().order_by('-file_date')[:21]
        a = "Please enter a search parameter!"
        context = {'files': files, 'size': size, 'query': a}
    return render(request, 'files/file_list.html', context)
