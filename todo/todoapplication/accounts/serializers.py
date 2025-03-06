from rest_framework import serializers
from .models import User

class UserSerialezer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=["id","email","username","password"]
        extra_kwargs={"password":{"write_only":True}}

    def create(self , validated_data):
        user=User.objects.create_user(**validated_data)
        return user    
    






# Serializers ka use Django models ko JSON format me convert karne ke liye hota hai, taaki data APIs me send/receive kiya ja sake.    
# serializers.ModelSerializer → Ye Django model ke fields ko automatically serialize kar deta hai.

# User.objects.create_user(**validated_data)

#     Django ka built-in create_user method ka use ho raha hai jo password ko hash (encrypt) kar deta hai.
#     Agar hum User.objects.create(**validated_data) use karein, to password plaintext (unencrypted) store hoga, jo security issue hai.