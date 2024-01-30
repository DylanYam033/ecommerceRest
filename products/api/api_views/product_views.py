from base.api import GeneralListApiView
from products.api.serializers.product_serializers import ProductSerializer
from rest_framework import generics, status, viewsets
from rest_framework.response import Response

#viewset, contiene todos los metodos CRUD
class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer

    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(state=True)
        return self.get_serializer().Meta.model.objects.filter(id=pk, state=True).first()
    
    def list(self, request):
        product_serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(product_serializer.data, status=status.HTTP_200_OK)
        
    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Product created succesfully'}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def update(self, request, pk=None):
        product = self.get_queryset(pk)
        if product:
            product_serializer = self.serializer_class(self.get_queryset(pk), data=request.data)
            if product_serializer.is_valid():
                product_serializer.save()
                return Response(product_serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(product_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def destroy(self, request, pk=None): #borrado logico
        product = self.get_queryset().filter(id=pk).first() #se obtiene el producto del queryset
        if product:
            product.state = False
            product.save()
            return Response({'message:' 'product deleted succesfully'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Does not exist product'}, status=status.HTTP_400_BAD_REQUEST)

# class ProductlistAPIView(GeneralListApiView):
#     serializer_class = ProductSerializer

# class ProductCreateAPIView(generics.CreateAPIView):
#     serializer_class = ProductSerializer

#     def post(self, request): #validacion al crear producto
#         serializer = self.serializer_class(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'message': 'Product created succesfully'}, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class ProductDetailAPIView(generics.RetrieveAPIView):
#     serializer_class = ProductSerializer

#     def get_queryset(self):
#         return self.get_serializer().Meta.model.objects.filter(state=True)
    
# class ProductDeleteAPIView(generics.DestroyAPIView):
#     serializer_class = ProductSerializer

#     def get_queryset(self):
#         return self.get_serializer().Meta.model.objects.filter(state=True)
    
#     # sobrescribiendo metodo delete de la clase, se debe llamar delete
#     def delete(self, request, pk=None): #borrado logico
#         product = self.get_queryset().filter(id=pk).first() #se obtiene el producto del queryset
#         if product:
#             product.state = False
#             product.save()
#             return Response({'message:' 'product deleted succesfully'}, status=status.HTTP_200_OK)
#         else:
#             return Response({'error': 'Does not exist product'}, status=status.HTTP_400_BAD_REQUEST)
        
# class ProductUpdateAPIView(generics.UpdateAPIView):
#     serializer_class = ProductSerializer

#     def get_queryset(self, pk):
#         return self.get_serializer().Meta.model.objects.filter(state=True).filter(id=pk).first()
    
#     def patch(self, request, pk=None):
#         product = self.get_queryset(pk)
#         if product:
#             product_serializer = self.serializer_class(product)
#             print(product_serializer.data)
#             print(product)
#             return Response(product_serializer.data, status=status.HTTP_200_OK)
#         else:
#             return Response({'error': 'product Does not exist '}, status=status.HTTP_400_BAD_REQUEST)
        
#     def put(self, request, pk=None): #validacion al editar producto
#         product = self.get_queryset(pk)
#         if product:
#             product_serializer = self.serializer_class(self.get_queryset(pk), data=request.data)
#             if product_serializer.is_valid():
#                 product_serializer.save()
#                 return Response(product_serializer.data, status=status.HTTP_200_OK)
#             else:
#                 return Response(product_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        
