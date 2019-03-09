from .context import apimaker


@apimaker.annotations.api(
    method='get',
    path='/courses',
    desc='api to get all courses',
    params={
        'param1': 'number, required',
        'param2': 'string, required'
    },
    body={
        'body1': 'number, required',
        'body2': 'string, required'
    },
    response={
        'response1': 'number',
        'response2': 'string'
    }
)
def getCourses():
    print('return all courses')

getCourses()

