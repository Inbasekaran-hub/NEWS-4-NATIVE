from django.shortcuts import render
from .logic import NewsReader
from .models import NewsStore
import os

def index(request):
    if request.method == "POST":
        obj = NewsReader()
        print(obj.language_selecter(request.POST["lang"], request.POST["OutLang"]))
        try:
            os.chdir("static")
        except FileNotFoundError: pass
        obj.conVert()
        NewsStore( orginal_news=" ".join(obj.source_lang_list), converted_news=" ".join(obj.sCointain) ).save()
        obj.voice()

        db = NewsStore.objects.all()[::-1][0]
        data ={
            "source_news": db.orginal_news.split("; "),
            "destin_news": db.converted_news.split("; ")
        }

        sour_news = db.orginal_news.split("; ")
        dest_news = db.converted_news.split("; ")
        content = zip(sour_news,dest_news)
        return render(request, "translate.html",locals())
    return render(request, "index.html")

def convert(request):
    return render(request, "translate.html",locals())