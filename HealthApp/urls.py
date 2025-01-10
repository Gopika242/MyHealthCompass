from django.urls import path
from HealthApp import views
urlpatterns=[

# Categories-CRED

path('Index/',views.Index,name='Index'),
path('AddShopCategory/',views.AddShopCategory,name='AddShopCategory'),
path('SaveCategory/',views.SaveCategory,name='SaveCategory'),
path('ViewCategory/',views.ViewCategory,name='ViewCategory'),
path('EditCategory/<int:CE_Id>/',views.EditCategory,name='EditCategory'),
path('UpdateCategory/<int:CU_Id>/',views.UpdateCategory,name='UpdateCategory'),
path('DeleteCategory/<int:DE_Id>/',views.DeleteCategory,name='DeleteCategory'),

# Products-CRED

path('AddProducts/',views.AddProducts,name='AddProducts'),
path('SaveProducts/',views.SaveProduct,name='SaveProducts'),
path('ViewProducts/',views.ViewProduct,name='ViewProducts'),
path('EditProduct/<EP_Id>/',views.EditProduct,name='EditProduct'),
path('UpdateProduct/<UP_Id>/',views.UpdateProduct,name='UpdateProduct'),
path('DeleteProduct/<DP_Id>/',views.DeleteProduct,name='DeleteProduct'),

    #MealPlans

path('AddMealPlan/',views.AddMealPlans,name='AddMealPlan'),
path('SaveMealPlan/',views.SaveMealPlans,name='SaveMealPlan'),
path('ViewMealPlan/',views.ViewMealPlans,name='ViewMealPlan'),
path('DeleteMealPlan/<int:DM_Id>/',views.DeleteMeals,name='DeleteMeals'),
path('EditMealPlan/<int:EM_Id>/',views.EditMeals,name='EditMeals'),
path('UpdateMealPlan/<int:UM_Id>/',views.UpdateMeals,name='UpdateMeals'),

    #Login
path('LoginPage/',views.LoginPage,name='LoginPage'),
path('AdminLogin/',views.AdminLogin,name='AdminLogin'),
path('AdminLogout/',views.admin_logout,name='AdminLogout'),

#Exercises

path('AddExercise/',views.addExercise,name='AddExercise'),
path('SaveExercise/',views.SaveExercise,name='SaveExercise'),
path('ViewExercise/',views.ViewExercise,name='ViewExercise'),
path('DeleteExercise/<int:DelId>',views.DeleteExercises,name='DeleteExercise'),

#WorkoutPlans

path('AddWorkoutPlans/',views.AddWorkoutPlans,name='AddWorkoutPlans'),
path('SaveWorkoutPlans/',views.SaveWorkoutPlans,name='SaveWorkoutPlans'),
path('ViewWorkoutPlans/',views.ViewWorkoutPlans,name='ViewWorkoutPlans'),
path('EditWplans/<int:WeId>/',views.EditWplans,name='EditWplans'),
path('UpdateWPlans/<int:WuId>/',views.UpdateWPlans,name='UpdateWPlans'),
path('DeleteWplans/<int:DwId>/',views.DeleteWplans,name='DeleteWplans'),

    #Blog
path('AddBlog/',views.AddBlog,name='AddBlog'),
path('SaveBlog/',views.SaveBlog,name='SaveBlog'),
path('ViewBlog/',views.ViewBlog,name='ViewBlog'),
path('EditBlog/<int:B_id>/',views.EditBlog,name='EditBlog'),
path('UpdateBlog/<int:UpId>/',views.UpdateBlog,name='UpdateBlog'),
path('DeleteBlog/<int:Did>/',views.DeleteBlog,name='DeleteBlog'),

]

