from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, permissions
from .serializers import accountbookSerializer
from .models import accountbook
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.contrib.auth.decorators import login_required
# Create your views here.

class accountView(APIView):
        permission_classes = [permissions.IsAuthenticated]
        authentication_classes = [JWTAuthentication]

        def get(self, request):
            Accountbook = accountbook.objects.order_by('-created_at') #최신순으로 정렬
            accountbook_data = accountbookSerializer(Accountbook, many=True).data
            return Response({'accountbook_data': accountbook_data}, status=status.HTTP_200_OK)
        def post(self, request):
            data = request.data.copy()
            data["user"] = request.user.id
            accountbook_serializer = accountbookSerializer(data=data)
            if accountbook_serializer.is_valid():
                # validator를 통과했을 경우 데이터 저장
                accountbook_serializer.save()

                return Response({"message": "정상"}, status=status.HTTP_200_OK)

            return Response(accountbook_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        def put(self, request, obj_id):
        
            Accountbook = accountbook.objects.get(id=obj_id)
            # user = User.objects.get(id=accountbook.user.id)
            if request.user.id == Accountbook.user.id:
                accountbook_serializer = accountbookSerializer(
                    Accountbook, data=request.data, partial=True)
                if accountbook_serializer.is_valid():
                    # validator를 통과했을 경우 데이터 저장
                    accountbook_serializer.save()
                    return Response({"message": "정상"}, status=status.HTTP_200_OK)
            return Response(accountbook_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


        def delete(self,request, obj_id):
            my_accountbook = accountbook.objects.get(id=obj_id)
            if request.user.id == my_accountbook.user.id:
                my_accountbook.delete()
                return Response({"message": "삭제 완료!"})
            return Response({"message":"권한이 없습니다"},status=status.HTTP_400_BAD_REQUEST)


class DetailView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get(self,request,obj_id):
        accountbook_get =accountbook.objects.get(id=obj_id)
        serialized_data =accountbookSerializer(accountbook_get).data
        serialized_data['boolean'] = request.user in accountbook_get.like.all()
        return Response(serialized_data,status=status.HTTP_200_OK)



class AccountCopyInstance(APIView):
    serializer_class = accountbookSerializer

    def get_object(self, obj_id):
        try:
            return accountbook.objects.get(id=obj_id)
        except accountbook.DoestNotExist:
            raise Response({"message":"권한이 없습니다"},status=status.HTTP_404_BAD_REQUEST)

    def get(self, request, obj_id, format=None):
        response = self.get_object(id=obj_id)
        serializer = accountbookSerializer(response)
        return Response(serializer.data)

    def post(self, request, obj_id, format=None, **kwargs):
        """
        복사하여 새로운 객체를 만들어주기 때문에 POST 메서드로 사용하기 도전
        그럼 instance=request.data 와 같이 어떤 객체인지를 먼저 알게 해줘야 할 듯
        """
        # 현재 해당하는 객체의 obj_id 가 무엇인지까지 확인
        # kwargs 는 해당하는 딕셔너리에서 key 값만을 불러옴
        # POST 메서드에서 data 를 불러오면 새로 입력한 값들이 들어오기 때문에 .data 는 피해야 함
        # original_data = self.kwargs.get('obj_id', '')
        # 생성하려는 객체를 만들기 위해 우선 accountbook 모델에서 불러오기(아직 직렬화 상태 아님)
        product = accountbook.objects.get(id=obj_id)
        product.obj_id = None
        # 직렬화 상태(serializer) 로 만듦
        # 이 클래스에서 get 메서드를 통해 들어온 request.data 를 data 로 받아 직렬화
        # 매직메서드 __dict__ 의 사용방법은 느낌적으로 옳지 않은 것 같지만 일단은 구현을 위해 사용
        serializer = accountbookSerializer(product, data=product.__dict__)
        additional_data = serializer
        if additional_data.is_valid():

            additional_data.save()
            return Response(additional_data.data, status=status.HTTP_201_CREATED)
        return Response(additional_data.errors, status=status.HTTP_400_BAD_REQUEST)