from django.shortcuts import render,redirect
from createlist.models import To_Do_List
from createlist.forms import To_Do_ListForm

def home(request):

    return render(request, 'home.html')

def _list_id(request):
    list = request.session.session_key
    if not list:
        list = request.session.create()
    return list

def createlist(request):

        return render(request , 'createlist.html')
def add_list(request):
    try:
        list = To_Do_List.objects.get(list_id=_list_id(request)
        ,titel=request.POST['Title'],note=request.POST['Note'])


    except To_Do_List.DoesNotExist:
        list =  To_Do_List.objects.create(
                list_id =_list_id(request),
                titel=request.POST['Title'],
                note=request.POST['Note'],
            )
    list.save()
    return redirect( 'createlist')
def showlist(request):
    list = To_Do_List.objects.filter(list_id=_list_id(request)).order_by('id')
    context = {
        'list' : list,

    }
    return render(request,'showlist.html',context)

def deletelist(request,id):
    list = To_Do_List.objects.get(id =id)
    list.delete()
    return redirect('showlist')
def updatelist(request,id):
    list = To_Do_List.objects.get(id=id)
    context = {
        'list' : list,

    }
    return  render(request,'updatelist.html',context)
def updateField(request,id):
    list = To_Do_List.objects.get(id=id)
    list.titel= request.POST['Title']
    list.note = request.POST['Note']
    list.save()
    return  redirect('showlist')
