from pydantic import BaseModel,Field,EmailStr
from typing import Optional

class Student(BaseModel):
    name:str='bharti'
    age:Optional[int]=None
    email:EmailStr
    cgpa:float=Field(gt=0,lt=10,default=9,description='a decimal value represent marks of student')

new_student={'age':32,'email':'bharti@gmail.com'}
student=Student(**new_student)

print(student)