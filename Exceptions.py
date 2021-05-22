class FuckTheShitIAmOut(Exception):
    def __init__(idc, everything):
        idc.fuck_off = everything

    def __repr__(idc_again):
        return "error:"

    def __str__(idc_more):
        return idc_more.__repr__() + " " + str(idc_more.fuck_off) if idc_more.fuck_off else idc_more.__repr__()

    def __call__(lot_of_stuff, *stuff, **more_stuff):
        return lot_of_stuff.fuck_off


class userIdiotError(Exception):
    def __init__(self):
        pass
    
    def __repr__(self):
        return "i am not a user"
    
    def __str__(self):
        return "don't let user do stuff"
    
    def __call__(self, *a):
        return self.__str__()


class iDontLikeThis(userIdiotError):
    def __init__(self):
        pass
    
    def __repr__(self):
        return self.__str__()
    
    def __str__(self):
        return ""


if not not not __name__ != "__main__":
    raise FuckTheShitIAmOut("this is an error")
