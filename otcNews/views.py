from django.views.generic import ListView, DetailView
from django.shortcuts import render
from django.template.loader import render_to_string
from otcNews.models import OtcNews, OtcSecurities

#need datetime to identify last 24 hours worth of news
from datetime import datetime, timedelta

#import modules useful for emailing
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect

#OTC News View
def otcNewsList(request):
    newsItems = OtcNews.objects.filter(category='news').order_by('-datetime')[:10]
    pg_num =list(range(1, 11))
    return render(request, 'otcnews.html', {'newsItems': newsItems,'pg_num':pg_num})
def pg2(request):
    newsItems = OtcNews.objects.filter(category='news').order_by('-datetime')[10:20]
    #pg_num =list(range(1, (int(len(newsItems)/7)+1)+1))
    pg_num = list(range(1, 11))
    return render(request, 'otcnews.html', {'newsItems': newsItems,'pg_num':pg_num})

def pg3(request):
    newsItems = OtcNews.objects.filter(category='news').order_by('-datetime')[20:30]
    #pg_num =list(range(1, (int(len(newsItems)/7)+1)+1))
    pg_num = list(range(1, 11))
    return render(request, 'otcnews.html', {'newsItems': newsItems,'pg_num':pg_num})

def pg4(request):
    newsItems = OtcNews.objects.filter(category='news').order_by('-datetime')[30:40]
    #pg_num =list(range(1, (int(len(newsItems)/7)+1)+1))
    pg_num = list(range(1, 11))
    return render(request, 'otcnews.html', {'newsItems': newsItems,'pg_num':pg_num})

def pg5(request):
    newsItems = OtcNews.objects.filter(category='news').order_by('-datetime')[40:50]
    #pg_num =list(range(1, (int(len(newsItems)/7)+1)+1)
    pg_num = list(range(1, 11))
    return render(request, 'otcnews.html', {'newsItems': newsItems,'pg_num':pg_num})

def pg6(request):
    newsItems = OtcNews.objects.filter(category='news').order_by('-datetime')[50:60]
    #pg_num =list(range(1, (int(len(newsItems)/7)+1)+1)
    pg_num = list(range(1, 11))
    return render(request, 'otcnews.html', {'newsItems': newsItems,'pg_num':pg_num})

def pg7(request):
    newsItems = OtcNews.objects.filter(category='news').order_by('-datetime')[60:70]
    #pg_num =list(range(1, (int(len(newsItems)/7)+1)+1)
    pg_num = list(range(1, 11))
    return render(request, 'otcnews.html', {'newsItems': newsItems,'pg_num':pg_num})

def pg8(request):
    newsItems = OtcNews.objects.filter(category='news').order_by('-datetime')[70:80]
    #pg_num =list(range(1, (int(len(newsItems)/7)+1)+1)
    pg_num = list(range(1, 11))
    return render(request, 'otcnews.html', {'newsItems': newsItems,'pg_num':pg_num})

def pg9(request):
    newsItems = OtcNews.objects.filter(category='news').order_by('-datetime')[80:90]
    #pg_num =list(range(1, (int(len(newsItems)/7)+1)+1)
    pg_num = list(range(1, 11))
    return render(request, 'otcnews.html', {'newsItems': newsItems,'pg_num':pg_num})

def pg10(request):
    newsItems = OtcNews.objects.filter(category='news').order_by('-datetime')[90:100]
    #pg_num =list(range(1, (int(len(newsItems)/7)+1)+1)
    pg_num = list(range(1, 11))
    return render(request, 'otcnews.html', {'newsItems': newsItems,'pg_num':pg_num})


def otcSecuritiesList(request):
    securities = OtcSecurities.objects.all()
    return render(request, 'otcSecurities.html', {'securities': securities})

def sendNews(request):
    newsItems = OtcNews.objects.filter(category='news').order_by('-datetime')
    message = render_to_string('otcnewsEmail.html',{'newsItems': newsItems})
    send_mail("Last 24 hours of OTC News", "Here are the latest OTC news items:", 'jucharles91@gmail.com', ['jcharles18@gsb.columbia.edu'],html_message=message)
    return HttpResponse("sent!")

