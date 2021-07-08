from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages
from django.urls import reverse
from attendanceapp.models import CustomUser, Staff, Course, Student, SessionModel
from datetime import datetime
from attendanceapp.forms import AddStudentForm, EditStudentForm
from django import forms


def admin_home(request):
    return render(request, "hod_template/home_content.html")

def add_staff(request):
    return render(request, "hod_template/add_staff.html")

def add_staff_save(request):
    if request.method!="POST":
        return HttpResponse("Method not allowed")
    else:
        first_name=request.POST.get("first_name")
        last_name=request.POST.get("last_name")
        username=request.POST.get("username")
        email=request.POST.get("email")
        password=request.POST.get("password")
        address=request.POST.get("address")
        try:
         user=CustomUser.objects.create_user(username=username,password=password,first_name=first_name,last_name=last_name, email=email,user_type=2)
         user.staff.address=address
         user.save()
         messages.success(request, "Staff Member Successfully Added")
         return HttpResponseRedirect(reverse("add_staff"))
        except:
            messages.error(request, "Failed To Add Staff Member")
            return HttpResponseRedirect(reverse("add_staff"))

def add_course(request):
    staff=CustomUser.objects.filter(user_type=2)
    return render(request, "hod_template/add_course.html", {"staff":staff})

def add_course_save(request):
    if request.method!="POST":
        return HttpResponseRedirect("Method Not Allowed")
    else:
        course=request.POST.get("course")
        staff_id=request.POST.get("staff")
        staff=CustomUser.objects.get(id=staff_id)
        try:
            course_model=Course(course_name=course, staff_id=staff)
            course_model.save()
            messages.success(request, "Course Successfully Added")
            return HttpResponseRedirect(reverse("add_course"))
        except:
            messages.error(request, "Failed To Add Course")
            return HttpResponseRedirect(reverse("add_course"))

  
def add_student(request):
    form=AddStudentForm()
    return render(request, "hod_template/add_student.html", {"form":form})

def add_student_save(request):
    if request.method!="POST":
        return HttpResponse("Method not allowed")
    else:
        form=AddStudentForm(request.POST,request.FILES)
        if form.is_valid():
         first_name=form.cleaned_data["first_name"]
         last_name=form.cleaned_data["last_name"]
         username=form.cleaned_data["username"]
         email=form.cleaned_data["email"]
         password=form.cleaned_data["password"]
         address=form.cleaned_data["address"]
         gender=form.cleaned_data["gender"]
         session_id=form.cleaned_data["session_id"]

        
        # try:
         user=CustomUser.objects.create_user(username=username,password=password,first_name=first_name,last_name=last_name, email=email,user_type=3)
         user.student.address=address
         user.student.gender=gender
         session_id=SessionModel.objects.get(id=id)
         user.student.session_id=session_id
         user.student.profile_pic=""
         user.save()
         messages.success(request, "Student Successfully Added")
         return HttpResponseRedirect(reverse("add_student"))
         #except:
          #   messages.error(request, "Failed To Add Student")
           #  return HttpResponseRedirect(reverse("add_student"))
        else:
            form=AddStudentForm(request.POST)
            return render(request, "hod_template/add_student.html", {"form":form})




def manage_staff(request):
    staff=Staff.objects.all()
    return render(request, "hod_template/manage_staff.html", {"staff":staff})

def manage_student(request):
    student=Student.objects.all()
    return render(request, "hod_template/manage_student.html", {"student":student})

def manage_course(request):
    course=Course.objects.all()
    return render(request, "hod_template/manage_course.html", {"course":course})

def edit_staff(request,staff_id):
    staff=Staff.objects.get(admin=staff_id)
    return render(request, "hod_template/edit_staff.html", {"staff":staff, "id":staff_id})

def edit_staff_save(request):
     if request.method!="POST":
            return HttpResponse("Method not allowed")
     else:
         staff_id=request.POST.get("staff_id")
         first_name=request.POST.get("first_name")
         last_name=request.POST.get("last_name")
         email=request.POST.get("email")
         username=request.POST.get("username")
         address=request.POST.get("address")

         try:
             user=CustomUser.get.objects(id=staff_id)
             user.first_name=first_name
             user.last_name=last_name
             user.email=email
             user.username=username
             user.save()

             staff_model=Staff.objects.get(admin=staff_id)
             staff_model.address=address
             staff_model.save()

             messages.success(request, "Changes Saved Succesfully")
             return HttpResponseRedirect(reverse("edit_staff", kwargs={"staff_id":staff_id}))

         except:
             messages.error(request, "Failed To Save Changes")
             return HttpResponseRedirect(reverse("edit_staff", kwargs={"staff_id":staff_id}))

def edit_student(request,student_id):
    request.session['student_id']=student_id
    student=Student.objects.get(admin=student_id)
    form=EditStudentForm()
    form.fields['email'].initial=student.admin.email
    form.fields['first_name'].initial=student.admin.first_name
    form.fields['last_name'].initial=student.admin.last_name
    form.fields['username'].initial=student.admin.username
    form.fields['gender'].initial=student.gender
    form.fields['address'].initial=student.address
    form.fields['session_id'].initial=student.session_id
    return render(request, "hod_template/edit_student.html",{"form":form, "id":student_id})

def edit_student_save(request):
     if request.method!="POST":
            return HttpResponse("Method not allowed")
     else:
         student_id=request.session.get("student_id")
         if student_id == None:
             return HttpResponseRedirect("/manage_student")
        
         form=EditStudentForm(request.POST,request.FILES)
         if form.is_valid(): 
          first_name=form.cleaned_data["first_name"]
          last_name=form.cleaned_data["last_name"]
          email=form.cleaned_data["email"]
          username=form.cleaned_data["username"]
          address=form.cleaned_data["address"]
          gender=form.cleaned_data["gender"]
          session_id=form.cleaned_data["session_id"]
          

          try:
              user=CustomUser.get.objects(id=student_id)
              user.first_name=first_name
              user.last_name=last_name
              user.email=email
              user.username=username
              user.save()

              student_model=Student.objects.get(admin=student_id)
              student_model.address=address
              student_model.gender=gender
              session_id=SessionModel.objects.get(id=id)
              student.session_id=session_id
              student_model.save()
              del request.session['student_id']

              messages.success(request, "Changes Saved Succesfully")
              return HttpResponseRedirect(reverse("edit_student", kwargs={"student_id":student_id}))

          except:
              messages.error(request, "Failed To Save Changes")
              return HttpResponseRedirect(reverse("edit_student", kwargs={"student_id":student_id}))
         else:
            form=EditStudentForm(request.POST)
            student=Student.objects.get(admin=student_id)
            return render(request, "hod_template/edit_student.html", {"form":form})


def manage_session(request):
    return render(request, "hod_template/manage_session.html")
     
        
def manage_session_save(request):
    if request.method!="POST":
            return HttpResponse("Method not allowed") 
    else:
        session_start=request.POST.get("session_start")
        session_end=request.POST.get("session_end")

        try:
            sessionyear=SessionModel(session_start=session_start,session_end=session_end)
            sessionyear.save()
            messages.success(request, "Session Created Successfully")
            return HttpResponseRedirect(reverse("manage_session"))

        except:
            messages.error(request, "Failed To Create Session")
            return HttpResponseRedirect(reverse("manage_session"))










        

