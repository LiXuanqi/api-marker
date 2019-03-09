from .context import apimaker


@apimaker.annotations.api(method='get', path='/courses', desc='api to get all courses')
@apimaker.annotations.params({
    'param1': 'number, required',
    'param2': 'string, required'
})
@apimaker.annotations.body({
    'body1': 'number, required',
    'body2': 'string, required'
})
@apimaker.annotations.response({
    'response1': 'number',
    'response2': 'string'
})
def getCourses():
    print('return all courses')

getCourses()
