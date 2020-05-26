from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, Http404 ,HttpResponseRedirect
from .models import Student,Admin
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from .forms import Loginform,Loginform2


class HomeView(generic.ListView):
    model = Student
    template_name = 'uni/home.html'


class PageView(generic.ListView):

    model = Student
    template_name = 'uni/page.html'
    
    def ren(self,request):
        return render(request ,self.template_name,{'12':12})
    
class LoginView(generic.ListView):
    model = Student
    template_name = 'uni/login.html'
    def get(self , request):
        form = Loginform()
        form2 = Loginform2()
        return render(request ,'uni/login.html',{'form' : form , 'form2' : form2})
        
    def post(self,request):

        form = Loginform(request.POST)
        form2 = Loginform2(request.POST)

        if (form.is_valid() and form2.is_valid()):

            users = Student.objects.all()
            for user in users:
                if user.student_username == form.cleaned_data['username'] and user.student_password == form2.cleaned_data['password']:
                    return HttpResponseRedirect(reverse('uni:page',args = (user.id,)))
                    
                    

            
            
            

    



