import enum

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
    # properties for object.

class Response:
    statusCode = 200
    description = ''

class Type(enum.Enum):
    string = 1
    number = 2
    integer = 3
    boolean = 4
    array = 5
    object = 6

