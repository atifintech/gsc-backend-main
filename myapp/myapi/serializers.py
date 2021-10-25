from rest_framework import serializers

from .models import Hero
from .models import Student
from .models import Agent
from .models import Uni
from .models import Post
from .models import User
from .models import Product

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
        fields = ('id','email','name','mobile','country','gender','birth_date','birth_month','birth_year','address1','address2','prev_qualification','IELTSBand','Desiredlevel','StudyDestination','IntendedSemester','DesiredSubject' )

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id','email','usertype')        
        
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