from django.urls import path
from WebApp import views
urlpatterns=[

path('Home/',views.Home,name='Home'),
path('DietIntro/',views.DietIntro,name='DietIntro'),
path('search-recipe/', views.search_recipe, name='search_recipe'),
path('Dishes/',views.Dishes,name='Dishes'),
path('ShopCategory/',views.ShopCategory,name='ShopCategory'),
path('ProductsFiltered/<CatName>/',views.ProductsFiltered,name='ProductsFiltered'),
path('SingleProduct/<int:P_id>/',views.SingleProduct,name='SingleProduct'),
path('IntroExercise/',views.IntroExercise,name='IntroExercise'),
path('ExerciseTutorials/',views.ExerciseTutorials,name='ExerciseTutorials'),
path('WLRoutines/<str:objective>/', views.WLRoutines, name='WLRoutines'),
path('WGRoutines/<str:objective>/', views.WGRoutines, name='WGRoutines'),
path('WMRoutines/<str:objective>/', views.WMRoutines, name='WMRoutines'),
path('SingleRoutine/<int:Rid>/', views.SingleRoutine, name='SingleRoutine'),
path('About/',views.About,name='About'),
path('Dashboard/',views.Dashboard,name='Dashboard'),
path('SignIn/',views.SignIn,name='SignIn'),
path('SignUp/',views.SignUp,name='SignUp'),
path('SaveSignUp/',views.SaveSignUp,name='SaveSignUp'),
path('UserLogin/',views.UserLogin,name='UserLogin'),
path('UserLogout/',views.UserLogout,name='UserLogout'),
path('SaveCart/',views.SaveCart,name='SaveCart'),
path('CartPage/',views.CartPage,name='CartPage'),
path('RemoveCart/<int:id1>/',views.RemoveCart,name='RemoveCart'),
path('Checkout/',views.Checkout,name='Checkout'),
path('Payment/',views.Payment,name='Payment'),
path('OrderSave/',views.OrderSave,name='OrderSave'),
path('Blog/',views.Blog,name='Blog'),
path('SingleBlog/<int:id1>/',views.SingleBlog,name='SingleBlog'),
path('Contact/',views.Contact,name='Contact'),
path('SaveContact/',views.SaveContact,name='SaveContact')

]