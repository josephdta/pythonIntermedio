# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.task_request import TaskRequest  # noqa: E501
from swagger_server.models.task_response import TaskResponse  # noqa: E501
from swagger_server.test import BaseTestCase


class TestRegistroDeTareaController(BaseTestCase):
    """RegistroDeTareaController integration test stubs"""

    def test_register_task(self):
        """Test case for register_task

        Registro de tarea
        """
        body = TaskRequest()
        response = self.client.open(
            '/josephdta/TASK/1.0.1/register_task',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
