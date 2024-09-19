from app import db


class GenericBase(db.Model):
    __abstract__ = True

    created_at = db.Column(
        db.DateTime,
        nullable=False,
        server_default=db.func.now()
    )
    updated_at = db.Column(
        db.DateTime,
        server_default=db.func.now(),
        server_onupdate=db.func.now()
    )

    @classmethod
    def get_columns(cls):
        list_columns = cls.__table__.columns.keys()
        list_columns.remove('id')
        return list_columns

    @classmethod
    def first(cls, **kwargs):
        return cls.query.filter_by(**kwargs).first()

    @classmethod
    def all(cls):
        """"Get All"""
        return cls.query.all()

    @classmethod
    def exists(cls, **kwargs) -> bool:
        return True if cls.query.filter_by(**kwargs).first() else False

    @classmethod
    def get_id(cls, **kwargs) -> int or None:
        obj = cls.query.filter_by(**kwargs).first()
        if obj:
            return obj.id
        return None

    @classmethod
    def get_by_id(cls, id: int):
        """"Get by id"""
        return cls.query.filter_by(id=id).first()

    def insert(self):
        """Insert data from MixinBase on database"""
        db.session.add(self)
        return self

    @classmethod
    def update(cls, update, **kwargs):
        """Update data on database from MixinBase"""
        return cls.query.filter_by(**kwargs).update(update)

    @classmethod
    def delete(cls, **kwargs):
        """Delete object MixinBase on database"""
        return cls.__commit(cls.query.filter_by(**kwargs).delete())

    @staticmethod
    def __commit(result: bool = False) -> bool:
        """"Commit data on database"""
        if result:
            db.session.commit()
            return True
        return False

    def to_dict(self):
        dict_model = self.__dict__
        dict_model.pop("_sa_instance_state")
        return dict_model


class MixinBase(GenericBase):
    __abstract__ = True
    id = db.Column(
        db.Integer,
        primary_key=True
    )


class MixinNotAutoIncrement(GenericBase):
    __abstract__ = True

    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=False
    )
