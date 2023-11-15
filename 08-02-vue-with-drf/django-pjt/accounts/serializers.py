from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer


class CustomRegisterSerializer(RegisterSerializer):
    # 나머지 필드들은 RegisterSerializer 에 있음 
    # 회원가입 시 추가로 필요한 필드들을 모두 정의
    nickname = serializers.CharField(required=False, allow_blank=True, max_length=255)

    