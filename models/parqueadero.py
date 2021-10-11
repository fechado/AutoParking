from app import database, TipoVehiculo

class Parqueadero(database.Model):
    __tablename__ = 'parqueaderos'
    
    id_p = database.Column(database.Integer, primary_key=True)
    capacidad = database.Column(database.Integer, nullable=False)
    id_tv = database.Column(database.Integer, database.ForeignKey('tipo_vehiculo.id_tv'))
    
    def __init__(self, capacidad, id_tv):
        self.capacidad = capacidad
        self.id_tv = id_tv
    
    def create(self):
        database.session.add(self)
        database.session.commit()

    def __str__(self):
        return f"<Parqueadero: {self.id_p} {self.capacidad} {self.id_tv}>"
    
    @staticmethod
    def get_all():
        return Parqueadero.query.all()
    
    @staticmethod
    def get_full():
        return database.session.query(Parqueadero, TipoVehiculo).join(TipoVehiculo).all()
    
    @staticmethod
    def get_by_tv(tv):
        return Parqueadero.query.filter_by(id_tv = tv).first()
    
    @staticmethod
    def update_parqueaderos(tv, capacidad):
        pre_park = Parqueadero.get_by_tv(tv)
        pre_park.capacidad = capacidad
        database.session.commit()