import datetime
from django.contrib.auth.models import User
from rest_framework import serializers
from .models import *
 

class WalletTableSerializer(serializers.ModelSerializer):
    user_data  = serializers.PrimaryKeyRelatedField(write_only=True, queryset=UserTable.objects.all())

  
    class Meta:
        model = WalletTable
        fields = ('wallet_id', 'user_data', 'ov_cash', 'ovr_cash', 'total_ov_cash', 'total_ovr_cash', 'achiver_cash_back', 'reward_and_prices', 'is_active', 'create_at', 'comment', 'status')

  

class Wallet2TableSerializer(serializers.ModelSerializer):
    user_data  = serializers.PrimaryKeyRelatedField(write_only=True, queryset=UserTable.objects.all())

  
    class Meta:
        model = WalletTable
        fields = ('wallet_id', 'user_data', 'ov_cash', 'ovr_cash', 'total_ov_cash', 'total_ovr_cash', 'achiver_cash_back', 'reward_and_prices', 'is_active', 'create_at', 'comment', 'status')

 

class Wallet3TableSerializer(serializers.ModelSerializer):
    user_data  = serializers.PrimaryKeyRelatedField(write_only=True, queryset=UserTable.objects.all())

  
    class Meta:
        model = WalletTable
        fields = ('wallet_id', 'user_data', 'ov_cash', 'ovr_cash', 'total_ov_cash', 'total_ovr_cash', 'achiver_cash_back', 'reward_and_prices', 'is_active', 'create_at', 'comment', 'status')

 

class Wallet4TableSerializer(serializers.ModelSerializer):
    user_data  = serializers.PrimaryKeyRelatedField(write_only=True, queryset=UserTable.objects.all())

  
    class Meta:
        model = WalletTable
        fields = ('wallet_id', 'user_data', 'ov_cash', 'ovr_cash', 'total_ov_cash', 'total_ovr_cash', 'achiver_cash_back', 'reward_and_prices', 'is_active', 'create_at', 'comment', 'status')


class Wallet5TableSerializer(serializers.ModelSerializer):
    user_data  = serializers.PrimaryKeyRelatedField(write_only=True, queryset=UserTable.objects.all())

  
    class Meta:
        model = WalletTable
        fields = ('wallet_id', 'user_data', 'ov_cash', 'ovr_cash', 'total_ov_cash', 'total_ovr_cash', 'achiver_cash_back', 'reward_and_prices', 'is_active', 'create_at', 'comment', 'status')
 
