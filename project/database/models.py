from project import db

from passlib.hash import bcrypt
from sqlalchemy_json import NestedMutableJson

class Company(db.Model):
    __tablename__ = 'company'

    # Column's definition
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(300), nullable=False, unique=True)
    email_group = db.Column(db.String(300), nullable=False, unique=True)
    ruc = db.Column(db.String(11), nullable=False, unique=True)
    address = db.Column(db.String(300), nullable=False, unique=True)
    phone = db.Column(db.String(15), nullable=False, unique=True)
    contact_person = db.Column(db.String(100), nullable=False, unique=True)
    users = db.relationship('User', backref='company', lazy='subquery',
                            cascade='delete, delete-orphan')
    installations = db.relationship('QhawaxInstallationHistory', backref='company', lazy='subquery',
                             cascade='delete, delete-orphan')

    def __init__(self, name, email_group,ruc,address,phone, contact_person):
        utils.checkValidEmailGroup(email_group)
        self.name = name
        self.email_group = email_group
        self.ruc = ruc
        self.address = address
        self.phone = phone
        self.contact_person = contact_person

    @property
    def serialize(self):
        return {'name': self.name, 'email_group': self.email_group,'ruc':self.ruc,'address':self.address,'phone':self.phone,'contact_person':self.contact_person}


class Qhawax(db.Model):
    __tablename__ = 'qhawax'

    # Column's definition
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(300), nullable=False, unique=True)
    main_aqi = db.Column(db.Float)
    main_inca = db.Column(db.Float)
    qhawax_type = db.Column(db.String(100), nullable=False, unique=True)
    state = db.Column(db.String(5), nullable=False, unique=True)
    availability = db.Column(db.String(100), nullable=False, unique=True)
    mode = db.Column(db.String(100), nullable=False, unique=True)
    processed_measurements = db.relationship('ProcessedMeasurement', backref='qhawax', lazy='subquery',
                                                cascade='delete, delete-orphan')
    air_quality_measurements = db.relationship('AirQualityMeasurement', backref='qhawax', lazy='subquery',
                                                cascade='delete, delete-orphan')
    gas_sensors = db.relationship('GasSensor', backref='qhawax', lazy='subquery') # Don't delete gas sensor if qhawax is deleted
    
    gas_inca = db.relationship('GasInca', backref='qhawax', lazy='subquery',
                                                cascade='delete, delete-orphan')
    qhawax_installation_historys = db.relationship('QhawaxInstallationHistory', backref='qhawax', lazy='subquery',
                                                cascade='delete, delete-orphan')

    firmware_updates = db.relationship('FirmwareUpdate', backref='qhawax', lazy='subquery',
                                                cascade='delete, delete-orphan')
    air_daily_measurements = db.relationship('AirDailyMeasurement', backref='qhawax', lazy='subquery',
                                                cascade='delete, delete-orphan')
    bitacoras = db.relationship('Bitacora', backref='qhawax', lazy='subquery',
                                                cascade='delete, delete-orphan')

    def __init__(self,id, name, qhawax_type,state, availability,main_inca,main_aqi,mode):
        self.id = id
        self.name = name
        self.qhawax_type = qhawax_type
        self.state = state
        self.availability = availability
        self.main_inca= main_inca
        self.main_aqi = main_aqi
        self.mode = mode

    @property
    def serialize(self):
        return {
            'name'          : self.name,
            'main_aqi'      : self.main_aqi,
            'main_inca'     : self.main_inca,
            'qhawax_type'   : self.qhawax_type,
            'state'         : self.state,
            'availability'  : self.availability,
            'mode'          : self.mode}

class GasSensor(db.Model):
    __tablename__ = 'gas_sensor'

    # Column's definition
    id = db.Column(db.Integer, primary_key=True)
    serial_number = db.Column(db.String(100), nullable=False, unique=True)
    purchase_date = db.Column(db.DateTime)
    type = db.Column(db.String(100))
    WE = db.Column(db.Float)
    AE = db.Column(db.Float)
    sensitivity = db.Column(db.Float)
    sensitivity_2 = db.Column(db.Float)
    C2 = db.Column(db.Float, nullable=False, default=0, server_default='0')
    C1 = db.Column(db.Float, nullable=False, default=1, server_default='1')
    C0 = db.Column(db.Float, nullable=False, default=0, server_default='0')
    NC1 = db.Column(db.Float, nullable=False, default=1, server_default='1')
    NC0 = db.Column(db.Float, nullable=False, default=0, server_default='0')
    qhawax_id = db.Column(db.Integer, db.ForeignKey('qhawax.id'))

    @property
    def serialize(self):
        return {
            'serial_number': self.serial_number,
            'purchase_date': str(self.timestamp),
            'type': self.type,
            'WE': self.WE,
            'AE': self.AE,
            'sensitivity': self.sensitivity,
            'sensitivity_2': self.sensitivit_2
        }

class ProcessedMeasurement(db.Model):
    __tablename__ = 'processed_measurement'

    # Column's definition
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, nullable=False)
    CO = db.Column(db.Float)
    CO_ug_m3 = db.Column(db.Float)
    CO2 = db.Column(db.Float)
    H2S = db.Column(db.Float)
    H2S_ug_m3 = db.Column(db.Float)
    NO = db.Column(db.Float)
    NO2 = db.Column(db.Float)
    NO2_ug_m3 = db.Column(db.Float)
    O3 = db.Column(db.Float)
    O3_ug_m3 = db.Column(db.Float)
    PM1 = db.Column(db.Float)
    PM25 = db.Column(db.Float)
    PM10 = db.Column(db.Float)
    SO2 = db.Column(db.Float)
    SO2_ug_m3 = db.Column(db.Float)
    VOC = db.Column(db.Float)
    UV = db.Column(db.Float)
    UVA = db.Column(db.Float)
    UVB = db.Column(db.Float)
    spl = db.Column(db.Float)
    humidity = db.Column(db.Float)
    pressure = db.Column(db.Float)
    temperature = db.Column(db.Float)
    lat = db.Column(db.Float)
    lon = db.Column(db.Float)
    alt = db.Column(db.Float)
    qhawax_id = db.Column(db.Integer, db.ForeignKey('qhawax.id'))

    @property
    def serialize(self):
        return {
            'timestamp': str(self.timestamp),
            'CO': self.CO,
            'CO2': self.CO2,
            'H2S': self.H2S,
            'NO': self.NO,
            'NO2': self.NO2,
            'O3': self.O3,
            'PM1': self.PM1,
            'PM25': self.PM25,
            'PM10': self.PM10,
            'SO2': self.SO2,
            'VOC': self.VOC,
            'UV': self.UV,
            'UVA': self.UVA,
            'UVB': self.UVB,
            'spl': self.spl,
            'humidity': self.humidity,
            'pressure': self.pressure,
            'temperature': self.temperature,
            'lat': self.lat,
            'lon': self.lon,
            'alt': self.alt}

class GasInca(db.Model):
    __tablename__ = 'gas_inca'

    # Column's definition
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, nullable=False)
    CO = db.Column(db.Float)
    CO2 = db.Column(db.Float)
    H2S = db.Column(db.Float)
    NO = db.Column(db.Float)
    NO2 = db.Column(db.Float)
    O3 = db.Column(db.Float)
    PM1 = db.Column(db.Float)
    PM25 = db.Column(db.Float)
    PM10 = db.Column(db.Float)
    SO2 = db.Column(db.Float)
    qhawax_id = db.Column(db.Integer, db.ForeignKey('qhawax.id'))
    main_inca = db.Column(db.Float)


class AirQualityMeasurement(db.Model):
    __tablename__ = 'air_quality_measurement'

    # Column's definition
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, nullable=False)
    CO = db.Column(db.Float)
    CO_ug_m3 = db.Column(db.Float)
    H2S = db.Column(db.Float)
    H2S_ug_m3 = db.Column(db.Float)
    NO2 = db.Column(db.Float)
    NO2_ug_m3 = db.Column(db.Float)
    O3 = db.Column(db.Float)
    O3_ug_m3 = db.Column(db.Float)
    PM25 = db.Column(db.Float)
    PM10 = db.Column(db.Float)
    SO2 = db.Column(db.Float)
    SO2_ug_m3 = db.Column(db.Float)
    uv = db.Column(db.Float)
    uva = db.Column(db.Float)
    uvb = db.Column(db.Float)
    spl = db.Column(db.Float)
    humidity = db.Column(db.Float)
    pressure = db.Column(db.Float)
    temperature = db.Column(db.Float)
    lat = db.Column(db.Float)
    lon = db.Column(db.Float)
    alt = db.Column(db.Float)
    qhawax_id = db.Column(db.Integer, db.ForeignKey('qhawax.id'))
    


class EcaNoise(db.Model):
    __tablename__ = 'eca_noise'

    # Column's definition
    id = db.Column(db.Integer, primary_key=True)
    area_name = db.Column(db.String(100))
    max_daytime_limit = db.Column(db.Integer)
    max_night_limit = db.Column(db.Integer)
    installations = db.relationship('QhawaxInstallationHistory', backref='eca_noise', lazy='subquery',
                             cascade='delete, delete-orphan') 

class QhawaxInstallationHistory(db.Model):
    __tablename__ = 'qhawax_installation_history'

    # Column's definition
    id = db.Column(db.Integer, primary_key=True)
    lat = db.Column(db.Float)
    lon = db.Column(db.Float)
    instalation_date = db.Column(db.DateTime, nullable=False)
    end_date = db.Column(db.DateTime, nullable=False)
    link_report = db.Column(db.String(500), nullable=False, unique=True)
    observations = db.Column(db.String(300), nullable=False, unique=True)
    qhawax_id = db.Column(db.Integer, db.ForeignKey('qhawax.id'))
    district = db.Column(db.String(300), nullable=False, unique=True)
    comercial_name = db.Column(db.String(300), nullable=False, unique=True)
    address = db.Column(db.String(300), nullable=False, unique=True)
    company_id = db.Column(db.Integer, db.ForeignKey('company.id'))
    eca_noise_id = db.Column(db.Integer, db.ForeignKey('eca_noise.id'))
    connection_type = db.Column(db.String(300), nullable=False, unique=True)
    index_type = db.Column(db.String(100), nullable=False, unique=True)
    measuring_height = db.Column(db.Integer)
    season = db.Column(db.String(300), nullable=False, unique=True)
    last_maintenance_date = db.Column(db.DateTime, nullable=False)
    last_cleaning_area_date = db.Column(db.DateTime, nullable=False)
    last_cleaning_equipment_date = db.Column(db.DateTime, nullable=False)
    last_time_physically_turn_on = db.Column(db.DateTime, nullable=False)
    person_in_charge = db.Column(db.String(300), nullable=False, unique=True)
    is_public  = db.Column(db.String(10), nullable=False, unique=True)
    last_registration_time = db.Column(db.DateTime, nullable=False)
    main_inca = db.Column(db.Float) 
    valid_processed_measurements = db.relationship('ValidProcessedMeasurement', backref='qhawax_installation_history', lazy='subquery',
                                                cascade='delete, delete-orphan')


class QhawaxCleaningArea(db.Model):
    __tablename__ = 'qhawax_cleaning_area'

    # Column's definition
    id = db.Column(db.Integer, primary_key=True)
    installation_id = db.Column(db.Integer, db.ForeignKey('installation.id'))
    cleaning_area_date = db.Column(db.DateTime, nullable=False)
    comments = db.Column(db.String(500), nullable=False, unique=True)


class QhawaxCleaningEquipment(db.Model):
    __tablename__ = 'qhawax_cleaning_equipment'

    # Column's definition
    id = db.Column(db.Integer, primary_key=True)
    installation_id = db.Column(db.Integer, db.ForeignKey('installation.id'))
    cleaning_equipment_date = db.Column(db.DateTime, nullable=False)
    comments = db.Column(db.String(500), nullable=False, unique=True)

class QhawaxMaintenance(db.Model):
    __tablename__ = 'qhawax_maintenance'

    # Column's definition
    id = db.Column(db.Integer, primary_key=True)
    installation_id = db.Column(db.Integer, db.ForeignKey('installation.id'))
    maintenance_date = db.Column(db.DateTime, nullable=False)
    comments = db.Column(db.String(500), nullable=False, unique=True)

class ValidProcessedMeasurement(db.Model):
    __tablename__ = 'valid_processed_measurement'

    # Column's definition
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, nullable=False)
    CO = db.Column(db.Float)
    CO_ug_m3 = db.Column(db.Float)
    CO2 = db.Column(db.Float)
    H2S = db.Column(db.Float)
    H2S_ug_m3 = db.Column(db.Float)
    NO = db.Column(db.Float)
    NO2 = db.Column(db.Float)
    NO2_ug_m3 = db.Column(db.Float)
    O3 = db.Column(db.Float)
    O3_ug_m3 = db.Column(db.Float)
    PM1 = db.Column(db.Float)
    PM25 = db.Column(db.Float)
    PM10 = db.Column(db.Float)
    SO2 = db.Column(db.Float)
    SO2_ug_m3 = db.Column(db.Float)
    VOC = db.Column(db.Float)
    UV = db.Column(db.Float)
    UVA = db.Column(db.Float)
    UVB = db.Column(db.Float)
    SPL = db.Column(db.Float)
    humidity = db.Column(db.Float)
    pressure = db.Column(db.Float)
    temperature = db.Column(db.Float)
    lat = db.Column(db.Float)
    lon = db.Column(db.Float)
    alt = db.Column(db.Float)
    qhawax_installation_id = db.Column(db.Integer, db.ForeignKey('qhawax_installation_history.id'))


class FirmwareUpdate(db.Model):
    __tablename__ = 'firmware_update'

    # Column's definition
    id = db.Column(db.Integer, primary_key=True)
    qhawax_id = db.Column(db.Integer, db.ForeignKey('qhawax.id'))
    date_of_update = db.Column(db.DateTime, nullable=False)
    url_of_bif_file = db.Column(db.String(1000), nullable=False, unique=True)
    number_of_frames = db.Column(db.Integer)
    frames = db.relationship('Frame', backref='firmware_update', lazy='subquery',
                                                cascade='delete, delete-orphan')

class Frame(db.Model):
    __tablename__ = 'frame'

    # Column's definition
    id = db.Column(db.Integer, primary_key=True)
    firmware_update_id = db.Column(db.Integer, db.ForeignKey('firmware_update.id'))
    numbering_by_frame = db.Column(db.Integer)
    frame_lenght = db.Column(db.Integer)
    address = db.Column(db.String(100), nullable=False, unique=True)
    data_lenght = db.Column(db.Integer)
    data = db.Column(db.String(1000), nullable=False, unique=True)
    crc1 = db.Column(db.Integer)
    crc2 = db.Column(db.Integer)
    crc3 = db.Column(db.Integer)
    crc4 = db.Column(db.Integer)

class AirDailyMeasurement(db.Model):
    __tablename__ = 'air_daily_measurement'

    # Column's definition
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, nullable=False)
    CO = db.Column(db.Float)
    CO_ug_m3 = db.Column(db.Float)
    H2S = db.Column(db.Float)
    H2S_ug_m3 = db.Column(db.Float)
    NO2 = db.Column(db.Float)
    NO2_ug_m3 = db.Column(db.Float)
    O3 = db.Column(db.Float)
    O3_ug_m3 = db.Column(db.Float)
    PM25 = db.Column(db.Float)
    PM10 = db.Column(db.Float)
    SO2 = db.Column(db.Float)
    SO2_ug_m3 = db.Column(db.Float)
    humidity = db.Column(db.Float)
    pressure = db.Column(db.Float)
    temperature = db.Column(db.Float)
    qhawax_id = db.Column(db.Integer, db.ForeignKey('qhawax.id'))

class Bitacora(db.Model):
    __tablename__ = 'bitacora'

    # Column's definition
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, nullable=False)
    observation_type = db.Column(db.String(100))
    description = db.Column(db.String(100))
    solution = db.Column(db.String(100))
    person_in_charge = db.Column(db.String(100))
    end_date = db.Column(db.DateTime, nullable=False)
    qhawax_id = db.Column(db.Integer, db.ForeignKey('qhawax.id'))
    


import project.database.utils as utils