#coding=utf8
from django.shortcuts import render, render_to_response
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib import auth
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from forms import LogForm, ProfileForm, StrategyForm, HopeForm, ActForm
from models import Log, Profile, Strategy, Hope, Messages, Activity
from PIL import Image
from django.utils.timezone import timedelta
import datetime
from django.db.models import Q
# Create your views here.
# the test
# the second git test
@csrf_exempt
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect("/login/")
    else:
        form = UserCreationForm()
    return render_to_response("register.html", {'form': form,})
@csrf_exempt
@login_required
def index(request):
    u = request.user
    username = u.username
    p = Profile.objects.get_or_create(user = u)[0]
    img_mark = p.is_img
    logs = u.log_set.all().order_by('-date')
    logs_num = len(logs)
    strgys = Strategy.objects.all()
    info_num = len(Messages.objects.filter(go = u, is_read = False))
    messages = Messages.objects.filter(go = u, is_read = False).order_by('-date')
    
    friends = p.friend.all()
    friends_u = []
    for friend in friends:
        friends_u.append(friend.user)
    friends_logs = Log.objects.filter(user__in = friends_u).order_by('-date')
    
    return render_to_response("index.html", locals())

@csrf_exempt
@login_required
def ensure_logout(request):
    u = request.user
    username = u.username
    p = Profile.objects.get_or_create(user = u)[0]
    img_mark = p.is_img
    if request.method == 'POST':
        if request.POST.has_key('ensure'):
            auth.logout(request)
            return HttpResponseRedirect("/login/")
        else:
            return HttpResponseRedirect("/index/")
    return render_to_response("logout.html", locals())

@csrf_exempt
@login_required
def addlog(request):
    u = request.user
    username = u.username
    p = Profile.objects.get_or_create(user = u)[0]
    img_mark = p.is_img
    if request.method == 'POST':
        form = LogForm(request.POST)
        if form.is_valid():
            log = Log()
            log.content = form.cleaned_data["content"]
            log.title = form.cleaned_data["title"]
            log.user = request.user
            log.save()
            return HttpResponseRedirect("/is_add_logimg/" + str(log.logID))
    else:
        form = LogForm()
    return render_to_response('addlog.html', locals())

@csrf_exempt
@login_required

def mylog(request, id):
    u = request.user
    username = u.username
    p = Profile.objects.get_or_create(user = u)[0]
    img_mark = p.is_img
    mylog = u.log_set.all().get(logID = id)
    logs = u.log_set.all().order_by('-date') 
    return render_to_response('mylog.html', locals())
@csrf_exempt
@login_required
def myprofile(request):
    u = request.user
    #User.profile = property(lambda u: Profile.objects.get_or_create(user = u)[0])
    p = Profile.objects.get_or_create(user = u)[0]
    username = p.user.username
    img_mark = p.is_img
    if request.method == 'POST':       
        form = ProfileForm(request.POST, instance = p)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/profile/")
    else:
        form = ProfileForm(instance = p)
    return render_to_response('profile.html', locals())

@csrf_exempt
@login_required
def passwd_change(request):
    u = request.user
    username = u.username
    p = Profile.objects.get_or_create(user = u)[0]
    img_mark = p.is_img
    if request.method == 'POST':
        if request.POST.has_key('cancel'):
            return HttpResponseRedirect("/index/")
        else:
            old_passwd = request.POST.get('old_passwd')
            new_passwd = request.POST.get('new_passwd')
            new_passwd2 = request.POST.get('new_passwd2')
            if u.check_password(old_passwd):
                if new_passwd == new_passwd2:
                    u.set_password(new_passwd)
                    u.save()
                    return HttpResponseRedirect("/index/")
                else:
                    return HttpResponseRedirect("/passwd_change/")
            else:
                return HttpResponseRedirect("/passwd_change/")
    return render_to_response('passwd_change.html', locals())
            
  
@csrf_exempt
@login_required
def img(request):
    u = request.user
    username = u.username
    p = Profile.objects.get_or_create(user = u)[0]
    img_mark = p.is_img
    if request.method == 'POST':       
        if 'image' in request.FILES:
            image=request.FILES["image"]
            img=Image.open(image)
            img.thumbnail((112,54),Image.ANTIALIAS)
            name='./static/imgs/'+username+'.png'
            img.save(name,"png")
            p.is_img = 1
            p.save()
            return HttpResponseRedirect("/index/")
    return render_to_response('img.html', locals())
    '''
    if request.method == 'POST':
        form = ImgForm(request.POST, request.FILES)
        if form.is_valid():
            p.img = form.cleaned_data['image']
            p.save()
            return HttpResponseRedirect("/index/")
    return render_to_response('img.html', locals())
'''
@csrf_exempt
@login_required
def addstrgy(request):
    u = request.user
    username = u.username
    p = Profile.objects.get_or_create(user = u)[0]
    img_mark = p.is_img
    if request.method == 'POST':
        form = StrategyForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/index/")
    else:
        form = StrategyForm()
    return render_to_response('addstrgy.html', locals())
    
@csrf_exempt
@login_required

def showstrgy(request, id):
    u = request.user
    username = u.username
    p = Profile.objects.get_or_create(user = u)[0]
    img_mark = p.is_img
    strgy = Strategy.objects.all().get(strgyID = id)
    strgys = Strategy.objects.all().order_by('date')
    return render_to_response('showstrgy.html', locals())

@csrf_exempt
@login_required

def myhope(request):
    u = request.user
    username = u.username
    p = Profile.objects.get_or_create(user = u)[0]
    img_mark = p.is_img
    h = Hope.objects.get_or_create(user = u)[0]
    if request.method == 'POST':       
        form = HopeForm(request.POST, instance = h)
        if form.is_valid():
            form.save()
            h.is_commit = True
            h.save()
            return HttpResponseRedirect("/myhope/")
    else:
        form = HopeForm(instance = h)
    return render_to_response('myhope.html', locals())
    
@csrf_exempt
@login_required
def design(request):
    u = request.user
    username = u.username
    p = Profile.objects.get_or_create(user = u)[0]
    img_mark = p.is_img
    return render_to_response('design.html', locals())
    
@csrf_exempt
@login_required
def result(request, id1, id2):
    u = request.user
    username = u.username
    p = Profile.objects.get_or_create(user = u)[0]
    img_mark = p.is_img
    home1 = id1
    home2 = id2
    return render_to_response('result.html', locals())

@csrf_exempt
@login_required
def advice(request):
    u = request.user
    username = u.username
    p = Profile.objects.get_or_create(user = u)[0]
    img_mark = p.is_img
    h = Hope.objects.get_or_create(user = u)[0]
    if h.is_commit == True:
        hlist = Hope.objects.filter(home__contains = h.home[0:1]).filter(goal__contains = h.goal[0:1])\
                .exclude(Q(end_date__lt = h.start_date)|Q(start_date__gt = h.end_date))
    return render_to_response('advice.html', locals())

@csrf_exempt
@login_required
def my_advice_user(request, id):
    u = request.user
    username = u.username
    p = Profile.objects.get_or_create(user = u)[0]
    img_mark = p.is_img
    h = Hope.objects.get_or_create(user = u)[0]
    hlist = Hope.objects.filter(home__contains = h.home[0:1]).filter(goal__contains = h.goal[0:1])\
            .exclude(Q(end_date__lt = h.start_date)|Q(start_date__gt = h.end_date))
    target_user = User.objects.get(username = id)
    target_hope = target_user.hope
    if target_user.profile in p.friend.all():
        is_friend = True
    else:
        is_friend = False
    print is_friend
    if request.method == 'GET':
        if request.GET.has_key('friend'):
            mf = Messages()
            mf.go = target_user
            mf.come = u
            mf.is_freq = True
            mf.is_req = True
            mf.save()
        if request.GET.has_key('travel'):
            mt = Messages()
            mt.go = target_user
            mt.come = u
            mt.is_freq = False
            mf.is_req = True
            mt.save() 
    return render_to_response('my_advice_user.html', locals())


@csrf_exempt
@login_required
def deal_msg(request, come_username, msgID):
    u = request.user
    username = u.username
    p = Profile.objects.get_or_create(user = u)[0]
    img_mark = p.is_img
    friend_u = User.objects.get(username = come_username)
    friend_p = Profile.objects.get_or_create(user = friend_u)[0]
    friend_h = Hope.objects.get_or_create(user = friend_u)[0]
    if friend_p in p.friend.all():
        is_friend = True
    else:
        is_friend = False
    target_msg = Messages.objects.get(msgID = msgID)
    if request.method == 'GET':
        if target_msg.is_freq:
            print 1
            if request.GET.has_key('cancelf'):
                print 2
                message_readed = Messages.objects.filter(come = friend_u, go = u)
                for message in message_readed:
                    message.is_read = True
                    message.save()
                    
            elif request.GET.has_key('ensuref'):
                print 3
                p.friend.add(friend_p)
                message_readed = Messages.objects.filter(come = friend_u, go = u)
                for message in message_readed:
                    message.is_read = True
                    message.save()
                    
            result_m = Messages.objects.create(
                go = friend_u,
                come = u,
                is_freq = True,
                is_req = False
                )
        else:
            pass
    return render_to_response('deal_msg.html', locals())
    
@csrf_exempt
@login_required    
def is_add_logimg(request, id):
    u = request.user
    username = u.username
    p = Profile.objects.get_or_create(user = u)[0]
    img_mark = p.is_img
    if request.method == 'POST':
        if request.POST.has_key('ensure'):
            return HttpResponseRedirect("/logimg/" + str(id))
        else:
            return HttpResponseRedirect("/index/")
    return render_to_response("is_add_logimg.html", locals())
    

@csrf_exempt
@login_required
def logimg(request, id):
    u = request.user
    username = u.username
    p = Profile.objects.get_or_create(user = u)[0]
    img_mark = p.is_img
    log = Log.objects.get(logID = id)
    if request.method == 'POST':       
        if 'image' in request.FILES:
            image=request.FILES["image"]
            img=Image.open(image)
            img.thumbnail((1080,720),Image.ANTIALIAS)
            name='./static/imgs/' + username + str(log.logID) + 'log.png'
            img.save(name,"png")
            nameurl = username + str(log.logID) + 'log'
            log.img_name = nameurl
            log.is_img = True
            log.save()
            return HttpResponseRedirect("/index/")
    return render_to_response('img.html', locals())


@csrf_exempt
@login_required
def friend_logimgs(request, id):
    u = request.user
    username = u.username
    p = Profile.objects.get_or_create(user = u)[0]
    img_mark = p.is_img
    friend_u = User.objects.get(username = id)
    friend_logs = friend_u.log_set.all().filter(is_img = True).order_by('-date')
    logimgs_num = len(friend_logs)
    return render_to_response('friend_logimgs.html', locals())

    
