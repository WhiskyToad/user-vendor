import graphene
from graphene_django import DjangoObjectType

from .models import Vendor


class VendorType(DjangoObjectType):
    class Meta:
        model = Vendor
        fields = ("id", "store_name")


class Query(graphene.ObjectType):
    get_Vendor = graphene.Field(VendorType, id=graphene.ID(required=True))


schema = graphene.Schema(Query)
