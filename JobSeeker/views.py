from django.views.generic import ListView,View,DetailView
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render,redirect
from .models import formations,seeker,files,programme,month
from .formulaires import formationForm,catform,docform,seekerform,progform,monthform
from .utils import render_to_pdf
from django.contrib import messages

def add_form(request):
    form = formationForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request,"bien reçu,si vous voulez  ajouter un autre objet")
        return redirect('http://127.0.0.1:8000/addfor/')
    return render(request,"fromation.html",{'form':form})
def add_form_ar(request):
    form = formationForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "تمت العملية بسلام!")
        return redirect('http://127.0.0.1:8000/addforar/')
    return render(request,"formationar.html",{'form':form})




def updateform(request,pk):
    form=formationForm(request.POST or None)
    contexte={'form':form}
    return render(request,"fromation.html",contexte)




def add_cat(request):
    form=catform(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "bien reçu,si vous voulez  ajouter un autre objet")
        return redirect('http://127.0.0.1:8000/addcat/')
    return render(request,"categorie.html",{"form":form})
def add_cat_ar(request):
    form=catform(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "تمت العملية بسلام!")
        return redirect('http://127.0.0.1:8000/addcatar/')
    return render(request,"categoriear.html",{"form":form})





def uploadfile(request):
    context={}
    if request.method== 'POST':
        uploaded_file= request.FILES["document"]
        fs=FileSystemStorage()
        name=fs.save(uploaded_file.name,uploaded_file)
        context['url']=fs.url(name)
    return render(request,"uploadfile.html",context)



def adddoc(request):
    if request.method=="POST":
        form=docform(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "bien reçu,si vous voulez  ajouter un autre objet")
            return redirect('http://127.0.0.1:8000/adddoc/')
    else:
        form=docform()
    return render(request,'document.html',{"form":form})
def adddocar(request):
    if request.method=="POST":
        form=docform(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "تمت العملية بسلام!")
            return redirect('http://127.0.0.1:8000/adddocar/')
    else:
        form=docform()
    return render(request,'documentar.html',{"form":form})








def addprog(request):
    if request.method=="POST":
        form=progform(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "bien reçu,si vous voulez  ajouter un autre objet")
            return redirect('http://127.0.0.1:8000/addprog/')
    else:
        form=docform()
    return render(request,'programme.html',{"form":form})
def addprogar(request):
    if request.method=="POST":
        form=progform(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "تمت العملية بسلام!")
            return redirect('http://127.0.0.1:8000/addprogar/')
    else:
        form=docform()
    return render(request,'programmear.html',{"form":form})






def listedoc(request):
    form=files.objects.all()
    return render(request,'listedoc.html',{"form":form})
def listedocar(request):
    form=files.objects.all()
    return render(request,'listedocar.html',{"form":form})

def listeprog(request):
    form=programme.objects.all()
    return render(request,"listeprog.html",{"form":form})
def listeprogar(request):
    form=programme.objects.all()
    return render(request,"listeprogar.html",{"form":form})


def showadmin(request):
    form = formations.objects.all()
    m=monthform(request.POST or None)
    if m.is_valid():
        month.objects.all().delete()
        m.save()
        messages.success(request, "تمت العملية بسلام!")
        return redirect('http://127.0.0.1:8000/showfor/')
    return render(request,"datatable.html",{'form':form,'month':m})
def showadminar(request):
    form = formations.objects.all()
    m = monthform(request.POST or None)
    if m.is_valid():
        month.objects.all().delete()
        m.save()
        messages.success(request, "تمت العملية بسلام!")
        return redirect('http://127.0.0.1:8000/showforar/')
    return render(request, "showadminar.html", {'form': form, 'month': m})







def homeadmin(request):
    return render(request,"adm.html")
def homeadminar(request):
    return render(request,"admar.html")






def inscrip(request):
    form=seekerform(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "vous êtes bien inscrit(e)")
        return redirect('http://127.0.0.1:8000/inscription/')
    return render(request,"inscription.html",{"form":form})
def inscrip_ar(request):
    form=seekerform(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "تمت العملية بسلام!")
        return redirect('http://127.0.0.1:8000/inscripar')
    return render(request,"inscriptionarabe.html",{"form":form})



def homeseeker(request):
    return render(request,"homeseeker.html")
def homeseekerarabe(request):
    return render(request,"homeseekerarabe.html")




def showseeker(request):
    form = formations.objects.all()
    m=month.objects.all()
    data={'form':form,
          'm':m}
    return render(request,"showseeker.html",data)
def showseekerarabe(request):
    form = formations.objects.all()
    m=month.objects.all()
    data={'form':form,
          'm':m}
    return render(request,"showseekerarabe.html",data)













def showinscription(request):
    form=seeker.objects.all()
    return render(request,"showinscrip.html",{"form":form})
def showinscriptionar(request):
    form=seeker.objects.all()
    return render(request,"showinscripar.html",{"form":form})





def msg(request):
    return render(request,"msg.html")
def msgar(request):
    return render(request,"msgar.html")



def msgseeker(request):
    return render(request,"msgseeker.html")
def msgseekerar(request):
    return render(request,"msgseekerar.html")


def deletefor(request,id):
    f=formations.objects.get(id=id)
    f.delete()

    return redirect("http://127.0.0.1:8000/showfor/")
def deleteforar(request,id):
    f=formations.objects.get(id=id)
    f.delete()
    return redirect("http://127.0.0.1:8000/showforar/")



def deleteiar(request,id):
    f=files.objects.get(id=id)
    f.delete()
    return redirect("http://127.0.0.1:8000/listedocar/")
def deletei(request,id):
    f=files.objects.get(id=id)
    f.delete()
    return redirect("http://127.0.0.1:8000/listedoc/")


def deleteprog(request,id):
    f=programme.objects.get(id=id)
    f.delete()
    return redirect("http://127.0.0.1:8000/listeprog/")
def deleteprogar(request,id):
    f=programme.objects.get(id=id)
    f.delete()
    return redirect("http://127.0.0.1:8000/listeprogar/")


def deletein(request,id):
    f=seeker.objects.get(id=id)
    f.delete()
    return redirect("http://127.0.0.1:8000/showinscrip/")
def deleteinar(request,id):
    f=seeker.objects.get(id=id)
    f.delete()
    return redirect("http://127.0.0.1:8000/showinscripar")

class listeformationview(ListView):
    model= formations
    template_name = "displaypdf.html"
    context_object_name = "formatpdf"

class listeformpdf(View):
    def get(self,request,*args,**kwargs):
        formatpdf= formations.objects.all()
        data={
            'formatpdf':formatpdf,
        }
        pdf=render_to_pdf("liste'.html",data)
        return HttpResponse(pdf,content_type='application/pdf')

class listeinsriview(ListView):
    model= seeker
    template_name = "listeinscripdf.html"
    context_object_name = "instpdf"

class listeinscripdf(View):
    def get(self,request,*args,**kwargs):
        inspdf= seeker.objects.all()
        data={
            'inspdf':inspdf
        }
        pdf=render_to_pdf("inspdf.html",data)
        return HttpResponse(pdf,content_type='application/pdf')


def updatefor(request,id):
    up=formations.objects.get(id=id)
    form=formationForm(instance=up)
    if request.method=='POST':
        form=formationForm(request.POST,instance=up)
        if form.is_valid():
            form.save()
            return redirect("http://127.0.0.1:8000/showfor/")
    return render(request,'edit.html',{'form':form})

def updatefor(request,id):
    up=formations.objects.get(id=id)
    form=formationForm(instance=up)
    if request.method=='POST':
        form=formationForm(request.POST,instance=up)
        if form.is_valid():
            form.save()
            return redirect("http://127.0.0.1:8000/showfor/")
    return render(request,'edit.html',{'form':form})

def updateforar(request,id):
    up=formations.objects.get(id=id)
    form=formationForm(instance=up)
    if request.method=='POST':
        form=formationForm(request.POST,instance=up)
        if form.is_valid():
            form.save()
            return redirect("http://127.0.0.1:8000/showforar/")
    return render(request,'edit.html',{'form':form})

