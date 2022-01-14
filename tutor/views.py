from django.http.response import Http404
from django.http import JsonResponse
from rest_framework import permissions
from rest_framework import generics,mixins
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from .serializers import *
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from rest_framework.views import APIView
from django.contrib.auth import authenticate, login,get_user_model
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authentication import TokenAuthentication
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from geopy.geocoders import Nominatim
from geopy.distance import great_circle

username='mathtutor4655@gmail.com'
password='tushar1234'

geolocator = Nominatim(user_agent="tutor")
x1=27.156200
y1=76.852100
usloca=(x1,y1)


User =get_user_model()

# deserilizing saving an data instance by json request method
#it works as first deseriliaer converts json data to pyhton datatype 



def send_mail(html=None,text='',subject='you have successfully re as a math tutor',from_email='mathtutor4655@gmail.com',to_emails=[]):
    assert isinstance(to_emails,list)
    msg=MIMEMultipart('alternative')
    msg['From']=from_email
    msg['To']=", ".join(to_emails)
    msg['Subject']=subject
    txt_part=MIMEText(text,'plain')
    msg.attach(txt_part)
    html_part = MIMEText(f"<p>Here is your password reset token</p><h1>{html}</h1>", 'html')
    msg.attach(html_part)
    msg_str=msg.as_string()
    print("yoyo")
    server=smtplib.SMTP(host='smtp.gmail.com',port=587)
    server.ehlo()
    server.starttls()
    server.login(username,password)
    server.sendmail(from_email,to_emails,msg_str)
    server.quit()



class macreateView(generics.GenericAPIView):

   # permission_classes = (permissions.IsAuthenticated,IsOwnerOrReadOnly)
    serializer_class = macreateserializer
    def post(self, request):
        serializer = self.get_serializer(data=request.data,context={'request': request})
        serializer.is_valid(raise_exception=True)
        y=serializer.save()    # here y is an object instance means y is what its serilizer create funtion returns
        print(y.matutor.id)
        print(serializer)
        tex='congrats {y.matutor.username} you finnaly applied as an mathtutor at our mytutor organization'
        send_mail(text=tex,to_emails=[y.matutor.email])
        #serilizer.data is actually deserilizing the instance created now it is converting pyhton model to pyhton dict
        return Response(serializer.data,status=status.HTTP_200_OK)

class malistView(generics.GenericAPIView):
    # one parameter i am taking throug form is the distance upto which user wants to serarch tutors
    serializer_class = macreateserializer
    def post(self, request): 
        apr=request.data['range']
        apr=int(apr)
        print(apr)
        q1=mathtutor.objects.all()
        for obj in q1.iterator():
            q1.filter(pk=obj.pk).update(dis=True)
            
        for obj in q1.iterator():    
            lat=obj.lati
            lon=obj.longi
            loca=(lat,lon)
            x3=great_circle(loca,usloca).km
            q1.filter(pk=obj.pk).update(distance=x3)
            if (x3>apr ):
                q1.filter(pk=obj.pk).update(dis=False)
            else:
                print(x3)
       
        q2=q1.filter(dis=True)      
        serializer=self.get_serializer(q2,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

class UserProfileView(generics.GenericAPIView):
    serializer_class= macreateserializer
    def get(self,request,id):
        userr=get_object_or_404(mathtutor,id=id)
        print(userr)
        serializer= self.get_serializer(userr)
        return Response(serializer.data,status=status.HTTP_200_OK)



            

            







        




       