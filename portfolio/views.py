from django.shortcuts import render,get_object_or_404,redirect
from django.core.paginator import Paginator
from django.core.files.storage import FileSystemStorage


from .models import Portfolio
#from .forms import PortfolioPost
# Create your views here.
def portfolio(request):
    portfolios = Portfolio.objects
    portfolio_list=Portfolio.objects.all()
    #블로그 객체 세 개를 한 페이지로 자르기
    paginator = Paginator(portfolio_list,12)
    #request된 페이지가 뭔지를 알아내고 ( request페이지를 변수에 담아냄 )
    page = request.GET.get('page')
    #request된 페이지를 얻어온 뒤 return 해 준다
    posts = paginator.get_page(page)

    return render(request,'portfolio/portfolio.html',{'portfolios': portfolios,'posts':posts})


#def new(request):
#    if request.method =='POST':
#        form = PortfolioPost(request.POST,request.FILES)
#        if form.is_valid():
#            post = form.save(commit=False)
#            post.save()
#            return redirect('portfolio')
#    else:
#        form = PortfolioPost()
#        return render(request,'portfolio/new.html',{'form':form})