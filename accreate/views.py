from django import forms
from django.contrib.auth.models import User
from django.http import request
from django.http.response import HttpResponse
from django.shortcuts import redirect, render,HttpResponse

# Create your views here.

from .forms import CForm

from. models import Catalog

from xml.etree import ElementTree as ET
import threading
from django.db.models import Q

from xml.etree.ElementTree import fromstring, ElementTree
import io
import xml.etree.ElementTree as ET


import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys


class WebXml:

    def webxmlR(request):
    

        if request.FILES:
           threading.Thread(target=WebXml.parser ,args=(request)).start()

        
        context={"form":CForm}
        return render(request,"accreate/wxml.html",context)





    def parser(request):
            

        
            xmlfile= request.FILES['xmlfile'].file.getvalue()
            xmlfile=xmlfile.decode('ascii')
            tree = ElementTree(ET.fromstring(xmlfile))
            
            id=request.user.id
            for data in tree.findall("PLANT"):
                common = data.find("COMMON").text
                botantical = data.find("BOTANICAL").text
                zone = data.find("ZONE").text
                light = data.find("LIGHT").text
                price = data.find("PRICE").text

                availabilty = data.find("AVAILABILITY").text

                
                query=Catalog.objects.filter(Q(user_id=request.user.id))
                
                obj=query.filter(common=common)
                print(obj)
                

                
                if obj!=None:

                    
                    print("Elemanlar güncellnecek bunun için e posta onayı alınacak")



                    
                else:
                    catalog=Catalog.objects.create(user_id=request.user.id,common=common,botanical=botantical,zone=zone,light=light,price=price,acaıkabıkıty=availabilty).save()
                    print("evres")
                    #catalog.
                

    def mail():
        print("yetişmedi ....")
        pass
       





               


    
