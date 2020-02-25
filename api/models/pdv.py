from api.odm.pdv import PDVDocument


class PDVModel:
    @staticmethod
    def create_pdv(data: dict):
        pdv_entity = PDVDocument(data)
        pdv_entity.insert()
        return pdv_entity

    @staticmethod
    def update_pdv(pdv_entity: PDVDocument, data: dict):
        for key, value in data.items():
            pdv_entity.__setattr__(key, value)

        pdv_entity.update()
        return pdv_entity

    @staticmethod
    def get_pdv_by_id(pdv_id: int):
        return PDVDocument.one({'id': int(pdv_id)})

    @staticmethod
    def delete_pdv(pdv_entity: PDVDocument):
        return pdv_entity.delete()

    @staticmethod
    def get_pdv_by_position(lng: float, lat: float, comparison='$geoIntersects'):
        return PDVDocument.one({
                'coverageArea': {
                    comparison: {
                        '$geometry': {
                            'type': "Point",
                            'coordinates': [lng, lat]
                        }
                    }
                }
            }
        )
