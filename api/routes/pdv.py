from flask import Blueprint, request, jsonify
from api.routes.schemas.pdv import PDVSchema, PDVSchemaUpdate
from api.models.pdv import PDVModel
from pymongo.errors import PyMongoError

pdv = Blueprint('pdv', __name__, url_prefix='/pdv')


@pdv.route('/covers', methods=['GET'])
def route_get_pdv_by_position():
    lng = float(request.args.get('lng'))
    lat = float(request.args.get('lat'))
    pdv_entity = PDVModel.get_pdv_by_position(lng, lat)

    if pdv_entity is None:
        pdv_entity = PDVModel.get_pdv_by_position(lng, lat, '$near')

    if pdv_entity is None:
        return jsonify({'message': 'Not found'}), 404

    return jsonify(pdv_entity.to_json_type())


@pdv.route('', methods=['POST'])
def route_create_pdv():
    json_data = request.get_json(force=True)
    result, message = PDVSchema.validate(json_data)

    if result is False:
        return jsonify({'message': message}), 400

    try:
        pdv_entity = PDVModel.create_pdv(json_data)
    except PyMongoError as e:
        return jsonify({'message': str(e)}), 400

    return jsonify(pdv_entity.to_json_type()), 201


@pdv.route('/<pdv_id>', methods=['PUT', 'PATCH'])
def route_update_pdv(pdv_id: int):
    pdv_entity = PDVModel.get_pdv_by_id(pdv_id)

    if pdv_entity is None:
        return jsonify({'message': 'Not found'}), 404

    json_data = request.get_json(force=True)

    if request.method == 'PATCH':
        result, message = PDVSchemaUpdate.validate(json_data)
    else:
        result, message = PDVSchema.validate(json_data)

    if result is False:
        return jsonify({'message': message}), 400

    pdv_entity = PDVModel.update_pdv(pdv_entity, json_data)
    return jsonify(pdv_entity.to_json_type())


@pdv.route('/<pdv_id>', methods=['GET'])
def route_get_pdv(pdv_id: int):
    pdv_entity = PDVModel.get_pdv_by_id(pdv_id)

    if pdv_entity is None:
        return jsonify({'message': 'Not found'}), 404

    return jsonify(pdv_entity.to_json_type())


@pdv.route('/<pdv_id>', methods=['DELETE'])
def route_delete_pdv(pdv_id: int):
    pdv_entity = PDVModel.get_pdv_by_id(pdv_id)

    if pdv_entity is None:
        return jsonify({'message': 'Not found'}), 404

    PDVModel.delete_pdv(pdv_entity)
    return jsonify({'message': 'OK'})
