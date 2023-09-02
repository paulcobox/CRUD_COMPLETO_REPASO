from controllers.mobile import MobileController

mobile = MobileController()

# Listar todos los registros
#mobile.list_mobiles()

# Listar por condición
#mobile.list_mobile()

# Listar por condiciones
#mobile.list_mobile_columns()

# Insertar
#mobile.insert_mobile({
#    "model": "M60",
#    "price": 560
#})

# Update
#mobile.update_mobile({
#    "id": 16,
#    "model": "M70"
#}, {
#    "model": "M80",
#    "price": 6000
#})

# Delete
mobile.delete_mobile({
    "id": 17
})
