from django.shortcuts import render, redirect
from django.http import HttpResponse
from itess.models import Topic, Information
from accounts.models import Article, Comment, ArticleImages, Board, HashTag
from django.contrib.auth.models import User
import requests , re, json
# Create your views here.

java = Topic.objects.filter(name = '자바')
cloud = Topic.objects.filter(name = '클라우드')
Big_Data = Topic.objects.filter(name = '빅데이터')
IOT = Topic.objects.filter(name = 'IOT')
AI = Topic.objects.filter(name = 'AI')
python = Topic.objects.filter(name = '파이썬')
VR = Topic.objects.filter(name = 'VR')
C = Topic.objects.filter(name = 'C언어')
all_data = Topic.objects.all()

context = {
        'java' : java,
        'cloud' : cloud,
        'Big_Data' : Big_Data,
        'Iot' : IOT,
        'Ai' : AI,
        'python' : python,
        'Vr' : VR,
        'C' : C,
        'all_data' : all_data,
        'title' : {
            '자바': '',
            '클라우드': '',
            '빅데이터':'',
            'IOT':'',
            'AI':'',
            '파이썬':'',
            'VR':'', 
            'C언어':'',
        },
        
    }

def menu(request):
    return render(request, 'window/index.html', context)

def about(request):
    return render(request, 'window/about.html', context)    

def incheon(request):
    return render(request, 'window/incheon.html', context)    

def seoul(request):
    return render(request, 'window/seoul.html', context)    

def zzim(request):
    id =request.user.id
    info_id = request.POST['info']
    info = Information.objects.get(id=info_id)
    info.zzim_user.add(id)
    return HttpResponse('', status=200)   

def myfage(request):
    user = request.user
    l = request.user.zzim_info.all()
    
    print(l)
    context2={
        'myfages':l,
       
    }
    return render(request, 'window/zzim.html', context2)

def show(request, topic_title):        
    if( topic_title == "자바" ):
        return render(request, 'window/java.html', context)
    if( topic_title == "클라우드" ):
        return render(request, 'window/cloud.html', context)
    if( topic_title == "빅데이터" ):
        return render(request, 'window/bigdata.html', context)
    if( topic_title == "파이썬" ):
        return render(request, 'window/python.html', context)
    if( topic_title == "Iot" ):
        return render(request, 'window/IOT.html', context)
    if( topic_title == "Ai" ):
        return render(request, 'window/AI.html', context)
    if( topic_title == "C언어" ):
        return render(request, 'window/c.html', context)
    if( topic_title == "Vr" ):
        return render(request, 'window/vr.html', context)

# 여기다가 댓글 달기 구현
def comment(request, topic_title):
    return render(request, 'window/index.html', context) 


# 복붙...

def edit(request, article_id):
    article = Article.objects.get(id=article_id)
    if article.is_permitted(request.user.id):
        if request.method == "POST":
            article.contents = request.POST["contents"]
            article.save()
            return redirect('articles')
        else:
            context = {
                'article': article
            }
            return render(request, 'article/edit.html', context)
    else:
        return redirect('articles')

def delete(request, article_id):
    article = Article.objects.get(id=article_id)
    if article.is_permitted(request.user.id):
        article.delete()
        return redirect('articles')
    else:
        return redirect('articles')

def comments(request):
    if request.method == "POST":
        if request.user.is_authenticated :
            contents = request.POST["contents"]
            article_id = request.POST["article_id"]
        
            if request.POST["form_method"] == "create":
                comment = Comment()
                # 첫번째 comment.user_id = request.user.id
            elif request.POST["form_method"] == "edit":
                comment_id = request.POST["comment_id"]
                comment = Comment.objects.get(id=comment_id)
                if comment.user_id != request.user.id:
                    return HttpResponse('', status=401)   
            comment.contents = contents
            comment.article_id = article_id
            comment.user_id = request.user.id
            comment.save()
            context = {
                'method': request.POST["form_method"],
                'comment': comment.contents,
                'username': comment.user.username,
                'comment_id': comment.id,
                'article_id': comment.article_id,
            }
            return HttpResponse(json.dumps(context), content_type='application/json')
        else:
            context = {
                'status': 401,
                'message': '로그인이 필요합니다.'
            }
            return HttpResponse(json.dumps(context), status=401, content_type="application/json")

def delete_comment(request):
    if request.method == "POST":
        comment_id = request.POST["comment_id"]
        comment = Comment.objects.get(id=comment_id)
        if comment.user_id == request.user.id:
            comment.delete()
            return HttpResponse('', status=204)
        else :
            return HttpResponse('' , status=401)

def edit_comment(request, comment_id):
    comment = Comment.objects.get(id=comment_id)
    if request.method == "POST":
        comment.contents = request.POST["contents"]
        comment.save()
        return redirect('articles')
    else:
        context = {
            'comment': comment
        }
        return render(request, 'comment/edit.html', context)

# 복붙...



#def link(request):
#    if request.method == "POST":
#        data = request.POST["link_address"]
#        print(data)
#        return HttpResponse(data)
          
    #print(request)
    #if request.method == "POST":
    #    data = request.POST["link_address"]
        # print(data.split('?'))
        # return HttpResponse(data.split('?')[1])
     