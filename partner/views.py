#DEFAULTS
from django.forms.models import model_to_dict
from django.db import IntegrityError
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
#UTILS
from django.views.decorators.csrf import csrf_exempt
from json import loads
from app.utils import gen_uuid, verify_dict
#MODELS
from .models import Partner


class PartnerView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    @csrf_exempt
    def post(self, request):
        data = loads(request.body)
        verified_fields = verify_dict(data, ['name', 'cpf_cnpj', 'rg_ie', 'phone_number', 'email'])

        if len(verified_fields) != 0:
            return Response(verified_fields)
        
        try:
            partner = Partner.objects.create(
                uuid=gen_uuid(),
                name=data['name'],
                cpf_cnpj=data['cpf_cnpj'],
                rg_ie=data['rg_ie'],
                phone_number=data['phone_number'],
                email=data['email']
            )
            return Response(model_to_dict(partner))
        except IntegrityError as error:
            return Response({ 'message': str(error) })
    
    @csrf_exempt
    def delete(self, request):
        data = loads(request.body)
        verified_fields = verify_dict(data, ['uuid'])

        if len(verified_fields) != 0:
            return Response(verified_fields)
        
        try:
            partner = Partner.objects.get(uuid=data['uuid']).delete()
            return Response({ 'message': f"Partners that uuid is was {data['uuid']} has been deleted" })
        except ObjectDoesNotExist as error:
            return Response({ 'message': str(error) })
    
    def get(self, request):
        partner = Partner.objects.all()
        result = []
        for part in partner:
            result.append(model_to_dict(part))
        return Response(result)