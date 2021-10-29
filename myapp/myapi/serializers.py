from rest_framework import serializers

from .models import Hero
from .models import Student
from .models import Agent
from .models import Uni
from .models import Post
from .models import User
from .models import Product
from .models import NewUser

class HeroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Hero
        fields = ('id','name', 'alias')

class ServiceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ('id','name', 'partner','branches','product_type','approx_fee','revenue_type','duration','description')
        

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ('id','name', 'partner','branches','product_type','approx_fee','revenue_type','intake_month','duration','description')
        
class StudentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Student
        fields = ('id','name','email','mobile','country','gender','birth_date','birth_month','birth_year','address1','address2','prev_qualification','IELTSBand','Desiredlevel','StudyDestination','IntendedSemester','DesiredSubject' )

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id','name','email','usertype')

        # def create(self, validated_data):
        #     password = validated_data.pop('password', None)
            # instance = 
                    
class AgentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Agent
        fields = ('id','name','email','role','agency_name','country','mobile','website','offices','subagents','YearFounded','number_of_staff','services_provided','students_sent_abroad','association_bin','associations','recruitment_area','charge' )
        
class UniSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Uni
        fields = ('id','name','mobile','email','country','UGfee','PGfee','Diplomafee','AccomodationCost','FallSemester','SpringSemester','SummerSemester','ranking', )

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


# class NewUserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = NewUser
#         fields = '__all__'


class CustomUserSerializer(serializers.ModelSerializer):
    """
    Currently unused in preference of the below.
    """
    email = serializers.EmailField(required=True)
    user_name = serializers.CharField(required=True)
    password = serializers.CharField(min_length=8, write_only=True)

    class Meta:
        model = NewUser
        fields = ('email', 'user_name', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        # as long as the fields are the same, we can just use this
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance