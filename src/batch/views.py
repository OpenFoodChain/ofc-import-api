from rest_framework import viewsets
import helpers.report as report
from .models import Batch, BatchIntegrity, TimestampTransaction
from .serializers import BatchSerializer, BatchIntegritySerializer, TimestampTransactionSerializer
# from rest_framework.views import APIView
# from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.decorators import action
from rest_framework.response import Response
from helpers.logging import log
import json

class BatchIntegrityView(viewsets.ModelViewSet):

    queryset = BatchIntegrity.objects.all()
    serializer_class = BatchIntegritySerializer

    def retrieve(self, request, pk):
      serializer = self.serializer_class(self.queryset, many=True)
      geturlquery = dict(request.GET.items())
      data = serializer.data[0]
      if geturlquery:
        if ("log" in geturlquery):
          offline_wallet_sent = json.loads(data["offline_wallet_sent"])
          # foodict = all(value == False for value in offline_wallet_sent.values())
          failTs = {key: offline_wallet_sent[key] for key in offline_wallet_sent if offline_wallet_sent[key] == True}
          if failTs:
            message = f"{data['id']}: Failed! {failTs}"
            log("logs/import-status.log", message, 'WARNING')
          else:
            message = f"{data['id']}: All Imported!"
            log("logs/import-status.log", message, 'INFO')
      return Response(data)

    def list(self, request, *args, **kwargs):
      serializer = self.serializer_class(self.queryset, many=True)
      geturlquery = dict(request.GET.items())
      data = serializer.data
      
      if geturlquery:
        if ("report" in geturlquery):
          data = report.batch_import_integrity(serializer.data)
      return Response(data)

class TimestampTransactionView(viewsets.ModelViewSet):
    queryset = TimestampTransaction.objects.all()
    serializer_class = TimestampTransactionSerializer


class BatchView(viewsets.ModelViewSet):
    queryset = Batch.objects.all()
    serializer_class = BatchSerializer

    def create(self, request, *args, **kwargs):
      serializer = self.get_serializer(data=request.data)
      serializer.is_valid(raise_exception=True)
      self.perform_create(serializer)
      headers = self.get_success_headers(serializer.data)
      message = f"BATCH CREATED: {str(serializer.data)}"
      log("logs/batch-import.log", message, 'INFO')
      return Response(serializer.data, status='201', headers=headers)
  
    # from https://stackoverflow.com/a/23836288
    # from https://www.django-rest-framework.org/api-guide/viewsets/
    # #marking-extra-actions-for-routing
    @action(detail=False)  # listview
    def require_integrity(self, request, pk=None):
        null_integrity = Batch.objects.filter(
            integrity_details__isnull=True
        )
        serializer = self.get_serializer(null_integrity, many=True)
        return Response(serializer.data)

