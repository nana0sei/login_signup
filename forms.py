from django import forms
from attendanceapp.models import SessionModel

class DateInput(forms.DateInput):
    input_type="date"



class AddStudentForm(forms.Form):
    email=forms.EmailField(label="Email",max_length=50, widget=forms.EmailInput(attrs={"class":"form-control"}))
    password=forms.CharField(label="Password",max_length=50, widget=forms.PasswordInput(attrs={"class":"form-control"}))
    first_name=forms.CharField(label="First Name",max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}))
    last_name=forms.CharField(label="Last Name",max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))
    username=forms.CharField(label="Username",max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))
    
    session_list = []
    sessions = SessionModel.objects.all()

    for ses in sessions:
        small_ses = (ses.id, str(ses.session_start)+" | "+str(ses.session_end))
        session_list.append(small_ses)
    
        #session_list=[]

    gender_choice=(
        ("Male","Male"),
        ("Female","Female")
    )  
    gender=forms.ChoiceField(label="Gender", choices=gender_choice, widget=forms.Select(attrs={"class":"form-control"})) 
    address=forms.CharField(label="Address",max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}))  
    session_id=forms.ChoiceField(label="Session", widget=forms.Select(attrs={"class":"form-control"}),choices=session_list)
   

class EditStudentForm(forms.Form):
    email=forms.EmailField(label="Email",max_length=50, widget=forms.EmailInput(attrs={"class":"form-control"}))
    first_name=forms.CharField(label="First Name",max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}))
    last_name=forms.CharField(label="Last Name",max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))
    username=forms.CharField(label="Username",max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))
    session_list = []
    try:
        sessions = SessionModel.objects.all()

        for ses in sessions:
           small_ses = (ses.id, str(ses.session_start)+"-"+str(ses.session_end))
           session_list.append(small_ses)
    except:
        session_list=[]
        
    gender_choice=(
        ("Male","Male"),
        ("Female","Female")
    )  
    gender=forms.ChoiceField(label="Gender", choices=gender_choice, widget=forms.Select(attrs={"class":"form-control"})) 
    address=forms.CharField(label="Address",max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}))  
    session_id=forms.ChoiceField(label="Session", widget=forms.Select(attrs={"class":"form-control"}),choices=session_list)


 