from rest_framework.views import APIView
from rest_framework.response import Response

from vrc import vrc_client


class VRCView(APIView):
    def get(self, request):
        q = request.query_params.get('q')
        users = vrc_client.search_users(q)

        return Response(users)






