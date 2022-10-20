from django.db.models import (
    Model,
    CharField,
    FloatField,
    DateField,
    ForeignKey,
    IntegerField,
    JSONField,
    OneToOneField,
    UUIDField,
    CASCADE
)
import uuid

# Create your models here.


class Batch(Model):
    id = UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    ########################################################
    # field names acronymized from spreadsheet sample (full name in comment)
    
    # UPPERCASE_COMMENT heribert orig export with data type/characteristics
    # https://github.com/The-New-Fork/sampleData/blob/master/data_r/heribert.1.orig.txt
    ########################################################
    # (article number finished product) ARTICLE_NUMBER_FINISHED_PRODUCT
    anfp = CharField(max_length=20, unique=False)
    # (description finished product) DESCRIPTION_FINISHED_PRODUCT
    dfp = CharField(max_length=40)
    # (batch number finished product) LOT_FINISHED_PRODUCT
    bnfp = CharField(max_length=10, unique=True)
    # (production day start) NONE IN ORIGINAL SAMPLE
    pds = DateField(auto_now=False, auto_now_add=False)
    # (production day end) PRODUCTION_DATE_FINISHED_PRODUCT
    pde = DateField(auto_now=False, auto_now_add=False)
    # (julian day start) NONE
    jds = IntegerField(blank=True, null=True)
    # (julian day end) NONE
    jde = IntegerField(blank=True, null=True)
    # (best before date) NONE
    bbd = DateField(auto_now=False, auto_now_add=False)
    # (production country) PRODUCTION_COUNTRY
    pc = CharField(max_length=3)
    # (production location) PRODUCTION_LOCATION
    pl = CharField(max_length=30)
    # (raw material number) NONE
    rmn = CharField(max_length=20)
    # (purchase order number) PO_NUMBER_NFC
    pon = CharField(max_length=20)
    # (purchase order position) NONE
    pop = CharField(max_length=3)
    ##############################
    mass = FloatField(blank=True, null=True)
    # integrity address & tx
    raw_json = JSONField(default=dict)
    # integrity_details = OneToOneField(Integrity, related_name="batch",  on_delete=DO_NOTHING, null=True)
    ##############################
    created_at = DateField(auto_now_add=True)
    # timestamp


class BatchIntegrity(Model):
    id = UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    integrity_address = CharField(max_length=34, null=True, unique=True)
    integrity_pre_tx = CharField(max_length=64, null=True)
    integrity_post_tx = CharField(max_length=64, null=True)
    batch_lot_raddress = CharField(max_length=34, null=True, unique=True)
    offline_wallet_sent = CharField(max_length=255, default="{}")
    batch = OneToOneField(Batch, related_name="integrity_details",  on_delete=CASCADE, null=True)


class TimestampTransaction(Model):
    tsintegrity = ForeignKey(BatchIntegrity, related_name="tx_list", on_delete=CASCADE, null=True)
    sender_raddress = CharField(max_length=34)
    sender_name = CharField(max_length=255, null=True, blank=True)
    txid = CharField(max_length=64, unique=True)

    def __str__(self):
        return self.txid
