from .models import Post
import requests
import json

class CrawlerHandler(object):
	def __init__(self,u='http://opendata2.epa.gov.tw/UV/UV.json'):
		self.u=u

	def crawl_data(self):
		rs=requests.get(self.u)
		datas=rs.json()
		return datas
	def check_data(self,data):
		d=Post.objects.filter(SiteName=data["SiteName"])
		if len(d)>0:
			return  True
		return False
	def save_data(self,datas):
		for data in datas:
			if(self.check_data(data)):
			    d=Post.objects.get(SiteName=data["SiteName"])
			    d.UVI=data["UVI"]
			    d.PublishAgency=data["PublishAgency"]
			    d.WGS84Lon=data["WGS84Lon"]
			    d.County=data["County"]
			    d.WGS84Lat=data["WGS84Lat"]
			    d.PublishTime=data["PublishTime"]
			    d.save()
			else:    
 			    d=Post(SiteName=data["SiteName"],UVI=data["UVI"],PublishAgency=data["PublishAgency"],WGS84Lon=data["WGS84Lon"],County=data["County"],WGS84Lat=data["WGS84Lat"],PublishTime=data["PublishTime"])
 			    d.save()
	def get_data(self):
		datas=Post.objects.all()
		return datas
	def search_data(self,area):
		datas=Post.objects.filter(SiteName=area)
		return datas