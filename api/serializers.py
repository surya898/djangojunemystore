from rest_framework import serializers
from api.models import products,Reviews
from django.contrib.auth.models import User
from api.models import Carts
# class productserializer(serializers.Serializer):

#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField()
#     price = serializers.IntegerField()
#     description = serializers.CharField()
#     category = serializers.CharField()
#     image = serializers.ImageField(required=False,default=None)

class productModelSerializer(serializers.ModelSerializer):
    avg_rating = serializers.CharField(read_only=True)                           #evda avg feild just read cheydamathi so readonly koduthu
    review_count = serializers.CharField(read_only = True)

    class Meta:  #class about class information

        model = products
        fields = "__all__"
        # or, fields = ["name","price","description"]


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["first_name","last_name","email","username","password"]

    def create(self, validated_data):
        return User.objects.create_user(**self.validated_data)
        

class Cartserializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only =True)
    user = serializers.CharField(read_only = True)
    product = serializers.CharField(read_only = True)
    date = serializers.CharField(read_only = True)        #becoz evida deserialization nadakunnilla.so we put these.
    class Meta:
        model = Carts
        fields = "__all__"

class Reviewseializer(serializers.ModelSerializer):
    user =serializers.CharField(read_only=True)
    product = serializers.CharField(read_only=True)
    date = serializers.CharField(read_only=True)
    class Meta:
        model = Reviews
        fields = "__all__"