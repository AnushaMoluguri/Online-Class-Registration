from django.shortcuts import render,redirect
from app1.models import AddClassModel,StudentModel,EnroleListModel
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError
from  django.db.models import Q

def admin_login(request):
    return render(request,"admin_login.html")


def admin_login_check(request):
    na = request.POST.get("a1")
    pw = request.POST.get("a2")
    if na == "a" and pw == "a":
        return render(request, "admin_page.html")
    else:
        messages.error(request, "Invali Admin")
        return redirect('admin_login')


def shedule_new_cls(request):
    return render(request,"shedule_new_cls.html")


def class_added(request):

    na=request.POST.get("c1")
    fa = request.POST.get("c2")
    da = request.POST.get("c3")
    ti = request.POST.get("c4")
    fe = request.POST.get("c5")
    du = request.POST.get("c6")
    try:
      AddClassModel(Name=na,Faculty=fa,Date=da,Time=ti,Fee=fe,Duration=du).save()
      messages.success(request, "schedule is added successfully")
      return redirect("shedule_new_cls")

    except IntegrityError:
        messages.error(request,"This schedule has added already")
        return redirect("shedule_new_cls")


def view_shedule(request):
    res=AddClassModel.objects.all()
    return render(request,"view_shedul.html",{"data":res})


def showupdate(request):
    no=request.GET.get("t1")
    # Query to read 1 record from DB
    result=AddClassModel.objects.get(Idno=no)
    return render(request, "update.html", {"data": result})


def update_cls(request):
    no=request.POST.get("u1")
    na = request.POST.get("u2")
    fa = request.POST.get("u3")
    da = request.POST.get("u4")
    ti = request.POST.get("u5")
    fe = request.POST.get("u6")
    du = request.POST.get("u7")
    AddClassModel.objects.filter(Idno=no).update(Name=na, Faculty=fa, Date=da, Time=ti, Fee=fe,Duration=du),
    return redirect('view_shedule')


def delete(request):
    no=request.GET.get("no")
    # delete 1 recod from DB
    AddClassModel.objects.filter(Idno=no).delete()
    return redirect('view_shedule')

def Showmain(request):
    results = AddClassModel.objects.all()
    return render(request, "main.html", {"da": results})


def stu_reg(request):
    return render(request,"stu_reg.html")


def stu_registerd(request):
      na = request.POST.get("t1")
      cn = request.POST.get("t2")
      ei = request.POST.get("t3")
      pw = request.POST.get("t4")
      try:
         StudentModel(name=na, Contactno=cn, emailid=ei, password=pw).save()
         messages.success(request, "registration is succesfull")
      except IntegrityError:
          messages.error(request,"Mail-ID must be Unique")
          return redirect('stu_reg')
      #except ValueError:
          #messages.error(request,"hai")
          #return  redirect('stu_reg')


def stu_login(request):
    return render(request,"stu_login.html")


def stu_login_check(request):
    un = request.POST.get("l1")
    pw = request.POST.get("l2")
    cor=AddClassModel.objects.all()
    try:
        result=StudentModel.objects.get(Q(name=un, password=pw))
        request.session['contact']=result.Contactno
        return render(request, "student_page.html",{'data':result,"courses":cor})

    except ObjectDoesNotExist:
        messages.error(request, "Invalid User")
        return redirect('stu_login')


def enrol_course(request):
    res=AddClassModel.objects.all()
    return render(request,"enrol_course.html",{"data":res})


def enroled_course(request):
    cid=request.POST.get("cid")
    cno=request.POST.get("cno")
    try:
        EnroleListModel.objects.get(Contanctno_id=cno,idno_id=cid)
        messages.error(request,"Course has enrolled already")
        return redirect('enrol_course')
    except ObjectDoesNotExist:
        EnroleListModel.objects.create(Contanctno_id=cno,idno_id=cid)
        messages.error(request, " Course was enrolled  succesfully")
        return redirect('enrol_course')


def view_enrol_courses(request):
    contatno=request.GET.get("contact")
    res=EnroleListModel.objects.filter(Contanctno_id=contatno)
    data=[AddClassModel.objects.get(Idno=x.idno_id) for x in res]
    return render(request,"view_enrol_courses.html",{"data":data})


def cancel_enrol_course(request):
    contactno=request.GET.get("contact")
    res=EnroleListModel.objects.filter(Contanctno_id=contactno)
    data=[AddClassModel.objects.get(Idno=x.idno_id)for x in res]
    return render(request,"cancel_enrol_courses.html",{"data":data})


def course_canceled(request):
    courseId=request.POST.get('cid')
    studentcontactno=request.POST.get('scn')
    EnroleListModel.objects.get(Contanctno_id=studentcontactno,idno_id=courseId).delete()
    return redirect('cancel_enrol_course')