from rest_framework import serializers
from .models import Batch, BatchIntegrity, TimestampTransaction
from django.core.validators import RegexValidator
from rest_framework.validators import UniqueTogetherValidator


class TimestampTransactionSerializer(serializers.ModelSerializer):

    txid = serializers.CharField(
        max_length=64,
        validators=[
            RegexValidator(
                regex='^.{64}$',
                message='Incorrect txid length, must be 64',
                code='txid64')])
    sender_raddress = serializers.CharField(
        max_length=34,
        validators=[
            RegexValidator(
                regex='^.{34}$',
                message='Incorrect raddress length, must be 34',
                code='raddress34')])

    class Meta:
        model = TimestampTransaction
        fields = ('id', 'sender_raddress', 'sender_name', 'tsintegrity', 'txid')


class BatchIntegritySerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    tx_list = TimestampTransactionSerializer(many=True, read_only=True)

    class Meta:
        model = BatchIntegrity
        fields = ('id', 'integrity_address', 'integrity_pre_tx', 'integrity_post_tx', 'batch', 'tx_list', 'batch_lot_raddress', 'offline_wallet_sent')


class BatchSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    integrity_details = BatchIntegritySerializer(read_only=True)

    class Meta:
        model = Batch
        fields = ('id', 'anfp', 'dfp', 'bnfp', 'pds', 'pde', 'jds', 'jde', 'bbd', 'pc', 'pl', 'rmn', 'pon', 'pop', 'mass', 'raw_json', 'integrity_details', 'created_at')
        validators = [
            UniqueTogetherValidator(
                queryset=Batch.objects.all(),
                fields=['bnfp']
            )
        ]
