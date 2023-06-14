from rest_framework import serializers
from product.models import Category, Product, Review, Tag
from rest_framework.exceptions import ValidationError


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    product_count = ProductSerializer

    class Meta:
        model = Category
        fields = 'id name product_count'.split()
        # fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = 'id text stars product_id'.split()
        # fields = '__all__'


class ProductsReviewsSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True)

    class Meta:
        model = Product
        fields = 'title reviews rating'.split()


class ProductValidateSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=150)
    description = serializers.CharField(required=False, default="No description")
    price = serializers.FloatField()
    category_id = serializers.IntegerField()
    tag = serializers.ListField(child=serializers.IntegerField(min_value=1))

    def validate_category_id(self, category_id):
        try:
            Category.objects.get(id=category_id)
        except Category.DoesNotExist:
            raise ValidationError('Category not found!')
        return category_id

    def validate_tag(self, tag):
        tags_db = Tag.objects.filter(id__in=tag)
        if len(tags_db) != len(tag):
            raise ValidationError('Tag not found')
        return tag


class CategoryValidateSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=150, min_length=1)


class ReviewValidateSerializer(serializers.Serializer):
    text = serializers.CharField(max_length=500)
    stars = serializers.IntegerField(required=False, min_value=1, max_value=5)
    product_id = serializers.IntegerField()

    def validate_product_id(self, product_id):
        try:
            Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            raise ValidationError(f'Director with id ({product_id}) not found')
        return product_id
