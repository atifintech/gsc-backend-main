from rest_framework import authentication, viewsets
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny

from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status

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
from .serializers import CustomUserSerializer
from .models import NewUser

from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny

# from myapp.myapi import serializers

class HeroViewSet(viewsets.ModelViewSet):
    queryset = Hero.objects.all().order_by('name')
    serializer_class = HeroSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all().order_by('name')
    serializer_class = StudentSerializer
    authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]

    # email column
    
class AgentViewSet(viewsets.ModelViewSet):
    queryset = Agent.objects.all().order_by('name')
    serializer_class = AgentSerializer
    
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('email')
    serializer_class = UserSerializer
    authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('id')
    serializer_class = ProductSerializer    

class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all().order_by('id')
    serializer_class = ServiceSerializer        
    
class UniViewSet(viewsets.ModelViewSet):
    queryset = Uni.objects.all().order_by('name')
    serializer_class = UniSerializer

# class NewUserViewSet(viewsets.ModelViewSet):
#     queryset = NewUser.objects.all().order_by('email')
#     serializer_class = NewUserSerializer
#     authentication_classes = [JWTAuthentication]
#     # permission_classes = [IsAuthenticated]      
    
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

# class RegisterView(APIView):

#     def post(self, request):
#         serializer = UserSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)


class CustomUserCreate(APIView):
    permission_classes = [AllowAny]

    def post(self, request, format='json'):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                json = serializer.data
                return Response(json, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BlacklistTokenUpdateView(APIView):
    permission_classes = [AllowAny]
    authentication_classes = ()

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)

# Create your views here.