from typing import Any

from fastapi import APIRouter

from corelib.db import CRUDManager
from corelib.db import SessionDep



def make_health_check_router():
    router = APIRouter(prefix="/utils", tags=["utils"])

    @router.get("/health-check/")
    async def health_check() -> bool:
        return True


def make_crud_router(
    *,
    router_prefix: str,
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
    router = APIRouter(prefix=router_prefix)

    if ModelsPublic and ModelInListPublic:
        @router.get("/", response_model=ModelsPublic)
        def read_all(session: SessionDep) -> Any:
            objs = CRUDManager(Model, session).get_all()
            return ModelsPublic(**{
                get_all_response_field: [ModelInListPublic.model_validate(obj) for obj in objs],
                get_all_count_field: len(objs)
            })

    if ModelPublic:
        @router.get("/{id}", response_model=ModelPublic)
        def read_one(id: str, session: SessionDep) -> Any:
            obj = CRUDManager(Model, session).get_or_404(id)
            return ModelPublic.model_validate(obj)

    if ModelPublic and ModelCreate:
        @router.post("/", response_model=ModelPublic)
        def create(obj_in: ModelCreate, session: SessionDep) -> Any:
            obj = CRUDManager(Model, session).create(obj_in)
            return ModelPublic.model_validate(obj)

    if ModelPublic and ModelUpdate:
        @router.put("/{id}", response_model=ModelPublic)
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
        def delete(id: str, session: SessionDep):
            manager = CRUDManager(Model, session)
            obj = manager.delete(session, id)
            return ModelDelete.model_validate(obj)

    return router