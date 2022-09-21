from email import message
from django.shortcuts import render
from mywatchlist.models import MyWatchList
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
def show_mywatchlist(request):
    data = MyWatchList.objects.all()
    data_sudah_ditonton = MyWatchList.objects.filter(watched=True).count()
    data_belum_ditonton = MyWatchList.objects.filter(watched=False).count()
    if (data_sudah_ditonton >= data_belum_ditonton):
        message = "Selamat, kamu sudah banyak menonton!"
    else:
        message = "Wah, kamu masih sedikit menonton!"

    context = {
        'movie_list': data,
        'nama': 'Devina Hana',
        'id': 2106751032,
        'message': message
    }
    return render(request, "mywatchlist.html", context)

def show_mywatchlist_xml(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_mywatchlist_json(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
