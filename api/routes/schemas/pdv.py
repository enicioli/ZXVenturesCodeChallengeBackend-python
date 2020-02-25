from api.routes.schemas._abstract import AbstractSchema


class PDVSchema(AbstractSchema):
    schema = {
        "$schema": "http://json-schema.org/draft-04/schema#",
        "properties": {
            "id": {
                "type": "number"
            },
            "address": {
                "properties": {
                    "coordinates": {
                        "items": {
                            "type": "number"
                        },
                        "maxItems": 2,
                        "minItems": 2,
                        "type": "array"
                    },
                    "type": {
                        "enum": [
                            "Point"
                        ],
                        "type": "string"
                    }
                },
                "required": [
                    "coordinates",
                    "type"
                ],
                "type": "object"
            },
            "coverageArea": {
                "properties": {
                    "coordinates": {
                        "items": {
                            "items": {
                                "items": {
                                    "items": {
                                        "type": "number"
                                    },
                                    "maxItems": 2,
                                    "minItems": 2,
                                    "type": "array"
                                },
                                "minItems": 4,
                                "type": "array"
                            },
                            "minItems": 1,
                            "type": "array"
                        },
                        "minItems": 1,
                        "type": "array"
                    },
                    "type": {
                        "enum": [
                            "MultiPolygon"
                        ],
                        "type": "string"
                    }
                },
                "required": [
                    "coordinates",
                    "type"
                ],
                "type": "object"
            },
            "document": {
                "type": "string"
            },
            "ownerName": {
                "maxLength": 255,
                "minLength": 1,
                "type": "string"
            },
            "tradingName": {
                "maxLength": 255,
                "minLength": 1,
                "type": "string"
            }
        },
        "required": [
            "id",
            "tradingName",
            "ownerName",
            "document",
            "coverageArea",
            "address"
        ],
        "type": "object"
    }


class PDVSchemaUpdate(PDVSchema):

    def get_schema(self):
        schema = self.schema
        if 'required' in schema:
            schema.pop('required')

        return schema
