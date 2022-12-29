from django.http import JsonResponse
from django.shortcuts import redirect, render
from . import forms
from feedback.models import GalleryIdea
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.core import serializers

# Create your views here.


OBJECTS_ON_PAGE = 2


def submit_idea(request):
    if request.method == "POST":
        form = forms.GalleryIdea(request.POST)
        if form.is_valid():
            form.save()
    return redirect("gallery")


def results(request):
    feedback_objs = GalleryIdea.objects.filter()

    paginator = Paginator(feedback_objs, OBJECTS_ON_PAGE)
    page = request.GET.get('page', 1)

    try:
        results_objs = paginator.page(page)
    except PageNotAnInteger:
        results_objs = paginator.page(1)
    except EmptyPage:
        results_objs = paginator.page(paginator.num_pages)

    page_list = results_objs.paginator.page_range

    return render(request, "results.html", {"page_list": page_list})


def paginate(request):
    page = int(request.POST.get("page"))

    starting_number = (page - 1) * OBJECTS_ON_PAGE
    ending_number = page * OBJECTS_ON_PAGE

    result = GalleryIdea.objects.filter()[starting_number:ending_number]

    data = serializers.serialize('json', result)

    return JsonResponse(data, safe=False)
