class ApiSpec:
    basePath = '/v2'
    paths=[]

class Path:
    url = '/pet'
    methods={
        'get': '',
        'post': '',
        'delete': '',
        'put': ''
    }

class Action:
    description = ''
    functionName = ''
    parameters = []
    responses = []

class Parameter:
    location = ''
    name = ''
    description = ''
    required = True
    type = ''
    items = [] # - for type = array.

class Response:
    statusCode = 200
    description = ''
