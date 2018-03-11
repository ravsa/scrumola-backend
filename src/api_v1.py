from flask import Blueprint, request, Response
from flask.json import jsonify
from flask_restful import Api, Resource
from flask_cors import CORS
from .exceptions import HTTPError

app_v1 = Blueprint('api_v1', __name__, url_prefix='/api/v1')
rest_api = Api(app_v1)
CORS(app_v1)
_resource_paths = list()


def add_resource_no_matter_slashes(resource, route,
                                   endpoint=None, defaults=None):
    slashless = route.rstrip('/')
    _resource_paths.append(app_v1.url_prefix + slashless)
    slashful = route + '/'
    endpoint = endpoint or resource.__name__.lower()
    defaults = defaults or {}

    rest_api.add_resource(resource,
                          slashless,
                          endpoint=endpoint + '__slashless',
                          defaults=defaults)
    rest_api.add_resource(resource,
                          slashful,
                          endpoint=endpoint + '__slashful',
                          defaults=defaults)


class ApiEndpoints(Resource):
    def get(self):
        return {'paths': sorted(_resource_paths)}


add_resource_no_matter_slashes(ApiEndpoints, '')
