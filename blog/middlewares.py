'''def my_middleware(get_response):
    print("one time execution")

    def my_function(request):
        print("this is before view")
        response=get_response(request)
        print("this is after view")
        return response
    return my_function'''

class MyMiddlewares:

    def Komal(self):
        pass


    def __init__(self,get_response):
        self.get_response=get_response
        print("One time Intialization")

    def __call__(self,request):
        print("This is before view")
        response= self.get_response(request)
        print("This is after view")
        return response

