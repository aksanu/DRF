from rest_framework import serializers
from .models import Customer


class customerSerializer(serializers.Serializer):
	name= serializers.CharField(max_length=100)
	mobileNumber= serializers.IntegerField()
	address= serializers.CharField(max_length=100)


	def validate_mobileNumber(self,value):
		v= str(value)
		if len(v)<5:
			raise serializers.ValidationError('Mobile Number Length should not be less than 5')

	def validate_name(self,value):
		if value == 'Ankit' or value == 'ankit':
			raise serializers.ValidationError("Sorry he's a developer...You can't use his name")


	def create(self,validated_data):
		return Customer.objects.create(**validated_data)

	def update(self,instance, validated_data):
		instance.name= validated_data.get('name', instance.name)
		instance.mobileNumber= validated_data.get('mobileNumber', instance.mobileNumber)
		instance.address= validated_data.get('address', instance.address)
		return instance