from django.shortcuts import render,HttpResponse,redirect
from .models import product
from .forms import addpostform
from django.views import generic

# def Product(request): 
#     if request.method == "POST":
#         form = addpostform(request.POST)
#         if form.is_valid():
#             P_name=form.cleaned_data['P_name']
#             discrption=form.cleaned_data['discrption']
#             price=form.cleaned_data['price'] 
#             Product = product.objects.create(P_name=P_name,discrption=discrption,price=price)
#             Product.save()
#             return HttpResponse('Created')
#     else:
#         Form = addpostform()
#         Product=product.objects.all()  
#     context ={
#         'Product':Product,
#         'Form':Form
#     }
#     return render(request,'home.html',context)
class Product(generic.ListView):
    template_name = "Product/home.html"
    context_object_name = 'Product'
    def get_queryset(self):    
        return product.objects.all()

def AddPost(request):
    if request.method == "POST":
        form = addpostform(request.POST,request.FILES)
        if form.is_valid():
            P_name=form.cleaned_data['P_name']
            discrption=form.cleaned_data['discrption']
            price=form.cleaned_data['price']
            image = form.cleaned_data['image']
            author = request.user 
            Product = product.objects.create(P_name=P_name,discrption=discrption,price=price,author=author,image=image)
            Product.save()
            return HttpResponse('Created')
    else:
        Form = addpostform()
        Product=product.objects.all()  
    context ={
        'Form':Form
    }
    return render(request,'Product/additem.html',context)


class productdetail(generic.DeleteView):
    model = product
    template_name = 'Product/detail.html'



def Post_Like(request,id):
    post = product.objects.get(id=id)
    user = request.user
    if user.is_authenticated:
        if user in post.like.all():
            return HttpResponse("you cant like this Post Again")
        post.like.add(user)
        return redirect('detail',id)
    else:
        return HttpResponse('you Are Not Like This Post please Login!')

def Post_UnLike(request,id):
    post = product.objects.get(id=id)
    user = request.user
    if user.is_authenticated:
        if user in post.like.all():
            post.like.remove(user)
            return redirect('detail',id)
        else:
            return HttpResponse("You have not liked this post before")
    else:
        return HttpResponse('you Are Not Like This Post please Login')
   