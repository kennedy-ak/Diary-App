from django.shortcuts import render
from .models import Entry# importing the model entries


# Create your views here.



def List(request):
    # getting all the entries in the dataset and ordering them by the time they were created
    all_entries = Entry.objects.all().order_by('-date_created')
    return render(request, "entry/list.html", {"all_entries":all_entries})


# def Detail(request,id):
#     ent = Entry.objects.get(id=id)
#     return render(request, "entry/detail.html",{"entry":ent})


def detail(request, id):
    entry = Entry.objects.get(id=id)
    context = {'entry': entry}
    return render(request, 'entry/detail.html', context)

