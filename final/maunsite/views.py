from django.shortcuts import render
from .handler import CrawlerHandler
from django.http import HttpResponse
# Create your views here.
def crawler_page(request):
	handler=CrawlerHandler()
	data=handler.crawl_data()
	handler.save_data(data)
	return HttpResponse("DataBase connected success,please enter 'sd' in the URL")
def show_data(request):
	SiteName=request.GET.get('SiteName')
	handler=CrawlerHandler()
	if (SiteName=='All datas'):
		datas=handler.get_data()
	else:
		datas=handler.search_data(SiteName)
	return render(request,'sd.html',locals())