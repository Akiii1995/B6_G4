"""B6_Book URL Configuration

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
from django.urls import path,include,re_path
from B6_Book.Book_App.views_0 import views_3

from Book_App import views
from Book_App.views_0 import views_3
print("in url.py")


urlpatterns = [
    path('admin/', admin.site.urls),
    path("home/",views.homepage,name="homepage"),
    path('show-all-books/',views.show_all_books,name="show_all_books"),
    path('edit/<int:id>',views.edit_data,name="edit"),
    path('delete/<int:id>',views.delete_data,name="delete"),
    path('delete-books',views.delete_all_books,name="delete-books"),
    path('soft-delete/<int:id>',views.soft_delete_data,name="soft delete"),
    path('json',views.Restore_All_Data,name='json'),
    path('form-home',views.form_home,name='form-home'),
    # path('Book-order',views.Book_order,name ='Book-order'),
    path('crispy-form',views.crispy_form,name='crispy-form'),
    path('book-adding-cart',views_3.book_add_to_cart,nmae = 'book-add-tp-cart'),
    path('user-login/',views_3.login_func,name = 'user_login'),
    

    
    
    
    
         
]

# urlpatterns = [
#     re_path(r'^Mumbai$', views.view_a, name='view_a'),
#     re_path(r'^Calcutta$', views.view_b, name='view_b'),
#     re_path(r'^Pune$', views.view_c, name='view_c'),
#     re_path(r'^Delhi$', views.view_d, name='view_d'),
# ]

# urlpatterns = [
#     re_path(r'^aaa$', views.add, name='view_a'),
#     re_path(r'^bbb$', views.divi, name='view_b'),
#     re_path(r'^ccc$', views.mul, name='view_c'),
#     re_path(r'^ddd$', views.minus, name='view_d'),
# ]

# urlpatterns = [
#     re_path(r'1', views.first_stud, name='view_a'),
#     re_path(r'2', views.second_stud, name='view_b'),
#     re_path(r'3', views.third_stud, name='view_c'),
#     re_path(r'4', views.fourth_stud, name='view_d'),
# ]

# urlpatterns = [
#     re_path(r'^aaa$', views.view_a, name='view_a'),
#     re_path(r'^bbb$', views.view_b, name='view_b'),
#     re_path(r'^ccc$', views.view_c, name='view_c'),
#     re_path(r'^ddd$', views.view_d, name='view_d'),
# ]
# urlpatterns = [
#     re_path(r'^ccc$', views.show_all_books, name='view_a'),
#     ]

# urlpatterns = [
#     re_path(r'^Sangli$', views_0.city1, name='view_a'),
#     re_path(r'^Kolhapur$', views_0.city2, name='view_b'),
#     re_path(r'^Nashik$', views_0.city3, name='view_c'),
#     re_path(r'^Nanded$', views_0.city4, name='view_d'),
# ]


urlpatterns+=[
    path('__debug__/', include('debug_toolbar.urls')),

]