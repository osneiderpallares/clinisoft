userfrm:dict()=[]
tokenfrm:str=''

def asign_value_user(username:str, password:str):
    user = dict(
      username=username, 
      password=password
      )
    return user