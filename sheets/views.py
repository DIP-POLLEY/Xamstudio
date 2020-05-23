from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from accounts.decorators import unauthenticated_user,allowed_users,admin_only
from django.contrib.auth.models import User, auth
from conduct.models import details,questions
from .models import tests,anspap,qsheet,result
from django.contrib import messages
from datetime import datetime
import pytz
# Create your views here.

@login_required(login_url='../accounts/login')
def room(request):
    if request.method == 'POST':
        usname = request.user.first_name
        code = request.POST['srch']
        obj = details.objects.all()
        flag = 0
        testpap = tests.objects.all()
        for i in testpap:
            if ((code == i.code) and (usname == i.name)):
                flag=1
        if flag == 1:
            messages.info(request,'Exam Already Given')
            return redirect('room')
        else:
            flag = 0
            suchk = details.objects.all()
            for i in suchk:
                if i.subject == code:
                    flag = 1
                    break
            if flag != 1:
                messages.info(request,'Entered Code is incorrect')
                return redirect('room')
            else:
                return render(request,'rule.html',{'subject':i.subject,'date':i.date,'nq':i.noques,'tim1':i.starttime,'tim2':i.stoptime})
    else:
        return render(request,'roomsel.html')


@login_required(login_url='../accounts/login')
def rule(request):
    if request.method == 'POST':
        flag = 0
        usname = request.user.first_name
        code = request.POST['pwrd']
        suchk = details.objects.all()
        for i in suchk:
            if i.pwd == code:
                flag = 1
                
        if flag == 1:
            date = i.date.strftime("%d-%m-%Y")
            day,month,year = date.split('-')
            ist = pytz.timezone('Asia/Calcutta')
            dateTimeObj = datetime.now(ist)
            timestampStr = dateTimeObj.strftime("%d-%m-%Y %H:%M:%S")
            d,t = timestampStr.split(' ')
            d,m,y = d.split('-')
            if( d == day and m == month and y == year):
                tim1 = i.starttime.strftime("%H:%M:%S")
                tim2 = i.stoptime.strftime("%H:%M:%S")
                h1,mi1,s1 = tim1.split(':')
                h2,mi2,s2 = tim2.split(':')
                h3,mi3,s3 = t.split(':')
                print(h1,mi1,s1)
                print(h2,mi2,s2)
                print(h3,mi3,s3)
                x1 = int(h1)*60+(int(mi1))
                x2 = int(h2)*60+(int(mi2))
                x3 = int(h3)*60+(int(mi3))
                if x3>=x1 and x3<=x2 :
                    obj = tests(code=i.subject,name=usname)
                    obj.save()
                    return redirect('xampage')
                else:
                    messages.info(request,'Exam Not now.')
                    return redirect('room')
            else:
                messages.info(request,'Exam Not today.')
                return redirect('room')
            
        else:
            messages.info(request,'Password was wrong.')
            return redirect('room')
        
        return redirect('xampage')
    else:
        return render(request,"rule.html")


@login_required(login_url='../accounts/login')
def xampage(request):
    if request.method == 'POST':
        opb1=bool(request.POST.get('opg1', False))
        opb2=bool(request.POST.get('opg2', False))
        opb3=bool(request.POST.get('opg3', False))
        opb4=bool(request.POST.get('opg4', False))
        uname = request.user.first_name
        tst = tests.objects.all()
        uname = request.user.first_name
        for i in tst:
            if uname == i.name:
                nam = i.code
        qsht = qsheet.objects.all()
        for g in qsht:
            break
        obc = anspap(uname=uname,nosub=nam,question=g.question,opb1=opb1,opb2=opb2,opb3=opb3,opb4=opb4)
        obc.save()
        suchk = details.objects.all()
        for j in suchk:
            if j.subject == nam:
                break
        qsht = qsheet.objects.all()
        for i in qsht:
            i.delete()
            break
        qsht = qsheet.objects.all()
        for m in qsht:
            break
        chk = qsheet.objects.all()
        if not chk:
            skr = 0
            anp = anspap.objects.all()
            for k in anp:
                if(k.uname == uname and k.nosub == nam):
                    qn = k.question
                    suchk = questions.objects.all()
                    for f in suchk:
                        if (f.quest == qn and nam == f.subject):
                            if((f.opb1 == k.opb1) and (f.opb2 == k.opb2) and (f.opb3 == k.opb3) and (f.opb4 == k.opb4)):
                                print(f.opb1,f.opb2)
                                print(k.opb1,k.opb2)
                                skr=skr+1
            ojt = result(uname=uname,nosub=nam,score=skr)
            ojt.save()                  
            return redirect('/')
        else:
            date = j.date.strftime("%B %d, %Y")
            ti = j.stoptime.strftime("%H:%M:%S")
            tim2 = date+' '+ti
            return render(request,"xampage.html",{'date':j.date,'time':tim2,'subject':nam,'qsht':m})
    else:
        tst = tests.objects.all()
        uname = request.user.first_name
        for i in tst:
            if uname == i.name:
                nam = i.code
        suchk = details.objects.all()
        for j in suchk:
            if j.subject == nam:
                break
        qpapr = questions.objects.all()
        for m in qpapr:
            if nam == m.subject:
                objct = qsheet(nosub=m.subject,uname=uname,question=m.quest,option1=m.option1,option2=m.option2,option3=m.option3,option4=m.option4,opb1=m.opb1,opb2=m.opb2,opb3=m.opb3,opb4=m.opb4)
                objct.save()
        qsht = qsheet.objects.all()
        for i in qsht:
            break
    date = j.date.strftime("%B %d, %Y")
    ti = j.stoptime.strftime("%H:%M:%S")
    tim2 = date+' '+ti
    return render(request,'xampage.html',{'date':j.date,'time':tim2,'subject':nam,'qsht':i})


@login_required(login_url='../accounts/login')
def result1(request):
    if request.method == 'POST':
        code = request.POST['cors']
        r = result.objects.all()
        t = details.objects.all()
        flag = 0
        for i in t:
            if code == i.subject:
                flag = 1
                n = i.noques
        if flag == 0:
            messages.info(request,'Subject Code not found')
            return redirect('result1')
        return render(request,'result.html',{'result':r,'nam':code,'no':n})
    else:
        code = "chh"
        r = result.objects.all()
        return render(request,'result.html',{'result':r,'nam':code})



def malpractice(request):
    return render(request,'error.html')