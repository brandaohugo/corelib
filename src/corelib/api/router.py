from functools import wraps
from typing import Any, Optional

from fastapi import APIRouter, Query
from fastapi.responses import JSONResponse
from corelib.db import CRUDManager
from corelib.db import SessionDep



def make_health_check_router():
    router = APIRouter(prefix="/utils", tags=["utils"])

    @router.get("/health-check/")
    async def health_check() -> bool:
        return True

    return router

def standard_json_response(
    data: Optional[Any] = None,
    success: bool = True,
    error: Optional[str] = None,
    status_code: int = 200
) -> JSONResponse:
    resp = {
        "success": success,
        "data": data if success else None,
        "error": error if not success else None
    }
    return JSONResponse(content=resp, status_code=status_code)

def safe_json_response(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            return standard_json_response(data=result)
        except Exception as exc:
            return standard_json_response(success=False, error=str(exc), status_code=500)
    return wrapper


def make_crud_router(
    *,
    router_prefix: str,
    tags: list[str] = [],
    Model: type = None,
    ModelsPublic: type = None,
    ModelPublic: type = None,
    ModelInListPublic: type = None,
    ModelCreate: type = None,
    ModelUpdate: type = None,
    ModelDelete: type = None,
    get_all_response_field: str = "data",
    get_all_count_field: str = "count",
    id_field: str = "id"
) -> APIRouter:
    router = APIRouter(prefix=router_prefix, tags=tags)

    if ModelsPublic and ModelInListPublic:
        @router.get("/", response_model=ModelsPublic)
        @safe_json_response
        def read_all(
            session: SessionDep,
            skip: int = Query(0, ge=0, description="How many items to skip"),
            limit: int = Query(100, ge=1, le=1000, description="Maximum number of items to return"),
        ) -> Any:
            objs = CRUDManager(Model, session).get_all(skip=skip, limit=limit)
            return ModelsPublic(**{
                get_all_response_field: [ModelInListPublic.model_validate(obj) for obj in objs],
                get_all_count_field: len(objs)
            })

    if ModelPublic:
        @router.get("/{id}", response_model=ModelPublic)
        @safe_json_response
        def read_one(id: str, session: SessionDep) -> Any:
            obj = CRUDManager(Model, session).get_or_404(id)
            return ModelPublic.model_validate(obj)

    if ModelPublic and ModelCreate:
        @router.post("/", response_model=ModelPublic)
        @safe_json_response
        def create(obj_in: ModelCreate, session: SessionDep) -> Any:
            obj = CRUDManager(Model, session).create(obj_in)
            return ModelPublic.model_validate(obj)

    if ModelPublic and ModelUpdate:
        @router.put("/{id}", response_model=ModelPublic)
        @safe_json_response
        def update(id: str, obj_in: ModelUpdate, session: SessionDep) -> Any:
            manager = CRUDManager(Model, session)
            old_obj = manager.get_or_404(id)
            obj_in_dict = obj_in.model_dump(exclude_unset=True)
            for k, v in obj_in_dict.items():
                setattr(old_obj, k, v)
            session.add(old_obj)
            session.commit()
            session.refresh(old_obj)
            return ModelPublic.model_validate(old_obj)

    if ModelDelete:
        @router.delete("/{id}", response_model=ModelDelete)
        @safe_json_response
        def delete(id: str, session: SessionDep):
            manager = CRUDManager(Model, session)
            obj = manager.delete(session, id)
            return ModelDelete.model_validate(obj)

    return router