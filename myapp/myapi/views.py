from rest_framework import authentication, viewsets
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

from .serializers import HeroSerializer
from .models import Hero

from .serializers import StudentSerializer
from .models import Student

from .serializers import AgentSerializer
from .models import Agent

from .serializers import UniSerializer
from .models import Uni

from .serializers import UserSerializer
from .models import User

from .serializers import PostSerializer
from .models import Post


from .serializers import ProductSerializer
from .models import Product

from .serializers import ServiceSerializer
from .models import Service

from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status

class HeroViewSet(viewsets.ModelViewSet):
    queryset = Hero.objects.all().order_by('name')
    serializer_class = HeroSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all().order_by('name')
    serializer_class = StudentSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
class AgentViewSet(viewsets.ModelViewSet):
    queryset = Agent.objects.all().order_by('name')
    serializer_class = AgentSerializer
    
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('email')
    serializer_class = UserSerializer    

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('id')
    serializer_class = ProductSerializer    

class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all().order_by('id')
    serializer_class = ServiceSerializer        
    
class UniViewSet(viewsets.ModelViewSet):
    queryset = Uni.objects.all().order_by('name')
    serializer_class = UniSerializer    
    
class PostView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def get(self, request, *args, **kwargs):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        posts_serializer = PostSerializer(data=request.data)
        if posts_serializer.is_valid():
            posts_serializer.save()
            return Response(posts_serializer.data, status=status.HTTP_201_CREATED)
        else:
            print('error', posts_serializer.errors)
            return Response(posts_serializer.errors, status=status.HTTP_400_BAD_REQUEST)    
# Create your views here.
