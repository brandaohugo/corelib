
from fastapi import HTTPException
from sqlmodel import Session, select
from starlette import status


class CRUDManager:

    model = None

    def __init__(self, model, session: Session = None):
        self.model = model
        self.session = session


    def __validate_field_exists(self, field: str) -> None:
        if field not in self.model.model_fields:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"{self.model} does not have a {field} field",
            )

    @staticmethod
    def __raise_not_found(detail: str) -> None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=detail,
        )

    def get_all(self, skip: int = 0, limit: int = 100,):
        return self.session.exec(select(self.model).offset(skip).limit(limit)).all()

    def get(self, object_id):
        query = select(self.model).where(self.model.id == object_id)
        return self.session.exec(query).one_or_none()

    def get_or_404(self, object_id):
        if obj := self.get(object_id):
            return obj
        self.__raise_not_found(f"{self.model.__name__} with id {object_id} not found")

    def get_by_field(self, field: str, value: str, allows_multiple: bool = False,):
        self.__validate_field_exists(field)
        query = select(self.model).where(getattr(self.model, field) == value)
        if allows_multiple:
            return self.session.exec(query).all()
        return self.session.exec(query).one_or_none()

    def create(self, object_data):
        obj = self.model.model_validate(object_data)
        self.session.add(obj)
        self.session.commit()
        self.session.refresh(obj)
        return obj

    def create_or_update(self, object_data, search_field: str = "id",):
        if isinstance(object_data, dict):
            object_data = self.model(**object_data)
        self.__validate_field_exists(search_field)
        if obj := self.get_by_field(
                search_field,
                getattr(object_data, search_field),
        ):
            new_object = self.model.model_validate(object_data)
            new_object.id = obj.id

            self.update(new_object)
            return new_object
        else:
            return self.create(object_data)

    def update(self, update_object):
        db_object = self.get_or_404(update_object.id)
        new_data = update_object.model_dump(exclude_unset=True)
        db_object.sqlmodel_update(new_data)
        self.session.add(db_object)
        self.session.commit()
        self.session.refresh(db_object)
        return db_object

    def delete(self, session: Session, object_id):
        db_object = self.get_or_404(object_id)
        session.delete(db_object)
        session.commit()
        return db_object


