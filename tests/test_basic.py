from .context import apimaker


@apimaker.annotations.api(method='get', path='/courses', desc='api to get all courses')
def getCourses():
    print('return all courses')

getCourses()