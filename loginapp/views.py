from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from loginapp.models import UserTable,ConversationTable
# Create your views here.
def login(request):
    # try:
    #     request.session['username']
    #     return HttpResponseRedirect('http://localhost:8000/loginapp/login/')
    # except:
    user = UserTable.objects.filter(username='admin')
    if not user:
        CreateAdmin()
    res = render(request,'loginPage.html')
    return res

def CreateAdmin():
    user = UserTable()
    user.username = 'admin'
    user.password = 'password'
    user.realname = 'SuperUser'
    user.save()


def loginValidation(request):
    try:
        user = UserTable.objects.get(username=request.POST['username'],password=request.POST['password'])
        user.username
        request.session['username'] = user.username
        request.session['realname'] = user.realname
        url = 'http://localhost:8000/loginapp/home/'
    except:
        url = f'http://localhost:8000/loginapp/login/'
    return HttpResponseRedirect(url)

def signup(request):
    d = {}
    try:
        if request.GET['error'] == '1':
            d['errmsg'] = 'username already taken'
    except:
        d['errmsg'] = ' '
    res = render(request,'signupPage.html',d)
    return res

def saveUser(request):
    user = UserTable()
    u = UserTable.objects.filter(username = request.POST['username'])
    if not u:
        user.username = request.POST['username']
        user.password = request.POST['password']
        user.realname = request.POST['realname']
        user.save()
        url = 'http://localhost:8000/loginapp/login/'
    else:
        url = 'http://localhost:8000/loginapp/signup/?error=1'
    return HttpResponseRedirect(url)

def home(request):
    userData = UserTable.objects.all()
    try:
        request.session['username'] 
    except Exception as e:
        return HttpResponseRedirect(f'http://localhost:8000/loginapp/login/?error={e}')
    
    messages = ConversationTable.objects.all()
    dict = {
        "userData":userData,
        "messages":messages,
    }
    res = render(request,'homePage.html',dict)
    return res

def send(request):
    conversationdb = ConversationTable()
    conversationdb.username = request.session['username']
    conversationdb.message = request.POST['message']
    conversationdb.save()
    return HttpResponseRedirect('http://localhost:8000/loginapp/home/')

def delete(request):
    if request.GET['username'] !='admin':
        user = UserTable.objects.filter(username = request.GET['username'])
        user.delete()
    return HttpResponseRedirect('http://localhost:8000/loginapp/home/')

def logout(request):
    request.session.clear()
    return HttpResponseRedirect('http://localhost:8000/loginapp/login/')

def deleteConversation(request):
    cdb = ConversationTable.objects.all()
    for data in cdb:
        data.delete()
    return HttpResponseRedirect('http://localhost:8000/loginapp/home')

