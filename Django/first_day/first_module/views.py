# -*- coding: utf-8 -*-
from django.shortcuts import render

# Create your views here.
def home(request):
    string = u"没有什么很难，继续加油！！"
    stringlist = ['page1', 'page2', 'page3', 'page4']
    string_dict = {'name':'jojo', 'age':'100'}
    return render(request, 'home.html', {'string_dict': string_dict})
