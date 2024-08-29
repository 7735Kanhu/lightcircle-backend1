from rest_framework import serializers
from .models import Myuser, Myteam, Item_Information, ItemAttribute, Stockin, Stockout, Adjust, Transaction



class StockinSerializer(serializers.ModelSerializer):

    class Meta:
        model = Stockin
        fields = '__all__'



# class ItemAttributeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ItemAttribute
#         fields = ['attribute_name', 'attribute_value', 'attribute_type']

# class ItemInformationSerializer(serializers.ModelSerializer):
#     attributes = ItemAttributeSerializer(many=True, source='itemattribute_set')

#     class Meta:
#         model = Item_Information
#         fields = ['Name', 'Barcode', 'cost', 'Price', 'image', 'initial_quantity', 'attributes']

# class StockinSerializer(serializers.ModelSerializer):
#     item = ItemInformationSerializer(source='myteam')

#     class Meta:
#         model = Stockin
#         fields = ['id', 'supplier', 'initial_quantity', 'created_at', 'memo', 'item']

# class StockoutSerializer(serializers.ModelSerializer):
#     item = ItemInformationSerializer(source='myteam')

#     class Meta:
#         model = Stockout
#         fields = ['id', 'customer', 'initial_quantity', 'created_at', 'memo', 'item']

# class AdjustSerializer(serializers.ModelSerializer):
#     item = ItemInformationSerializer(source='myteam')

#     class Meta:
#         model = Adjust
#         fields = ['id', 'initial_quantity', 'created_at', 'memo', 'item']

# class TransactionSerializer(serializers.ModelSerializer):
#     stockins = StockinSerializer(many=True, read_only=True)
#     stockouts = StockoutSerializer(many=True, read_only=True)
#     adjusts = AdjustSerializer(many=True, read_only=True)

#     class Meta:
#         model = Transaction
#         fields = ['transaction_id', 'created_at', 'stockins', 'stockouts', 'adjusts']

# class MyuserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Myuser
#         fields = ['nick_name']
