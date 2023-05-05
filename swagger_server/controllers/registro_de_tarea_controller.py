import connexion
import six

from swagger_server.models.task_request import TaskRequest  # noqa: E501
from swagger_server.models.task_response import TaskResponse  # noqa: E501
from swagger_server import util

from flask.views import MethodView

class RegisterTaskView(MethodView):
        
    def register_task(self):  # noqa: E501
        """Registro de tarea

        Endpoint para el registro de tareas # noqa: E501

        :param body: 
        :type body: dict | bytes

        :rtype: TaskResponse
        """
        if connexion.request.is_json:
            body = TaskRequest.from_dict(connexion.request.get_json())  # noqa: E501
        return 'do some magic!'
