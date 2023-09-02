from connection.conn import Connection


class Mobile:
    def __init__(self):
        self.model = Connection('mobile')

    def get_mobile_all(self, order):
        return self.model.get_all(order)

    def get_mobile(self, id_object):
        return self.model.get_by_id(id_object)

    def get_mobiles_columns(self, id_object):
        return self.model.get_columns(id_object)

    def insert_mobile(self, data):
        return self.model.insert(data)

    def update_mobile(self, id_object, data):
        return self.model.update(id_object, data)

    def delete_mobile(self, id_object):
        return self.model.delete(id_object)

    