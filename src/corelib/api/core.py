from typing import List, TypeVar, Generic

from fastapi import APIRouter
from pydantic.generics import GenericModel
from sqlalchemy.ext.indexable import index_property
from sqlmodel import SQLModel

ModelData = TypeVar('ModelData', bound=SQLModel)


from fastapi import HTTPException

from types import MethodType, FunctionType


def list_methods_change(cls):
    return [func for func in dir(cls)
            if callable(getattr(cls, func))
            and not func.startswith("__")
            and func in ["create_object", "update_object"]]

def api(model, response_model=None, **kwargs):
    def wrapper(api_cls):
        api_cls.model = model
        api_cls.response_model = response_model if response_model else model
        for method in list_methods_change(api_cls):
            fn = getattr(api_cls, method)
            new_fn = FunctionType(
                    fn.__code__,
                    fn.__globals__,
                )
            new_fn.__annotations__ = {"data": kwargs.get(method.replace("_object", ""), model)}
            bound_method = MethodType(new_fn, api_cls)
            setattr(api_cls, method, bound_method)
        return api_cls
    return wrapper



def raise_as_http_exception(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            if e.__class__.__name__ == "HTTPException":
                raise e
            else:
                raise HTTPException(status_code=500, detail=str(e)) from e
    return wrapper


class ObjectCreate(SQLModel):
    pass


class ObjectUpdate(SQLModel):
    id: int


class ObjectDelete(SQLModel):
    id: int
    message: str = "Object deleted successfully"


class ApiResponse(GenericModel, Generic[ModelData]):
    data: ModelData = None




class BaseAPI:
    model = None
    response_model = None

    @classmethod
    def get_router(cls):
        print("GET ROUTER")
        api_router = APIRouter()
        api_router.get("/", response_model=ApiResponse[List[cls.response_model]])(cls.read_objects)
        api_router.get("/{id}", response_model=ApiResponse[cls.response_model])(cls.read_object)
        api_router.post("/", response_model=ApiResponse[cls.response_model])(cls.create_object)
        api_router.patch("/", response_model=ApiResponse[cls.response_model])(cls.update_object)
        api_router.delete("/{id}", response_model=ApiResponse[cls.response_model])(cls.delete_object)
        return api_router


    @classmethod
    async def read_objects(cls):
        return {"data": cls.model.manager.get_all()}

    @classmethod
    async def read_object(cls, object_id: int):
        return {"data": cls.model.manager.get_or_404(object_id)}

    @classmethod
    async def create_object(cls, data: ModelData):
        return {"data": cls.model.manager.create(data)}

    @classmethod
    async def delete_object(cls, object_id: int):
        return {"data" : cls.model.manager.delete(object_id)}

    @classmethod
    async def update_object(cls, data: ModelData):
        return  {"data" : cls.model.manager.update(data)}
