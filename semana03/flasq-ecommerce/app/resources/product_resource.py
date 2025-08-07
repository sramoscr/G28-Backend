from flask_restful import Resource, request
from pydantic import ValidationError
from app.schemas.product_schema import CreateProductSchema, UpdateProductSchema
import cloudinary
import cloudinary.uploader
import cloudinary.utils
import os
import uuid
from app.models.product_model import ProductModel
from app.models.update_product_log_model import UpdateProductLogModel
from db import db
from dotenv import load_dotenv
from flask_jwt_extended import jwt_required, get_jwt_identity

load_dotenv()

cloudinary.config(
    clod_name=os.getenv('CLOUDINARY_CLOUD_NAME'),
    api_key=os.getenv('CLOUDINARY_API_KEY'),
    api_secret=os.getenv('CLOUDINARY_API_SECRET'),
    secure=True
)

class ProductResource(Resource):
    @jwt_required()
    def get(self):
        try:
            page = request.args.get('page', 1, type=int)
            per_page = request.args.get('per_page', 10, type=int)

            products = ProductModel.query.filter_by(
                status=True
            ).paginate(
                page=page,
                per_page=per_page,
                error_out=False
            )

            response = []
            for product in products.items:
                response.append({
                    'id': product.id,
                    'name': product.name,
                    'code': product.code,
                    'description': product.description,
                    'image': cloudinary.utils.cloudinary_url(
                        product.image,
                        width=300,
                        crop='scale',
                        format='webp'
                    )[0],
                    'brand': product.brand,
                    'size': product.size,
                    'price': product.price,
                    'stock': product.stock,
                    'status': product.status,
                    'category_id': product.category_id
                })

            return response, 200
            # return {
            #     'data': response,
            #     'pagination': {
            #         'page': products.page,
            #         'per_page': products.per_page,
            #         'total': products.total,
            #         'pages': products.pages
            #     }
            # }, 200
        except Exception as e:
            return {
                'error': str(e)
            }, 500
    
    @jwt_required()
    def post(self):
        try:
            validated_data = CreateProductSchema(
                name=request.form.get('name'),
                description=request.form.get('description'),
                brand=request.form.get('brand'),
                size=request.form.get('size'),
                price=request.form.get('price'),
                stock=request.form.get('stock'),
                category_id=request.form.get('category_id')
            )

            image = request.files.get('image')
            if not image:
                raise Exception('Imagen no encontrada')
            
            if image.filename == '':
                raise Exception('Imagen no encontrada')
            
            if not image.content_type.startswith('image/'):
                raise Exception('El archivo debe ser una imagen')
            
            public_id = f'{uuid.uuid4()}-{image.filename}'
            cloudinary.uploader.upload(
                file=image.stream,
                public_id=public_id,
            )

            last_product = ProductModel.query.order_by(
                ProductModel.id.desc()
            ).first()

            product_code = 'P-0001'
            if last_product:
                last_code = last_product.code
                last_number = int(last_code.split('-')[1])
                new_number = last_number + 1
                # product_code = f'P-{new_number:04d}'
                product_code = f'P-{str(new_number).zfill(4)}'

            product = ProductModel(
                name=validated_data.name,
                code=product_code,
                description=validated_data.description,
                image=public_id,
                brand=validated_data.brand,
                size=validated_data.size,
                price=validated_data.price,
                stock=validated_data.stock,
                category_id=validated_data.category_id
            )
            db.session.add(product)
            db.session.commit()

            return {
                'message': 'Producto creado correctamente',
            }, 200
        except ValidationError as e:
            return {
                'error': e.errors()
            }, 400
        except Exception as e:
            return {
                'error': str(e)
            }, 500
        
class ProductByIdResource(Resource):
    @jwt_required()
    def put(self, product_id):
        try:
            product = ProductModel.query.get(product_id)
            if not product:
                raise Exception('Producto no encontrado')

            data = request.form
            validated_data = UpdateProductSchema(**data)

            image = request.files.get('image')
            if image is not None:
                if image.filename == '':
                    raise Exception('Imagen no encontrada')
                
                if not image.content_type.startswith('image/'):
                    raise Exception ('El archivo debe ser una imagen')
                
                public_id = f'{uuid.uuid4()}-{image.filename}'
                cloudinary.uploader.upload(
                    file=image.stream,
                    public_id=public_id,
                )
                cloudinary.uploader.destroy(product.image)
                product.image = public_id

            if validated_data.name is not None:
                product.name = validated_data.name
            if validated_data.description is not None:
                product.description = validated_data.description
            if validated_data.brand is not None:
                product.brand = validated_data.brand
            if validated_data.size is not None:
                product.size = validated_data.size
            if validated_data.price is not None:
                product.price = validated_data.price
            if validated_data.stock is not None:
                product.stock = validated_data.stock
            if validated_data.category_id is not None:
                product.category_id = validated_data.category_id

            current_user = get_jwt_identity()

            upls = []
            for _data in validated_data:
                upl = UpdateProductLogModel(
                    field = _data[0],
                    value=str(_data[1]),
                    user_id=int(current_user),
                    product_id=product_id
                )
                upls.append(upl)

            db.session.add_all(upls)
            db.session.commit()

            return {
                'message': 'Producto actualizado correctamente'
            }
        except ValidationError as e:
            return {
                'error': e.errors()
            }, 400
        except Exception as e:
            db.session.rollback()
            return {
                'error': str(e)
            }, 500
    
    @jwt_required()
    def delete(self, product_id):
        try:
            product = ProductModel.query.get(product_id)
            if not product:
                raise Exception('Producto no encontrado')
            
            product.status = False
            db.session.commit()

            return {
                'mensaje': 'Producto eliminadp correctamente'
            }, 200

        except Exception as e:
            return { 
                'error': str(e)
            }, 500
