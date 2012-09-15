# from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.contrib.auth.models import User
from django.template import RequestContext
from vote.models import New, \
                        UserVote
from datetime import datetime
from math import log


epoch = datetime(1970, 1, 1)


def epoch_seconds(date):
    """Returns the number of seconds from the epoch to date."""
    td = date - epoch
    return td.days * 86400 + td.seconds + (float(td.microseconds) / 1000000)


def score(ups, downs):
    return ups - downs


def hot(ups, downs, date):
    """The hot formula. Should match the equivalent function in postgres."""
    s = score(ups, downs)
    order = log(max(abs(s), 1), 10)
    sign = 1 if s > 0 else -1 if s < 0 else 0
    seconds = epoch_seconds(date) - 1134028003
    return round(order + sign * seconds / 45000, 7)


def show(request):
    user = request.user
    news = New.objects.order_by('-hot')
    if request.method == 'POST':
        return render_to_response('vote_content.html',
            {"news": news}, context_instance=RequestContext(request))
    else:
        return render_to_response('vote.html', {"news": news, "user": user})


def checkRobot(newid, ip):
    count = UserVote.objects.filter(new=newid, ipad=ip)
    return len(count)


# @login_required
def up(request, id=''):
    new = New.objects.get(id=id)
    userid = request.session['_auth_user_id']
    username = 'up'
    ipad = request.META['REMOTE_ADDR']
    count = checkRobot(id, ipad)
    if count > 100:
        error = 'you are robot!'
    else:
        error = ''
        try:
            userVote = UserVote.objects.get(user=userid, new=id)
            if userVote.up == 0:
                userVote.up = 1
                new.ups = new.ups + 1
                if userVote.down == 1:
                    userVote.down = 0
                    new.downs = new.downs - 1
                username = request.user
            else:
                userVote.up = 0
                new.ups = new.ups - 1
                username = 'wu'
            userVote.save()
        except:
            new.ups = new.ups + 1
            user = User.objects.get(id=userid)
            userVote = UserVote(user=user, new=new, up=1, ipad=ipad)
            userVote.save()
        time = new.pubtime
        date = datetime.combine(time.date(), time.time())
        new.hot = hot(new.ups, new.downs, date)
        new.save()
    news = New.objects.order_by('-hot')
    return render_to_response('vote_content.html',
        {"news": news, 'user': username, 'id': count, 'error': error},
        context_instance=RequestContext(request))


def down(request, id=''):
    new = New.objects.get(id=id)
    userid = request.session['_auth_user_id']
    username = 'down'
    ipad = request.META['REMOTE_ADDR']
    count = checkRobot(id, ipad)
    if count > 22:
        error = 'you are robot!'
    else:
        error = ''
        try:
            userVote = UserVote.objects.get(user=userid, new=id)
            if userVote.down == 0:
                userVote.down = 1
                new.downs = new.downs + 1
                if userVote.up == 1:
                    userVote.up = 0
                    new.ups = new.ups - 1
                username = request.user
            else:
                userVote.down = 0
                new.downs = new.downs - 1
                username = 'wu'
            userVote.save()
        except:
            new.downs = new.downs + 1
            user = User.objects.get(id=userid)
            userVote = UserVote(user=user, new=new, down=1, ipad=ipad)
            userVote.save()
        time = new.pubtime
        date = datetime.combine(time.date(), time.time())
        new.hot = hot(new.ups, new.downs, date)
        new.save()
    news = New.objects.order_by('-hot')
    return render_to_response('vote_content.html',
        {"news": news, 'user': username, 'id': count, 'error': error},
        context_instance=RequestContext(request))
