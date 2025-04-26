from django.contrib.auth.models import User, Group
from rest_framework import serializers
from rest_framework.serializers import ValidationError


class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True, write_only=True)
    email = serializers.EmailField(required=False, allow_blank=True)
    first_name = serializers.CharField(required=False, allow_blank=True)
    last_name = serializers.CharField(required=False, allow_blank=True)
    permissions = serializers.ListField(child=serializers.CharField(), required=False)
    
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'first_name', 'last_name', 'permissions')
    
    def create(self, validated_data):
        permissions_list = validated_data.pop('permissions', [])
        
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email', ''),
            password=validated_data['password'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', '')
        )
        
        # Add permissions to the user
        self._set_permissions(user, permissions_list)
        
        return user
    
    def _set_permissions(self, user, permissions_list):
        if not permissions_list:
            raise ValidationError("No permissions were requested")
            
        for permission_name in permissions_list:
            # TODO: Add real permissions
            # TODO: Setup groups with permissions
            if 'example' == permission_name.lower():
                Group.objects.get(name='example').user_set.add(user)
            else:
                raise ValidationError(f"Permission request could not be granted")
        
        user.save()