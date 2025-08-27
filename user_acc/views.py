from django.shortcuts import render
from .serializers import RegisterSerializer
from rest_framework.decorators import api_view, permission_classes, APIView
from rest_framework.validators import ValidationError
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from rest_framework.generics import GenericAPIView
from .models import CustomUser
from rest_framework.response import Response
from rest_framework import permissions, status

# Create your views here.


class RegisterApi(GenericAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = CustomUser.objects.all()
    serializer_class = RegisterSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Siz royxatdan otdingiz', 'status':status.HTTP_201_CREATED})
        return Response({'err':serializer.errors, 'status':status.HTTP_400_BAD_REQUEST})


@api_view(['GET', ])
@permission_classes([permissions.IsAuthenticated])
def test(request):
    return Response({'data':True})


class LoginApi(APIView):
    permission_classes = [permissions.AllowAny]
    def post(self, request):
        data = request.data
        email = data['email']
        password = data['password']

        if not CustomUser.objects.filter(email=email).exists():
            return Response({
                'msg':'Bunaqa loginli foydalanuvchi mavjud emas',
                'status':status.HTTP_400_BAD_REQUEST
            })

        user = authenticate(email=email, password=password)
        token = RefreshToken.for_user(user)

        data = {
            'refresh': str(token),
            'access': str(token.access_token),
            'status': status.HTTP_200_OK
        }
        return Response(data=data)


class LogoutApi(APIView):
    def post(self, request):
        data = request.data
        try:
            token = RefreshToken(data['refresh'])
            token.blacklist()
            return Response({"msg": 'chiqdingiz', "status": status.HTTP_200_OK})
        except Exception as e:
            return Response({
                "err": str(e),
                "status":status.HTTP_400_BAD_REQUEST
            })

class TokenRefresh(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        data = request.data
        try:
            token = RefreshToken(data['refresh'])
            return Response({
                "access":str(token.access_token),
                'status':status.HTTP_201_CREATED
            })
        except Exception as e:
            return Response({
                "err": str(e),
                "status":status.HTTP_400_BAD_REQUEST
            })
