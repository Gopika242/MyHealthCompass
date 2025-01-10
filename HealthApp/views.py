from django.shortcuts import render,redirect
from HealthApp.models import ShopCategoryDb,ShopProductDb,MealPlansDb,videoDb,WorkoutPlansDb,BlogDb
from django.utils.datastructures import MultiValueDictKeyError
from django.core.files.storage import FileSystemStorage
import datetime
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib import messages


# Create your views here.
#Index
def Index(re):
    count1=ShopCategoryDb.objects.count()
    ProCount=ShopProductDb.objects.count()
    MealsCount=MealPlansDb.objects.count()
    WPlans=WorkoutPlansDb.objects.count()
    workouts=videoDb.objects.count()
    date=datetime.datetime.now()
    return render(re,'Index.html',{'date':date,'count1':count1,'ProCount':ProCount,'MealsCount':MealsCount,'WPlans':WPlans,'workouts':workouts})

#Categories-CRED


def AddShopCategory(re):

    return render(re,'AddShopCategories.html')
def SaveCategory(re):
    if re.method=="POST":
     a=re.POST.get('CategoryName')
     b=re.FILES['CategoryImage']
     c=re.POST.get('Description')
     obj=ShopCategoryDb(CategoryName=a,CategoryImage=b,Description=c)
     obj.save()
     messages.success(re, "Category added successfully")
     return redirect(AddShopCategory)
def ViewCategory(re):
    cat=ShopCategoryDb.objects.all()
    return render(re,'ViewCategory.html',{'cat':cat})
def EditCategory(re,CE_Id):
    EditData=ShopCategoryDb.objects.get(id=CE_Id)
    return render(re,'EditCategory.html',{'EditData':EditData})

def UpdateCategory(re,CU_Id):
    if re.method=="POST":

     a11=re.POST.get('CategoryName')
     c11 = re.POST.get('Description')
     try:
         img=re.FILES['CategoryImage']
         fs=FileSystemStorage()
         file=fs.save(img.name,img)
     except MultiValueDictKeyError:
         file=ShopCategoryDb.objects.get(id=CU_Id).CategoryImage
    ShopCategoryDb.objects.filter(id=CU_Id).update(CategoryName=a11,Description=c11,CategoryImage=file)
    return redirect(ViewCategory)

def DeleteCategory(re,DE_Id):
    x=ShopCategoryDb.objects.filter(id=DE_Id)
    x.delete()
    messages.error(re, "Category removed")
    return redirect(ViewCategory)

# Products-CRED

def AddProducts(re):
    category=ShopCategoryDb.objects.all()

    return render(re,'AddProducts.html',{'category':category})

def SaveProduct(re):
    if re.method=="POST":
        a22=re.POST.get('Category')
        a2=re.POST.get('ProductName')
        b2=re.FILES['ProductImage']
        c2=re.POST.get('ProductDescription')
        d2=re.POST.get('Price')
        ab=ShopProductDb(Category=a22,ProductName=a2,ProductImage=b2,ProductDescription=c2,Price=d2)
        ab.save()
        messages.success(re, "Products added successfully")
        return redirect(AddProducts)

def ViewProduct(re):
    products=ShopProductDb.objects.all()
    return render(re,'ViewProduct.html',{'products':products})

def EditProduct(re,EP_Id):
    pro=ShopProductDb.objects.get(id=EP_Id)
    cat1=ShopCategoryDb.objects.all()
    return render(re,'EditProduct.html',{'pro':pro,'cat1':cat1})

def UpdateProduct(re,UP_Id):
    if re.method=="POST":
        a223=re.POST.get('Category')
        a21=re.POST.get('ProductName')
        c21=re.POST.get('ProductDescription')
        d21=re.POST.get('Price')
        try:
            b21=re.FILES['ProductImage']
            fs=FileSystemStorage()
            file=fs.save(b21.name,b21)
        except MultiValueDictKeyError:
            file=ShopProductDb.objects.get(id=UP_Id).ProductImage
        ShopProductDb.objects.filter(id=UP_Id).update(Category=a223,ProductName=a21,ProductImage=file,ProductDescription=c21,Price=d21)
        return redirect(ViewProduct)

def DeleteProduct(re,DP_Id):
    y=ShopProductDb.objects.filter(id=DP_Id)
    y.delete()
    messages.error(re, "Product removed")
    return redirect(ViewProduct)

# MealPlans

def AddMealPlans(re):

    return render(re,'AddMealPlan.html')
def SaveMealPlans(re):
    if re.method=="POST":
     a31= re.POST.get('Objective')
     b31= re.POST.get('Diet')
     g2=re.POST.get('Plan')
     a3 = re.POST.get('BreakFast')
     b3 = re.POST.get('BCalorie')
     c3 = re.FILES['BImage']
     d3 = re.POST.get('Lunch')
     e3 = re.POST.get('LCalorie')
     f3 = re.FILES['LImage']
     g3 = re.POST.get('Dinner')
     h3 = re.POST.get('DCalorie')
     i3 = re.FILES['DImage']
     obj=MealPlansDb(Objective=a31,Diet=b31,Plan=g2,BreakFast=a3,BCalorie=b3,BImage=c3,Lunch=d3,LCalorie=e3,LImage=f3,Dinner=g3,DCalorie=h3,DImage=i3)
     obj.save()
     messages.success(re, "Meals added successfully")
     return redirect(AddMealPlans)

def ViewMealPlans(re):
    meals=MealPlansDb.objects.all()
    return render(re,'ViewMealPlan.html',{'meals':meals})

def DeleteMeals(re,DM_Id):
    x=MealPlansDb.objects.filter(id=DM_Id)
    x.delete()
    messages.error(re, "MealPlan removed")
    return redirect(ViewMealPlans)
def EditMeals(re,EM_Id):
    edit=MealPlansDb.objects.get(id=EM_Id)
    return render(re,'EditMeals.html',{'edit':edit})

def UpdateMeals(re,UM_Id):
    a41= re.POST.get('Objective')
    b41= re.POST.get('Diet')
    g1=re.POST.get('Plan')
    a4= re.POST.get('BreakFast')
    b4= re.POST.get('BCalorie')

    d4= re.POST.get('Lunch')
    e4= re.POST.get('LCalorie')

    g4= re.POST.get('Dinner')
    h4= re.POST.get('DCalorie')

    try:
        c4= re.FILES['BImage']
        fs=FileSystemStorage()
        file=fs.save(c4.name,c4)
    except MultiValueDictKeyError:
        file=MealPlansDb.objects.get(id=UM_Id).BImage
    try:
        f4= re.FILES['LImage']
        fs=FileSystemStorage()
        file1=fs.save(f4.name,f4)
    except MultiValueDictKeyError:
        file1=MealPlansDb.objects.get(id=UM_Id).LImage
    try:
        i4=re.FILES['DImage']
        fs=FileSystemStorage()
        file2=fs.save(i4.name,i4)
    except MultiValueDictKeyError:
        file2=MealPlansDb.objects.get(id=UM_Id).DImage
    MealPlansDb.objects.filter(id=UM_Id).update(Objective=a41,Diet=b41,Plan=g1,BreakFast=a4,BCalorie=b4,BImage=file,Lunch=d4,LCalorie=e4,LImage=file1,Dinner=g4,DCalorie=h4,DImage=file2)
    return redirect(ViewMealPlans)

#AdminLogin

def LoginPage(re):
    return render(re,'AdminLogin.html')

def AdminLogin(request):
    if request.method=="POST":
        un=request.POST.get('name')
        pswd=request.POST.get('pass')
        if User.objects.filter(username__contains=un).exists():
            user=authenticate(username=un,password=pswd)
            if user is not None:
                login(request, user)
                request.session['username']=un
                request.session['password']=pswd
                messages.success(request,"Welcome..!")
                return redirect(Index)
            else:
                messages.error(request,"Please check your password!")
                return redirect(LoginPage)
        else:
            messages.warning(request, "Invalid Username!")
            return redirect(LoginPage)

def admin_logout(request):
    del request.session['username']
    del request.session['password']
    messages.error(request,"Logged out!")
    return redirect(LoginPage)

#ExercisePlans

def addExercise(re):

    return render(re,'AddExercises.html')
def SaveExercise(re):
    ob=re.POST.get('Objective1')
    ca=re.POST.get('caption')
    vi=re.FILES['video']
    cal=re.POST.get('calorie')
    de=re.POST.get('EDescription')
    data=videoDb(Objective1=ob,caption=ca,video=vi,calorie=cal,EDescription=de)
    data.save()
    messages.success(re, "Workout added successfully")
    return redirect(addExercise)

def ViewExercise(re):
    plans=videoDb.objects.all()
    return render(re,'ViewExercises.html',{'plans':plans})

def DeleteExercises(re,DelId):
    x=videoDb.objects.filter(id=DelId)
    x.delete()
    messages.error(re, "Workout deleted!")
    return redirect(ViewExercise)

#WorkoutPlans
def AddWorkoutPlans(re):
    return render(re,"AddWorkoutplans.html")

def SaveWorkoutPlans(re):
    T1=re.POST.get('Title')
    O1=re.POST.get('FObjective')
    M1=re.POST.get('Monday')
    T2=re.POST.get('Tuesday')
    W1=re.POST.get('Wednesday')
    TH1=re.POST.get('Thursday')
    F1=re.POST.get('Friday')
    SA1=re.POST.get('Saturday')
    SU1=re.POST.get('Sunday')
    WPlans=WorkoutPlansDb(Title=T1,FObjective=O1,Monday=M1,Tuesday=T2,Wednesday=W1,Thursday=TH1,Friday=F1,Saturday=SA1,Sunday=SU1)
    WPlans.save()
    return redirect(AddWorkoutPlans)

def ViewWorkoutPlans(re):
    wplans=WorkoutPlansDb.objects.all()
    return render(re,'ViewPlans.html',{'wplans':wplans})

def EditWplans(re,WeId):
    Edit=WorkoutPlansDb.objects.get(id=WeId)
    return render(re,'EditWplans.html',{'Edit':Edit})

def UpdateWPlans(re,WuId):
    T11=re.POST.get('Title')
    O11=re.POST.get('FObjective')
    M11=re.POST.get('Monday')
    T21=re.POST.get('Tuesday')
    W11=re.POST.get('Wednesday')
    TH11=re.POST.get('Thursday')
    F11=re.POST.get('Friday')
    SA11=re.POST.get('Saturday')
    SU11=re.POST.get('Sunday')
    WorkoutPlansDb.objects.filter(id=WuId).update(Title=T11,FObjective=O11,Monday=M11,Tuesday=T21,Wednesday=W11,Thursday=TH11,Friday=F11,Saturday=SA11,Sunday=SU11)
    return redirect(ViewWorkoutPlans)

def DeleteWplans(re,DwId):
    x=WorkoutPlansDb.objects.filter(id=DwId)
    x.delete()
    return redirect(ViewWorkoutPlans)

def AddBlog(re):
    return render(re,'addBlog.html')
def SaveBlog(re):
    a=re.POST.get('PublishDate')
    b=re.POST.get('Heading')
    c=re.POST.get('BlogDescription')
    e=re.POST.get('intro')
    d=re.FILES['Cover']
    obj=BlogDb(PublishDate=a,Heading=b,BlogDescription=c,intro=e,Cover=d)
    obj.save()
    return redirect(AddBlog)
def ViewBlog(re):
    blog=BlogDb.objects.all()
    return render(re,'ViewBlog.html',{'blog':blog})

def EditBlog(re,B_id):
    Edit=BlogDb.objects.get(id=B_id)
    return render(re,'EditBlog.html',{'Edit':Edit})

def UpdateBlog(re,UpId):
    a1= re.POST.get('PublishDate')
    b1= re.POST.get('Heading')
    c1= re.POST.get('BlogDescription')
    e1=re.POST.get('intro')
    try:
     d1= re.FILES['Cover']
     fs=FileSystemStorage()
     file=fs.save(d1.name,d1)
    except MultiValueDictKeyError:
     file=BlogDb.objects.get(id=UpId).Cover
    BlogDb.objects.filter(id=UpId).update(PublishDate=a1, Heading=b1, BlogDescription=c1, Cover=file,intro=e1)
    return redirect(ViewBlog)
def DeleteBlog(re,Did):
    x=BlogDb.objects.filter(id=Did)
    x.delete()
    return redirect(ViewBlog)

















