
from django.shortcuts import render,redirect
import requests
import json
from django.http import JsonResponse
import openai
from django.contrib import messages
import razorpay
from HealthApp.models import MealPlansDb,ShopCategoryDb,ShopProductDb,videoDb,WorkoutPlansDb,BlogDb
from WebApp.models import SignUpDb,CartDb,OrderDb,ContactDb
from WebApp.forms import *
from .utils import *

openai.api_key = "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"


# Create your views here.
def Home(re):
    name = re.session.get('name')  # Use get() to safely access the key
    if not name:
        return redirect(SignIn)  # Redirect to SignIn if the user is not logged in
    x=CartDb.objects.filter(name=name)
    cart=x.count()
    Blogs=BlogDb.objects.all()
    daily_quote=fetch_fitness_quote()
    return render(re,'Home.html',{'cart':cart,'Blogs':Blogs,"daily_quote":daily_quote})


def Dashboard(request):
    data=SignUpDb.objects.filter(name=request.session['name'])
    if request.method == 'POST':
        query = request.POST.get('query', '').strip()  # Safely fetch the query
        api_url = 'https://api.calorieninjas.com/v1/nutrition?query='
        headers = {'X-Api-Key': 'o3t54D+t/feLQyikOG8/dg==Ud0nYD7HQerYLJhJ'}

        try:
            # Make the API request
            response = requests.get(api_url + query, headers=headers)
            response.raise_for_status()  # Raise HTTPError for bad status codes

            # Parse JSON response
            api_data = response.json().get('items', [])

            if api_data:  # Ensure the API returned items
                item = api_data[0]
                calories = item.get('calories', 0)

                # Calculate activity times
                jog_minutes = round(calories / 378 * 60, 0)  # Jogging
                yoga_minutes = round(calories / 223 * 60, 0)  # Yoga
                gym_minutes = round(calories / 483 * 60, 0)  # Gym workout
                walk_minutes = round(calories / 294 * 60, 0)  # Brisk walk

                return render(
                    request,
                    'Dashboard.html',
                    {
                        'api': item,
                        'jog_minutes': jog_minutes,
                        'yoga_minutes': yoga_minutes,
                        'gym_minutes': gym_minutes,
                        'walk_minutes': walk_minutes,
                    },
                )
            else:
                return render(request, 'Dashboard.html', {'data':data,'error': 'No data found. Please try another query.'})

        except requests.exceptions.RequestException as e:
            # Log and handle request exceptions
            print(f"API Request Error: {e}")
            
            daily_quote=fetch_fitness_quote()

            return render(request, 'Dashboard.html', {'data':data,'error': 'Failed to fetch data from the API.',"daily_quote":daily_quote})
            

    return render(request, 'Dashboard.html',{'data':data})  # Render form for GET request

def Dishes(re):
    diet=MealPlansDb.objects.all()
    return render(re,'Dishes.html',{'diet':diet})
def ShopCategory(re):
    name = re.session.get('name')  # Use get() to safely access the key
    if not name:
        return redirect(SignIn)  # Redirect to SignIn if the user is not logged in
    x=CartDb.objects.filter(name=name)
    cart=x.count()
    cat=ShopCategoryDb.objects.all()
    return render(re,'Shop-Category.html',{'cat':cat,'cart':cart})
def ProductsFiltered(re,CatName):
    pro=ShopProductDb.objects.filter(Category=CatName)
    cat1=ShopCategoryDb.objects.filter(CategoryName=CatName)
    return render(re,'ProductsFiltered.html',{'pro':pro,'cat1':cat1})

def SingleProduct(re,P_id):
    pro1=ShopProductDb.objects.filter(id=P_id)
    return render(re,'SingleProduct.html',{'pro1':pro1})

def IntroExercise(re):
    return render(re,'IntroExercise.html')

def ExerciseTutorials(re):
    Tutorial=videoDb.objects.all()
    return render(re,'ExerciseTutorials.html',{'Tutorial':Tutorial})


def WLRoutines(request, objective):
    wLoss = WorkoutPlansDb.objects.filter(FObjective=objective)  # Filter by the value, e.g., "WeightLoss"
    return render(request, 'Routines-wl.html', {'wLoss': wLoss})

def WGRoutines(request, objective):
    wGain = WorkoutPlansDb.objects.filter(FObjective=objective)
    return render(request, 'Routines-wg.html', {'wGain': wGain})

def WMRoutines(request, objective):
    wMaintain = WorkoutPlansDb.objects.filter(FObjective=objective)
    return render(request, 'Routines-M.html', {'wMaintain': wMaintain})

def SingleRoutine(re,Rid):
    data=WorkoutPlansDb.objects.filter(id=Rid)
    return render(re,'SingleRoutine.html',{'data':data})

def About(re):
    return render(re,'About.html')

def SignIn(re):
    return render(re,'SignIn.html')

def SignUp(re):
    return render(re,'SignUp.html')

def SaveSignUp(re):
    a1=re.POST.get('name')
    a2=re.POST.get('age')
    a3=re.POST.get('gender')
    a4=re.POST.get('objective')
    b1=re.POST.get('email')
    d1=re.POST.get('pass1')
    e1=re.POST.get('pass2')
    obj=SignUpDb(name=a1,age=a2,gender=a3,objective=a4,email=b1,pass1=d1,pass2=e1)
    if SignUpDb.objects.filter(name=a1).exists():
        messages.warning(re,"User already exits...!")
        return redirect(SignUp)
    elif SignUpDb.objects.filter(email=b1).exists():
        messages.warning(re, "User already exits...!")
        return redirect(SignUp)
    obj.save()
    return redirect(Home)


def UserLogin(request):
    if request.method=="POST":
        un=request.POST.get('name')
        pwd=request.POST.get('pass1')
        if SignUpDb.objects.filter(name=un,pass1=pwd).exists():
            request.session['name']=un
            request.session['pass1']=pwd
            return redirect(Home)
        else:
            return redirect(SignIn)
    else:
        return redirect(SignIn)

def UserLogout(request):
    del request.session['name']
    del request.session['pass1']
    return redirect(SignIn)

def SaveCart(re):
    a3=re.POST.get('name')
    b3=re.POST.get('ProductName')
    b4=re.POST.get('ProductImage')
    c3=re.POST.get('quantity')
    d3=re.POST.get('Price')
    e3=re.POST.get('total')
    obj=CartDb(name=a3,ProductName=b3,ProductImage=b4,quantity=c3,Price=d3,total=e3)
    obj.save()
    return redirect(CartPage)
def CartPage(re):
    items=CartDb.objects.filter(name=re.session['name'])
    x=items.count()
    SubTotal = 0
    ShippingAmount = 0
    TotalAmount = 0
    for i in items:
            if i.total:  # Check if i.total is not empty or None
                SubTotal += int(i.total)
            else:
                # Handle the case where total is empty, e.g., set it to 0 or log a warning
                SubTotal +=0
            if SubTotal >2000:
             ShippingAmount =0
            else:
             ShippingAmount =200
             TotalAmount = ShippingAmount + SubTotal

    return render(re,'CartPage.html',{'items':items,'x':x,'SubTotal':SubTotal,'ShippingAmount':ShippingAmount,'TotalAmount':TotalAmount})
def RemoveCart(re,id1):
    x=CartDb.objects.filter(id=id1)
    x.delete()
    return redirect(CartPage)
def Checkout(re):
    items = CartDb.objects.filter(name=re.session['name'])
    x = items.count()
    SubTotal = 0
    ShippingAmount = 0
    TotalAmount = 0
    for i in items:
        if i.total:  # Check if i.total is not empty or None
            SubTotal += int(i.total)
        else:
            # Handle the case where total is empty, e.g., set it to 0 or log a warning
            SubTotal += 0
        if SubTotal > 2000:
            ShippingAmount = 0
        else:
            ShippingAmount = 200
            TotalAmount = ShippingAmount + SubTotal

    return render(re, 'Checkout.html', {'items': items, 'x': x, 'SubTotal': SubTotal, 'ShippingAmount': ShippingAmount,
                                        'TotalAmount': TotalAmount})
def OrderSave(re):
    p1=re.POST.get('Name')
    p2=re.POST.get('Place')
    p3=re.POST.get('Email')
    p4=re.POST.get('Phone')
    p5=re.POST.get('Address')
    p6=re.POST.get('Total')
    p7=re.POST.get('Messages')
    obj=OrderDb(Name=p1,Place=p2,Email=p3,Phone=p4,Address=p5,Total=p6,Messages=p7)
    obj.save()
    return redirect(Payment)

def Payment(re):
    # Retrieve the data from OrderDb with the specified ID in reverse order

    customer = OrderDb.objects.order_by('-id').first()

    # Get the payment amount of the specified customer

    pay = customer.Total
    # convert the amount into paisa(Smallest currency unit)
    amount = int(pay * 100)
    pay_str = str(amount)

    for i in pay_str:
        print(i)
        if re.method == "POST":
            order_currency = 'INR'
            client = razorpay.Client(auth=('rzp_test_XrSOnebWyMTP0h', 'dkXxPnKjW8WLpIREIadMAfzv'))
            payment = client.order.create({'amount': amount, 'currency': order_currency})
        return render(re, 'Payment.html', {'customer': customer, 'pay_str': pay_str})

def Blog(re):
    blogs=BlogDb.objects.all()
    return render(re,'Blog.html',{'blogs':blogs})

def SingleBlog(re,id1):
    bl=BlogDb.objects.get(id=id1)
    blog=BlogDb.objects.all()
    return render(re,'SingleBlog.html',{'bl':bl})
def Contact(re):
    context={}
    context['form']=ContactForm
    return render(re,'Contact.html',context)
def SaveContact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)  # Pass POST data
        if form.is_valid():
            form.save()  # This will save the form data to the ContactDb model
            return redirect('Contact')  # Redirect after successful form submission
    else:
        form = ContactForm()  # Empty form for GET request
    
    return render(request, 'Contact.html', {'form': form})

def DietIntro(re):
    return render(re,'Dietintro.html')