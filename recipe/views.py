from rest_framework import viewsets,mixins
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated,IsAdminUser



from core.models import Recipe,Tag
from recipe import serializers


class RecipeViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.RecipeDetailsSerializer
    queryset =Recipe.objects.all()
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]
    def get_queryset(self):
        return self.queryset.filter(user=self.request.user).order_by('-id')
    
    
    def get_serializer_class(self):
        if self.action=='list':
            return serializers.RecipeSerializer
        return self.serializer_class
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        
class TagViewSet(mixins.UpdateModelMixin,
                 mixins.ListModelMixin,
                 viewsets.GenericViewSet):
    serializer_class=serializers.TagSerializer
    queryset=Tag.objects.all()
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]
    def get_queryset(self):
        return self.queryset.filter(user=self.request.user).order_by('-name')
    