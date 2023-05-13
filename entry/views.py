from django.shortcuts import render,redirect
from .models import Entry# importing the model entries
from django.contrib import messages
import datetime
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


def addNew(request):
    current_datetime = datetime.datetime.now()
    if request.method == "POST":
        title = request.POST['title']
        content = request.POST['content']
        date_created = request.POST['date_created']

        new_entry = Entry.objects.create(title=title,content=content,date_created=date_created)
        new_entry.save()
        return redirect('/')

    
    return render(request, "entry/form.html",{'current_datetime': current_datetime})

def edit(request,id):
    current_entry = Entry.objects.get(id = id)
    if request.method == "POST":
        title = request.POST['title']
        content = request.POST['content']
        # date_created = request.POST['date_created']
        current_entry.title = title
        current_entry.content =content
        # current_entry.date_created =date_created
        current_entry.save()
        return redirect('/')
    
    return render(request, "entry/edit.html",{"current_entry":current_entry})

def delete(request,id):
    current = Entry.objects.get(id=id)
    current.delete()
    return redirect('/')




