from mongoframes import *


class Coordinates(SubFrame):
    _fields = {
        'x',
        'y'
    }


class CoverageArea(SubFrame):
    _fields = {
        'type',
        'coordinates'
    }

    _default_projection = {
        'coordinates': {'$sub': Coordinates}
    }


class Address(SubFrame):
    _fields = {
        'type',
        'coordinates'
    }

    _default_projection = {
        'coordinates': {'$sub': Coordinates}
    }


class PDVDocument(Frame):
    import api.constants as constants
    _db = constants.MONGO_DB

    _collection = 'pdvs'

    _fields = {
        'id',
        'tradingName',
        'ownerName',
        'document',
        'address',
        'coverageArea'
    }

    _private_fields = {
        '_id'
    }

    _default_projection = {
        'address': {'$sub': Address},
        'coverageArea': {'$sub': CoverageArea}
    }
