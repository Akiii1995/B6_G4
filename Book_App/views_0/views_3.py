import http
import imp
import re
from tkinter.tix import StdButtonBox
from django.http import HttpResponse
from django.shortcuts import redirect, render
import json
from django.http import JsonResponse
from Book_App.models import Book
from django.contrib.auth import login,logout,authenticate
# Create your views here.

# from django.http import HttpResponse

import logging

# Get an instance of a logger
logger = logging.getLogger("first")

def homepage(request):
    logger.info("In Homepage view")
    all_books = Book.objects.all()  
    print(all_books)
    logger.info(all_books) 
    # return HttpResponse("Welcome to the First........!!!!!!!!!!")
    # print(request.method)
    # print(request.POST)
    name = request.POST.get("bname")
    price = request.POST.get("bprice")
    qty = request.POST.get("bqty")


    if request.method =="POST":
        '''Creating the Book Data'''
        if not request.POST.get("bid"): 
            book_name = name
            book_price = price
            book_qty = qty
            # print(book_name,book_price,book_qty)
            data = Book.objects.create(Name=book_name,Price=book_price,Qty=book_qty)    #Book data has created
            return redirect("homepage")
        else:
            bid = request.POST.get("bid")
            book_obj = Book.objects.get(id=bid)
            book_obj.Name = name
            book_obj.Price = price
            book_obj.Qty = qty
            book_obj.save()
            return redirect("homepage")     #redirecting to homepage after adding the data
            
    elif request.method=="GET":
        return render(request,template_name="home.html")


def show_all_books(request):
    '''showing all books from library'''
    logger.info(request.POST)       #info logger define
    all_books = Book.objects.all()  
    data = {"books":all_books}      #defining the context for the data
    return render(request,"show_books.html",context=data)   

def edit_data(request,id):
    '''Edit data as per the user'''
    book = Book.objects.get(id=id)  #edit data by passing the id
    cont = {"single_book":book} 
    return render(request,template_name="home.html",context=cont)            #return to homepage for editing

def delete_data(request,id):               #for deleting data we need the Primary key as a id
    '''delete data as per the user convenince'''
    if request.method =="GET":
        book = Book.objects.get(id=id)
        book.delete()                   #delete query performed
        return redirect("show_all_books")
    elif request.method=="POST":
        return HttpResponse("Error.....!!!")

def delete_all_books(request):                  #deleting the all objects from the database
    '''deleting the all the book data from database'''         
    if request.method =="GET":
        all_books = Book.objects.all()      
        data = {"books":all_books}
        return render(request,"delete_books.html",context=data)
    elif request.method =="POST":
        all_books = Book.objects.all().delete()
        data = {"books":all_books}
        return redirect("homepage")


def soft_delete_data(request,id):                               #just deleting data from the table not from the database
    '''here we deleting data from the table bt not from database'''
    if request.method =="GET":
        book = Book.objects.filter(Is_Active=False)
        book.delete()
        return redirect("show_all_books")
    elif request.method=="POST":
        return HttpResponse("Error.....!!!")


def Restore_All_Data(request):
    with open("Book_App.json",mode="r") as jsonfile:        #restore data from json file
        data=json.load(jsonfile) 
    
    return JsonResponse(data,safe=False)
# def view_a(request):
#     return HttpResponse("in view_a")

# def view_b(request):
#     return HttpResponse("in view_b")

# def view_c(request):
#     return HttpResponse("in view_c")

# def view_d(request):
#     return HttpResponse("in view_d")

# def add(request):
#     return HttpResponse(2+3)

# def divi(request):
#     return HttpResponse(2/5)

# def mul(request):
#     return HttpResponse(10*5)

# def minus(request):
#     return HttpResponse(10-5)

# def first_stud(request):

#     return HttpResponse("first stud is Akshay")

# def second_stud(request):
#     return HttpResponse("Second stud is Amit")

# def third_stud(request):
#     return HttpResponse("Third stud is Pankaj")

# def fourth_stud(request):
#     return HttpResponse("fourth stud is Suraj")

def book_add_to_cart(request):
    print("Book added successfully in a Cart....!!!!")

def login_func(request):
    username = request.POST.get("username")
    password = request.POST.get("password")
    user = authenticate(username,password)
    if user:
        login(request,user)
        return HttpResponse("Successfully logged in..!!!!!!")

def soft_delete_one(request,id):                               #just deleting data from the table not from the database
    '''here we deleting data from the table bt not from database'''
    if request.method =="GET":
        book = Book.objects.filter(Is_Active=False)
        book.delete()
        return redirect("show_all_books")
    elif request.method=="POST":
        return HttpResponse("Error.....!!!")