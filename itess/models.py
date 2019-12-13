from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from imagekit.models import ImageSpecField,ProcessedImageField
from imagekit.processors import ResizeToFill, Thumbnail
import re
# Create your models here.

class Topic(models.Model):
    name = models.CharField(max_length=100)

    
class Information(models.Model):
    title = models.CharField(max_length=300)
    academy = models.CharField(max_length=300)
    info = models.CharField(max_length=300)
    
    link = models.CharField(max_length=300) 
    academy_title = models.CharField(max_length=300)
    academy_num= models.CharField(max_length=300)
    training_date = models.CharField(max_length= 300)
    pay = models.CharField(max_length= 300)
    training_wage = models.CharField(max_length= 300)
    people = models.CharField(max_length= 300)
    training_time = models.CharField(max_length= 300)
    
    code = models.CharField(max_length=100)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='courses')
    zzim_user = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="zzim_info")
class imgdata(models.Model):
     image_url = models.CharField(max_length=300)

def get_data(*keywords):
    import requests
    from bs4 import BeautifulSoup
    
    for keyword in keywords:
        if not Topic.objects.filter(name=keyword):#없으면
            Topic.objects.create(name=keyword)#없으면 생성
        topic = Topic.objects.get(name=keyword)
        for i in range(1, 100):
            res = requests.post("http://hrd.go.kr/hrdp/co/pcoeo/PCOEO0101T.do", params={
                'searchTotalKeyword': topic.name,
                'pageIndex': i, 
            })
            data = BeautifulSoup(res.text, 'html.parser')
            if data.select('p[class=name]'):# 값이 있으면 
                titles = data.select('p[class=name]')
                academys = data.select('dl[class= academy]')
                infos = data.select('ul[class=info]')

                links =  data.select("p.name > a ") 
                academy_titles = data.select("dl.academy >dt:nth-child(1)") 
                academy_nums = data.select("dl.academy > dd")
                training_datas = data.select("ul[class = info] > li:nth-child(1)")
                pays = data.select("ul[class = info] > li:nth-child(3)")
                training_wages = data.select("ul[class = info] > li:nth-child(4)")
                peoples = data.select("ul[class = info] > li:nth-child(5)")
                training_times = data.select("ul.info.detail>li:nth-child(1)")
                
                for i in range(len(titles)):
                    
                    link_code1 = links[i].get('onclick')[30:-29]
                    link_code2 = links[i].get('onclick')[50:-25]
                    link_code3 = links[i].get('onclick')[62:-2]

                    Information.objects.create(
                        title= titles[i].text.strip(),
                        academy= academys[i].text.strip(),
                        info = infos[i].text.strip(),
                        link = f'https://hrd.go.kr/hrdp/co/pcobo/PCOBO0100P.do?tracseId={link_code1}&tracseTme={link_code2}&crseTracseSe=C0061&trainstCstmrId={link_code3}#undefined',
                        academy_title = academy_titles[i].text.strip(),
                        academy_num = academy_nums[i].text.split()[1],
                        training_date = training_datas[i].text.strip(),
                        pay = pays[i].text.strip(),
                    #   training_wage = training_wages[i].text.strip(),
                        people = peoples[i].text.strip(),
                        training_time = training_times[i].text.strip(),
                        topic = topic,
                    ) 
                
            else:
                break