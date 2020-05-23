from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from accounts.decorators import unauthenticated_user,allowed_users,admin_only
from django.contrib.auth.models import User, auth
from .models import details,questions
from django.contrib import messages
from datetime import datetime
# import datetime


# Create your views here.


@login_required(login_url='../accounts/login')
@admin_only
def exam(request):
    if request.method == 'POST':
        usname = request.user.first_name
        subject = request.POST['sname']
        pwd = request.POST['pwdname']
        date = request.POST['Date']
        noq = request.POST['noq']
        time1 = request.POST['ti1']
        time2 = request.POST['ti2']
        year,month,day = date.split('-')
        dateTimeObj = datetime.now()
        timestampStr = dateTimeObj.strftime("%d-%m-%Y (%H:%M:%S.%f)")
        d,t = timestampStr.split(' ')
        d,m,y = d.split('-')
        if(int(year)>=int(y)) and (int(month)>=int(m)) and (int(day)>=int(d)):
            if time1 < time2 :
                obj = details(uname=usname,subject=subject,pwd=pwd,date=date,noques=noq,starttime=time1,stoptime=time2)
                obj.save()
                return redirect('add_question')
            else:
                messages.info(request,'Starting Time Should Not be Greater than Stopping Time.')
                return redirect('exam')
        else:
            messages.info(request,'Entered date is no longer valid')
            return redirect('exam')
        
    else:
        return render(request,"host01.html",{'name':request.user.first_name})


@login_required(login_url='../accounts/login')
@admin_only
def add_question(request):
    usname = request.user.first_name
    obj = details.objects.all()
    for i in obj:
        if usname == i.uname:
            sub = i.subject
            pwd = i.pwd
            n = i.noques
            dat = i.date
    obj2 = questions.objects.all()
    k=0
    for j in obj2:
        
        if j.uname == usname and j.subject == sub and j.pwd == pwd :
            print('working')
            k=k+1
    
    if request.method == 'POST':
        k = k+1
        qus=request.POST['quest']
        opt1 = request.POST['opt1']
        opt2 = request.POST['opt2']
        opt3 = request.POST['opt3']
        opt4 = request.POST['opt4']

        opb1=bool(request.POST.get('chek1', False))
        opb2=bool(request.POST.get('chek2', False))
        opb3=bool(request.POST.get('chek3', False))
        opb4=bool(request.POST.get('chek4', False))
        
        if k<=n:
            obj3 = questions(uname=usname,quest=qus,subject=sub,pwd=pwd,option1=opt1,option2=opt2,option3=opt3,option4=opt4,opb1=opb1,opb2=opb2,opb3=opb3,opb4=opb4)
            obj3.save()
            if k<n:
                return render(request,"host.html",{'subject':sub,'date':dat,'num':k+1})
            else:
                return redirect('/')
        else:
            return redirect('/')

    else:
        
        return render(request,"host.html",{'subject':sub,'date':dat,'num':k+1})
    # else:
    #     return redirect('/')