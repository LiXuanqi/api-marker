from .context import apimaker


@apimaker.annotations.api(
    method='get',
    path='/courses',
    desc='api to get all courses',
    params={
        'param1': 'number, required, body',
        'param2': 'string, required, header',
        'param3': 'string, required, form',
        'param5': 'string, required, query'
    },
    responses={
        'response1': 'number',
        'response2': 'string'
    }
)
def getCourses():
    print('return all courses')

getCourses()
print(apimaker.core.ApiSpec.basePath)
