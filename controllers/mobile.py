from models.mobile import Mobile


class MobileController:
    def __init__(self):
        self.mobile = Mobile()

    def list_mobiles(self):
        mobiles = self.mobile.get_mobile_all('id')
        print(mobiles)

    def list_mobile(self):
        id = int(input('Ingrese el ID a buscar : '))
        mobile_one = self.mobile.get_mobile({'id': id})
        print(mobile_one)

    def list_mobile_columns(self):
        mobiles = self.mobile.get_mobiles_columns({
            'id': 9,
            'model': 'ZTE'
        })
        print(mobiles)

    def insert_mobile(self, data):
        self.mobile.insert_mobile(data)
        print('Se creo con exito')
        return True

    def update_mobile(self, id_object, data):
        self.mobile.update_mobile(id_object, data)
        print('Se actualizo con exito')
        return True

    def delete_mobile(self, id_object):
        self.mobile.delete_mobile(id_object)
        print('Se elimino con exito')
        return True

    



