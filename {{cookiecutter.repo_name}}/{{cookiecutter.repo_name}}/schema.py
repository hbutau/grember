import graphene

from graphene_django.types import DjangoObjectType

# create your schemae and queries here based on your models. For example:
#
#from django.contrib.auth.models import User, AbstractBaseUser
#
#class UserType(DjangoObjectType):
#    class Meta:
#        model = User
#
#class Query():
#    all_users = graphene.List(UserType)
#
#    def resolve_all_users(self, info, **kwargs):
#        return User.objects.all()
