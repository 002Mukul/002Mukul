"""medassist URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from . import Specialization
from . import Userreg
from . import Doctor
from . import Question
from . import Adminlogin
from . import QuesSub
from . import Product

urlpatterns = [
    path('admin/', admin.site.urls),
    #Specialization details
    path('specialization/',Specialization.SpecializationInterface),
    path('specializationsubmit',Specialization.specializationsubmit),
    path('specializationdisplay',Specialization.displayallspecialization),  
    path('specializationdisplayJSON/',Specialization.displayallspecializationJSON),  
    path('updatespecialization/',Specialization.UpdateSpecialization),
    path('deletespecialization/',Specialization.DeleteSpecialization),
    path('editspecialization',Specialization.EditSpecialization),
    #Doctor details
    path('doctorinterface/',Doctor.DoctorInterface),
    path('doctorsubmit',Doctor.DoctorSubmit),
    path('displayalldoctor/',Doctor.DisplayAllDoctor),
    path('Updatedoctor/',Doctor.Updatedoctor),
    path('Deletedoctor/',Doctor.Deletedoctor),
    path('editdoctoricon',Doctor.EditDoctorIcon),    
    #question    
    path('question/',Question.DoctorQuestionary),
    path('questionsubmit/',Question.QuestionSubmit),
    path('subquestiondisplayJSON/',Question.SubQuestionDisplay),
    #subquestion
    path('subquestion/',Question.SubQuestionary),
    path('subquestionsubmit/',Question.SubQuestioanrySubmit),
    #AdminLogin
    path('adminlogin/',Adminlogin.AdminLogin),   
    path('adminlogout/',Adminlogin.AdminLogout),    
    path('dashboard',Adminlogin.CheckAdminLogin),
    #Userdatails
    path('userregistration/',Userreg.UserRegistration),
    path('usersubmit',Userreg.SubmitUser),
    path('loginpage/',Userreg.UserLogin),
    path('otpverification',Userreg.OTPverified),
    path('frontpage/',Userreg.FrontPage),
    path('signemail/',Userreg.Signemail),
    path('forgetpass/',Userreg.ForgetPass),
    path('checkotp',Userreg.ChkOtp),  
    #QuestionFilling
    path('surveyform',QuesSub.SurveyForm),
    path('questionsub/',QuesSub.Question),
    path('questionlist',QuesSub.QuestionList),
    #Product Management
    path('productinterface/',Product.ProductInterface),
    path('productsubmit',Product.ProductSubmit),
    #staff
    path('stafflogin/',Product.StaffLogin),
    path('staffloginchk',Product.CheckStaffLogin),
    #User
    path('firstpage/',Product.LoginOption),
    path('userdetails/',Product.UserInterface),
    path('submituser',Product.UserSubmit),
    path('chkuser',Product.CheckUser),
    path('loginm/',Product.Loginm),
    path('Addcart/',Product.Addcart),
    path('itemlist/',Product.ShowItem),
]
