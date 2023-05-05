import connexion
import six

from swagger_server.models.user_request import UserRequest  # noqa: E501
from swagger_server.models.user_response import UserResponse  # noqa: E501
from swagger_server import util

from flask.views import MethodView

class RegisterUserView(MethodView):
    def register_user(body=None):  # noqa: E501
        """Registro de usuario

        Endpoint para el registro de usuarios # noqa: E501

        :param body: 
        :type body: dict | bytes

        :rtype: UserResponse
        """
        if connexion.request.is_json:
            body = UserRequest.from_dict(connexion.request.get_json())  # noqa: E501
        return 'do some magic!'
