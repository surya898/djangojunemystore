from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from api.models import products,Carts,Reviews
from api.serializers import productModelSerializer,UserSerializer,Cartserializer,Reviewseializer
from rest_framework.viewsets import ViewSet,ModelViewSet
from rest_framework.decorators import action
from django.contrib.auth.models import User
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

class productView(APIView):
    def get(self,request,*args,**kw):
        qs = products.objects.all()
        serializer = productserializer(qs,many=True)
        return Response(data=serializer.data)
    
    def post(self,request,*args,**kw):
        serializer = productserializer(data=request.data)
        if serializer.is_valid():
            print(serializer._validated_data)
            products.objects.create(**serializer.validated_data)
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
        
    

class productdetailView(APIView):
    def get(self,request,*args,**kw):

        print(kw)
        id = kw.get('id')
        qs = products.objects.get(id=id)
        serializer = productserializer(qs)
        return Response(data=serializer.data)
    
    def put(self,request,*args,**kw):
        
        serializer = productserializer(data = request.data)

        if serializer.is_valid():
            id = kw.get("id")
            products.objects.filter(id=id).update(**request.data)
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
    
    def delete(self,request,*args,**kw):

        id = kw.get("id")
        products.objects.filter(id=id).delete()
        return Response(data="successfully deleted")
    
# class productViewsetView(ViewSet):
#         def list(self,request,*args,**kw):
#             qs = products.objects.all()
#             serializer = productModelSerializer(qs,many = True)
#             return Response(data=serializer.data)
        
#         def create(self,request,*args,**kw):
#             serializer = productserializer(data = request.data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(data=serializer.data)
#             else:
#                 return Response(data=serializer.errors)
            
#         def retrieve(self,request,*args,**kw):
#             id = kw.get("pk")
#             qs = products.objects.get(id=id)
#             serializer = productModelSerializer(qs)
#             return Response(data=serializer.data)
        
#         def destroy(self,request,*args,**kw):
#             id = kw.get("pk")
#             products.objects.filter(id = id).delete()
#             return Response(data="item deleted")
        
#         def update(self,request,*args,**kw):
#             id = kw.get("pk")
#             obj= products.objects.get(id=id)
#             serializer = productModelSerializer(data=request.data,instance=obj)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(data= serializer.data)
#             else:
#                 return Response(data=serializer.errors)

#         @action(methods=['GET'],detail=False)    
#         def categories(self,request,*args,**kw):
#             qs = products.objects.values_list('category',flat=True).distinct()
#             return Response(data=qs)

# class UserView(ViewSet):
#         def create(self,request,*args,**kw):
#             serializer = UserSerializer(data=request.data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(data=serializer.data)
#             else:
#                 return Response(data=serializer.errors)
            

class productViewsetView(ModelViewSet):

    serializer_class = productModelSerializer
    queryset = products.objects.all()
    
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    @action(methods=['GET'],detail=False)    
    def categories(self,request,*args,**kw):
            qs = products.objects.values_list('category',flat=True).distinct()
            return Response(data=qs)
    
    @action(methods=["POST"],detail=True)
    def add_cart(self,request,*args,**kw):
        id = kw.get("pk")                          # egana kodukanath cartlek onu add akunila just fetch cheyth edthamai,so serializer cheyunila
        User = request.user
        item = products.objects.get(id=id)
        User.carts_set.create(product = item)
        return Response(data="item successfully added to cart")
    
    @action(methods=['post'],detail=True)
    def add_review(self,request,*args,**kw):
        user  = request.user
        pid = kw.get('pk')
        product = self.queryset.get(id=pid)
        ser = Reviewseializer(data=request.data)
        if ser.is_valid():
            ser.save(product=product,user=user)
            return Response(data=ser.data,status=status.HTTP_201_CREATED)
        else:
            return Response(data=ser.errors,status=status.HTTP_400_BAD_REQUEST)
        

class ReviewView(APIView):
    def delete(self,request,*args,**kwargs):
        rid = kwargs.get('id')
            #evida pk koduknilla becoz apiview aan,url nammal tane set cheynm so id kodukanam
        Reviews.objects.filter(id=rid).delete()
        
        return Response(data={"msg":"deleted"},status=status.HTTP_200_OK)


class UserView(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

# class Cartview(APIView):
#     def get(self,request,*args,**kw):

#         id = kw.get('id')
#         qs = products.objects.get(id=id)
#         serializer = Cartserializer(qs)
#         return Response(data=serializer.data)

class Cartview(ModelViewSet):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Carts.objects.all()
    serializer_class = Cartserializer
    def list(self, request, *args, **kwargs):
        user = request.user
        print(User)
        carts = self.queryset.filter(user=user)
        ser = self.serializer_class(carts,many=True)
        return Response(data=ser.data,status=status.HTTP_200_OK)




        


            

        







