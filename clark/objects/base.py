class BaseObject(object):
    # base for all objects, common code will end up here
    uuid = None

    @classmethod
    def from_db(cls, db_obj):
        return cls(db_obj)
