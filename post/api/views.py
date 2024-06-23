from rest_framework.viewsets import ModelViewSet
from post.models import Post
from post.api.serializers import PostSerializer
from rest_framework.parsers import MultiPartParser, FormParser

class PostApiViewSet(ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    parser_classes = (MultiPartParser,FormParser,)