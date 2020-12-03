import project.main.business.get_business_helper as get_business_helper
from datetime import timedelta
import unittest
import datetime
import pytz

class TestGetBusinessHelper(unittest.TestCase):
	""" Test of Get Business Functions """

	def test_query_qhawax_mode_customer_not_valid(self):
		self.assertRaises(TypeError,get_business_helper.queryQhawaxModeCustomer,{"name":"qH001"})
		self.assertRaises(TypeError,get_business_helper.queryQhawaxModeCustomer,4.33)
		self.assertRaises(TypeError,get_business_helper.queryQhawaxModeCustomer,5)
		self.assertRaises(TypeError,get_business_helper.queryQhawaxModeCustomer,None)
		self.assertRaises(TypeError,get_business_helper.queryQhawaxModeCustomer,True)
		self.assertRaises(TypeError,get_business_helper.queryQhawaxModeCustomer,10,None)
		self.assertRaises(TypeError,get_business_helper.queryQhawaxModeCustomer,"String_")

	def test_query_qhawax_mode_customer_valid(self):
		#y = [('qH002', 'Cliente', 'ON', 'STATIC', 50.0, 268, 2, 1, 'Socket 2', -12.03, -77.03, 'Zona de Protección Especial')]
		y = []
		self.assertAlmostEqual(get_business_helper.queryQhawaxModeCustomer(),y)

	def test_query_get_areas_not_valid(self):
		self.assertRaises(TypeError,get_business_helper.queryGetAreas,{"name":"qH001"})
		self.assertRaises(TypeError,get_business_helper.queryGetAreas,4.33)
		self.assertRaises(TypeError,get_business_helper.queryGetAreas,5)
		self.assertRaises(TypeError,get_business_helper.queryGetAreas,None)
		self.assertRaises(TypeError,get_business_helper.queryGetAreas,True)
		self.assertRaises(TypeError,get_business_helper.queryGetAreas,10,None)
		self.assertRaises(TypeError,get_business_helper.queryGetAreas,"String_")

	def test_query_get_areas_valid(self):
		area_list = [(4, 'Zona Industrial'),(3, 'Zona Comercial'),(2, 'Zona Residencial'), \
					 (1, 'Zona de Protección Especial')]
		self.assertAlmostEqual(get_business_helper.queryGetAreas(),area_list)

	def test_query_get_eca_noise_not_valid(self):
		self.assertRaises(TypeError,get_business_helper.queryGetEcaNoise)
		self.assertRaises(TypeError,get_business_helper.queryGetEcaNoise,{"eca_noise_id":1})
		self.assertRaises(TypeError,get_business_helper.queryGetEcaNoise,True)
		self.assertRaises(TypeError,get_business_helper.queryGetEcaNoise,None)
		self.assertRaises(TypeError,get_business_helper.queryGetEcaNoise,4.33)
		self.assertRaises(TypeError,get_business_helper.queryGetEcaNoise,"PUCP")
		self.assertRaises(TypeError,get_business_helper.queryGetEcaNoise,1, True)

	def test_query_get_eca_noise(self):
		e1 = (1, 'Zona de Protección Especial', 50, 40)
		e2 = (2, 'Zona Residencial', 60, 50)
		self.assertAlmostEqual(get_business_helper.queryGetEcaNoise(1),e1)
		self.assertAlmostEqual(get_business_helper.queryGetEcaNoise(2),e2)
		self.assertAlmostEqual(get_business_helper.queryGetEcaNoise(5),None)

	def test_query_get_offsets_from_productID_not_valid(self):
		self.assertRaises(TypeError,get_business_helper.getConstantsFromProductID)
		self.assertRaises(TypeError,get_business_helper.getConstantsFromProductID,{"name":"qH001"})
		self.assertRaises(TypeError,get_business_helper.getConstantsFromProductID,4.33)
		self.assertRaises(TypeError,get_business_helper.getConstantsFromProductID,None)
		self.assertRaises(TypeError,get_business_helper.getConstantsFromProductID,True)
		self.assertRaises(TypeError,get_business_helper.getConstantsFromProductID,"qH001",1)

	def test_query_get_offsets_from_productID(self):
		qhawax_name= 'qH002'
		offset_sensor ={'CO': {'WE': 337,'WEt': 2.0, 'AE': 356, 'AEt': 1.0, 'algorithm': 1,'sensitivity': 0.45, 'sensitivity_2': 0.0}, 
					   'SO2': {'WE': 346,'WEt': 7.0, 'AE': 360, 'AEt': 1.0, 'algorithm': 1,'sensitivity': 0.37, 'sensitivity_2': 0.0}, 
		               'H2S': {'WE': 350,'WEt': 3.0, 'AE': 346, 'AEt': 1.0, 'algorithm': 1,'sensitivity': 1.724,'sensitivity_2': 0.0}, 
		                'O3': {'WE': 224,'WEt': 6.0, 'AE': 234, 'AEt': 1.0, 'algorithm': 1,'sensitivity': 0.326, 'sensitivity_2': 0.0}, 
		                'NO': {'WE': 300,'WEt': 4.0, 'AE': 300, 'AEt': 1.0, 'algorithm': 1,'sensitivity': 0.3, 'sensitivity_2': 0.0}, 
		               'NO2': {'WE': 228,'WEt': 5.0, 'AE': 235, 'AEt': 1.0, 'algorithm': 1,'sensitivity': 0.234, 'sensitivity_2': 0.0}}
		self.assertAlmostEqual(get_business_helper.getConstantsFromProductID(qhawax_name,'offsets'),offset_sensor)
		self.assertAlmostEqual(get_business_helper.getConstantsFromProductID('qH100','offsets'),None)
		self.assertAlmostEqual(get_business_helper.getConstantsFromProductID('qH021','none'),None)

	def test_query_get_controlled_offsets_from_productID(self):
		qhawax_name= 'qH002'
		offset_sensor ={'CO':  {'C2': 0.0, 'C1': 0.0, 'C0': 0.0}, 
						'SO2': {'C2': 0.0, 'C1': 0.0, 'C0': 0.0}, 
						'H2S': {'C2': 0.0, 'C1': 0.0, 'C0': 0.0}, 
						'O3':  {'C2': 0.0, 'C1': 0.0, 'C0': 0.0}, 
						'NO':  {'C2': 0.0, 'C1': 0.0, 'C0': 0.0}, 
						'NO2': {'C2': 0.0, 'C1': 0.0, 'C0': 0.0}}
		self.assertAlmostEqual(get_business_helper.getConstantsFromProductID(qhawax_name,'controlled-offsets'),offset_sensor)
		self.assertAlmostEqual(get_business_helper.getConstantsFromProductID('qH100','controlled-offsets'),None)

	def test_query_get_non_controlled_offsets_from_productID(self):
		qhawax_name= 'qH002'
		offset_sensor ={'CO': {'NC0': 1.0, 'NC1': 0.0}, 
		               'SO2': {'NC0': 0.0, 'NC1': 0.0}, 
		               'H2S': {'NC0': 0.0, 'NC1': -1.0}, 
		                'O3': {'NC0': 0.0, 'NC1':  1.0}, 
		                'NO': {'NC0': 1.0, 'NC1': -9.0}, 
		               'NO2': {'NC0': 0.0, 'NC1': -1.0}}
		self.assertAlmostEqual(get_business_helper.getConstantsFromProductID(qhawax_name,'non-controlled-offsets'),offset_sensor)
		self.assertAlmostEqual(get_business_helper.getConstantsFromProductID('qH100','non-controlled-offsets'),None)

	def test_query_inca_qhawax_not_valid(self):
		self.assertRaises(TypeError,get_business_helper.queryIncaQhawax)
		self.assertRaises(TypeError,get_business_helper.queryIncaQhawax,{"name":"qH001"})
		self.assertRaises(TypeError,get_business_helper.queryIncaQhawax,4)
		self.assertRaises(TypeError,get_business_helper.queryIncaQhawax,None)
		self.assertRaises(TypeError,get_business_helper.queryIncaQhawax,True)
		self.assertRaises(TypeError,get_business_helper.queryIncaQhawax,"qH001",1)

	def test_query_inca_qhawax_valid(self):
		self.assertAlmostEqual(get_business_helper.queryIncaQhawax('qH001'),'green')
		self.assertAlmostEqual(get_business_helper.queryIncaQhawax('qH100'),None)

	def test_get_installation_date_not_valid(self):
		self.assertRaises(TypeError,get_business_helper.getInstallationDate)
		self.assertRaises(TypeError,get_business_helper.getInstallationDate,True)
		self.assertRaises(TypeError,get_business_helper.getInstallationDate,4.5)
		self.assertRaises(TypeError,get_business_helper.getInstallationDate,None)
		self.assertRaises(TypeError,get_business_helper.getInstallationDate,"342")

	def test_get_installation_date_valid(self):
		naive_time = datetime.time(17,36,53)
		date = datetime.date(2020, 11, 11)
		naive_datetime = datetime.datetime.combine(date, naive_time)
		timezone = pytz.timezone('UTC')
		aware_datetime = timezone.localize(naive_datetime)
		self.assertAlmostEqual(get_business_helper.getInstallationDate(1),None)
		self.assertAlmostEqual(get_business_helper.getInstallationDate(2),aware_datetime)

	def test_get_first_time_valid_processed_not_valid(self):
		self.assertRaises(TypeError,get_business_helper.getFirstTimestampValidProcessed)
		self.assertRaises(TypeError,get_business_helper.getFirstTimestampValidProcessed,True)
		self.assertRaises(TypeError,get_business_helper.getFirstTimestampValidProcessed,4.5)
		self.assertRaises(TypeError,get_business_helper.getFirstTimestampValidProcessed,None)
		self.assertRaises(TypeError,get_business_helper.getFirstTimestampValidProcessed,"342")

	def test_get_first_time_valid_processed_valid(self):
		naive_time = datetime.time(19,37,6)
		date = datetime.date(2020, 11, 11)
		naive_datetime = datetime.datetime.combine(date, naive_time)
		timezone = pytz.timezone('UTC')
		aware_datetime = timezone.localize(naive_datetime)
		self.assertAlmostEqual(get_business_helper.getFirstTimestampValidProcessed(1),None)
		self.assertAlmostEqual(get_business_helper.getFirstTimestampValidProcessed(2),aware_datetime)

	def test_get_last_qhawax_id_not_valid(self):
		self.assertRaises(TypeError,get_business_helper.queryGetLastQhawax,40)
		self.assertRaises(TypeError,get_business_helper.queryGetLastQhawax,True)
		self.assertRaises(TypeError,get_business_helper.queryGetLastQhawax,4.5)
		self.assertRaises(TypeError,get_business_helper.queryGetLastQhawax,None)
		self.assertRaises(TypeError,get_business_helper.queryGetLastQhawax,"342")

	#def test_get_last_qhawax_id_valid(self):
	#	self.assertAlmostEqual(get_business_helper.queryGetLastQhawax()[0],37)

	def test_get_last_gas_sensor_id_not_valid(self):
		self.assertRaises(TypeError,get_business_helper.queryGetLastGasSensor,40)
		self.assertRaises(TypeError,get_business_helper.queryGetLastGasSensor,True)
		self.assertRaises(TypeError,get_business_helper.queryGetLastGasSensor,4.5)
		self.assertRaises(TypeError,get_business_helper.queryGetLastGasSensor,None)
		self.assertRaises(TypeError,get_business_helper.queryGetLastGasSensor,"342")

	#def test_get_last_gas_sensor_id(self):
	#	self.assertAlmostEqual(get_business_helper.queryGetLastGasSensor()[0],204)

	def test_qhawax_in_field_valid(self):
		self.assertAlmostEqual(get_business_helper.isItFieldQhawax("qH030"),False)
		self.assertAlmostEqual(get_business_helper.isItFieldQhawax("qH004"),True)

	def test_qhawax_in_field_not_valid(self):
		self.assertRaises(TypeError,get_business_helper.isItFieldQhawax)
		self.assertRaises(TypeError,get_business_helper.isItFieldQhawax,40)
		self.assertRaises(TypeError,get_business_helper.isItFieldQhawax,True)
		self.assertRaises(TypeError,get_business_helper.isItFieldQhawax,4.5)
		self.assertRaises(TypeError,get_business_helper.isItFieldQhawax,None)
		self.assertRaises(TypeError,get_business_helper.isItFieldQhawax,{"name":"qH001"})

	def test_get_qhawax_latest_timestamp_processed_not_valid(self):
		self.assertRaises(TypeError,get_business_helper.getLatestTimeInProcessedMeasurement)
		self.assertRaises(TypeError,get_business_helper.getLatestTimeInProcessedMeasurement,40)
		self.assertRaises(TypeError,get_business_helper.getLatestTimeInProcessedMeasurement,True)
		self.assertRaises(TypeError,get_business_helper.getLatestTimeInProcessedMeasurement,4.5)
		self.assertRaises(TypeError,get_business_helper.getLatestTimeInProcessedMeasurement,None)
		self.assertRaises(TypeError,get_business_helper.getLatestTimeInProcessedMeasurement,{"name":"qH001"})

	def test_get_qhawax_latest_timestamp_processed_valid(self):
		self.assertAlmostEqual(get_business_helper.getLatestTimeInProcessedMeasurement('qH100'),None)

	def test_get_qhawax_in_field_public_mode_not_valid(self):
		self.assertRaises(TypeError,get_business_helper.queryQhawaxInFieldInPublicMode,40)
		self.assertRaises(TypeError,get_business_helper.queryQhawaxInFieldInPublicMode,True)
		self.assertRaises(TypeError,get_business_helper.queryQhawaxInFieldInPublicMode,4.5)
		self.assertRaises(TypeError,get_business_helper.queryQhawaxInFieldInPublicMode,None)
		self.assertRaises(TypeError,get_business_helper.queryQhawaxInFieldInPublicMode,{"name":"qH001"})
		self.assertRaises(TypeError,get_business_helper.queryQhawaxInFieldInPublicMode,{"name":"qH001"},1)

	def test_get_qhawax_in_field_public_mode_valid(self):
		y = [('qH002', 'Cliente', 'OFF', 'STATIC', -1.0, 303, 2, 1, 'Calibrador dev', -12.043, -77.028, 'Zona de Protección Especial'), 
			 ('qH004', 'Calibracion', 'OFF', 'STATIC', -1.0, 304, 4, 1, 'qHAWAX 04 en dev', -12.0444, -77.028888, 'Zona de Protección Especial'), 
			 ('qH021', 'Cliente', 'OFF', 'STATIC', -1.0, 305, 21, 1, 'UNICEF TEST', -12.04333333, -77.0281111, 'Zona de Protección Especial')]

		self.assertAlmostEqual(get_business_helper.queryQhawaxInFieldInPublicMode(),y)

	def test_get_qhawax_status_not_valid(self):
		self.assertRaises(TypeError,get_business_helper.getQhawaxStatus)
		self.assertRaises(TypeError,get_business_helper.getQhawaxStatus,40)
		self.assertRaises(TypeError,get_business_helper.getQhawaxStatus,True)
		self.assertRaises(TypeError,get_business_helper.getQhawaxStatus,4.5)
		self.assertRaises(TypeError,get_business_helper.getQhawaxStatus,None)
		self.assertRaises(TypeError,get_business_helper.getQhawaxStatus,{"name":"qH001"})
		self.assertRaises(TypeError,get_business_helper.getQhawaxStatus,{"name":"qH001"},1)

	def test_get_qhawax_status_valid(self):
		self.assertAlmostEqual(get_business_helper.getQhawaxStatus('qH001'),'OFF')
		self.assertAlmostEqual(get_business_helper.getQhawaxStatus('qH004'),'OFF')
		self.assertAlmostEqual(get_business_helper.getQhawaxStatus('qH100'),None)

	def test_query_noise_data_not_valid(self):
		self.assertRaises(TypeError,get_business_helper.getNoiseData)
		self.assertRaises(TypeError,get_business_helper.getNoiseData,{"qhawax_id":5})
		self.assertRaises(TypeError,get_business_helper.getNoiseData,True)
		self.assertRaises(TypeError,get_business_helper.getNoiseData,-5.0)
		self.assertRaises(TypeError,get_business_helper.getNoiseData,None)
		self.assertRaises(TypeError,get_business_helper.getNoiseData,"qH001",1,2)

	def test_query_noise_data_valid(self):
		self.assertAlmostEqual(get_business_helper.getNoiseData("qH004"),"Zona de Protección Especial")
		self.assertAlmostEqual(get_business_helper.getNoiseData("qH100"),None)

	def test_get_hours_difference_not_valid(self):
		self.assertRaises(TypeError,get_business_helper.getHoursDifference)
		self.assertRaises(TypeError,get_business_helper.getHoursDifference,{"qhawax_id":5})
		self.assertRaises(TypeError,get_business_helper.getHoursDifference,True)
		self.assertRaises(TypeError,get_business_helper.getHoursDifference,-5.0)
		self.assertRaises(TypeError,get_business_helper.getHoursDifference,None)
		self.assertRaises(TypeError,get_business_helper.getHoursDifference,"qH001",1,2)

	def test_get_hours_difference_valid(self):
		self.assertAlmostEqual(get_business_helper.getHoursDifference(100),(None,None))
		self.assertAlmostEqual(get_business_helper.getHoursDifference(9),(None,None))

if __name__ == '__main__':
    unittest.main(verbosity=2)
