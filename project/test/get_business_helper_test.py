import project.main.business.get_business_helper as get_business_helper
from datetime import timedelta
import unittest
import datetime
import pytz

class TestGetBusinessHelper(unittest.TestCase):
	""" Test of Get Business Functions """

	def test_query_all_qhawax_not_valid(self):
		self.assertRaises(TypeError,get_business_helper.queryAllQhawax,{"name":"qH001"})
		self.assertRaises(TypeError,get_business_helper.queryAllQhawax,4.33)
		self.assertRaises(TypeError,get_business_helper.queryAllQhawax,5)
		self.assertRaises(TypeError,get_business_helper.queryAllQhawax,None)
		self.assertRaises(TypeError,get_business_helper.queryAllQhawax,True)
		self.assertRaises(TypeError,get_business_helper.queryAllQhawax,10,None)
		self.assertRaises(TypeError,get_business_helper.queryAllQhawax,"String_")

	def test_query_all_qhawax_valid(self):
		y = [{'name': 'qH004', 'mode': 'Cliente', 'state': 'OFF', 'qhawax_type': 'STATIC', 'main_inca': -1.0, 'id': 1}, 
			 {'name': 'qH057', 'mode': 'Stand By', 'state': 'OFF', 'qhawax_type': 'STATIC', 'main_inca': -1.0, 'id': 2}]
		self.assertAlmostEqual(get_business_helper.queryAllQhawax(),y)

	def test_query_qhawax_mode_customer_not_valid(self):
		self.assertRaises(TypeError,get_business_helper.queryQhawaxModeCustomer,{"name":"qH001"})
		self.assertRaises(TypeError,get_business_helper.queryQhawaxModeCustomer,4.33)
		self.assertRaises(TypeError,get_business_helper.queryQhawaxModeCustomer,5)
		self.assertRaises(TypeError,get_business_helper.queryQhawaxModeCustomer,None)
		self.assertRaises(TypeError,get_business_helper.queryQhawaxModeCustomer,True)
		self.assertRaises(TypeError,get_business_helper.queryQhawaxModeCustomer,10,None)
		self.assertRaises(TypeError,get_business_helper.queryQhawaxModeCustomer,"String_")

	def test_query_qhawax_mode_customer_valid(self):
		#y = [{'name': 'qH004', 'mode': 'Cliente', 'state': 'ON', 'qhawax_type': 'STATIC', 'main_inca': 50.0, 'id': 4, \
		#	  'qhawax_id': 1, 'eca_noise_id': 2, 'comercial_name': 'FaberCastell', 'lat': -12.0, 'lon': -77.0, \
		#	  'area_name': 'Residential Zone'}]
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
		area_list = [(4, 'Industry Zone'),(3, 'Comercial Zone'),(2, 'Residential Zone'), \
					 (1, 'Special Protection Zone')]
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
		e1 = (1, 'Special Protection Zone', 50, 40)
		e2 = (2, 'Residential Zone', 60, 50)
		self.assertAlmostEqual(get_business_helper.queryGetEcaNoise(1),e1)
		self.assertAlmostEqual(get_business_helper.queryGetEcaNoise(2),e2)
		self.assertAlmostEqual(get_business_helper.queryGetEcaNoise(5),None)

	def test_get_installation_date_not_valid(self):
		self.assertRaises(TypeError,get_business_helper.getInstallationDate)
		self.assertRaises(TypeError,get_business_helper.getInstallationDate,True)
		self.assertRaises(TypeError,get_business_helper.getInstallationDate,4.5)
		self.assertRaises(TypeError,get_business_helper.getInstallationDate,None)
		self.assertRaises(TypeError,get_business_helper.getInstallationDate,"342")

	#def test_get_installation_date_valid(self):
	#	naive_time = datetime.time(17,36,53)
	#	date = datetime.date(2020, 11, 11)
	#	naive_datetime = datetime.datetime.combine(date, naive_time)
	#	timezone = pytz.timezone('UTC')
	#	aware_datetime = timezone.localize(naive_datetime)
	#	self.assertAlmostEqual(get_business_helper.getInstallationDate(2),None)
		#self.assertAlmostEqual(get_business_helper.getInstallationDate(1),aware_datetime)

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

	def test_get_qhawax_in_field_public_mode_not_valid(self):
		self.assertRaises(TypeError,get_business_helper.queryQhawaxInFieldInPublicMode,40)
		self.assertRaises(TypeError,get_business_helper.queryQhawaxInFieldInPublicMode,True)
		self.assertRaises(TypeError,get_business_helper.queryQhawaxInFieldInPublicMode,4.5)
		self.assertRaises(TypeError,get_business_helper.queryQhawaxInFieldInPublicMode,None)
		self.assertRaises(TypeError,get_business_helper.queryQhawaxInFieldInPublicMode,{"name":"qH001"})
		self.assertRaises(TypeError,get_business_helper.queryQhawaxInFieldInPublicMode,{"name":"qH001"},1)

	def test_get_qhawax_in_field_public_mode_valid(self):
		z = [{'name': 'qH004', 'mode': 'Cliente', 'state': 'OFF', 'qhawax_type': 'STATIC', 
			'main_inca': -1.0, 'id': 4, 'qhawax_id': 1, 'eca_noise_id': 2, 'comercial_name': 'FaberCastell', 
			'lat': -12.0, 'lon': -77.0, 'area_name': 'Residential Zone'}]
		self.assertAlmostEqual(get_business_helper.queryQhawaxInFieldInPublicMode(),z)

	def test_query_noise_data_not_valid(self):
		self.assertRaises(TypeError,get_business_helper.getNoiseData)
		self.assertRaises(TypeError,get_business_helper.getNoiseData,{"qhawax_id":5})
		self.assertRaises(TypeError,get_business_helper.getNoiseData,True)
		self.assertRaises(TypeError,get_business_helper.getNoiseData,-5.0)
		self.assertRaises(TypeError,get_business_helper.getNoiseData,None)
		self.assertRaises(TypeError,get_business_helper.getNoiseData,"qH001",1,2)

	#def test_query_noise_data_valid(self): hay un error
	#	self.assertAlmostEqual(get_business_helper.getNoiseData("qH004"),"Residential Zone")
	#	self.assertAlmostEqual(get_business_helper.getNoiseData("qH100"),None)

	def test_get_hours_difference_not_valid(self):
		self.assertRaises(TypeError,get_business_helper.getHoursDifference)
		self.assertRaises(TypeError,get_business_helper.getHoursDifference,{"qhawax_id":5})
		self.assertRaises(TypeError,get_business_helper.getHoursDifference,True)
		self.assertRaises(TypeError,get_business_helper.getHoursDifference,-5.0)
		self.assertRaises(TypeError,get_business_helper.getHoursDifference,None)
		self.assertRaises(TypeError,get_business_helper.getHoursDifference,1,2)

	#def test_get_hours_difference_valid(self):
	#	naive_time = datetime.time(15,1,12)
	#	date = datetime.date(2020, 6, 30)
	#	naive_datetime = datetime.datetime.combine(date, naive_time)
	#	timezone = pytz.timezone('UTC')
	#	aware_datetime = timezone.localize(naive_datetime)
	#	self.assertAlmostEqual(get_business_helper.getHoursDifference(100),(None,None))
	#	self.assertAlmostEqual(get_business_helper.getHoursDifference(9),(None,None))
	#	print(get_business_helper.getHoursDifference(21))
		#self.assertAlmostEqual(get_business_helper.getHoursDifference(21),(0,aware_datetime))

	def test_get_last_value_of_qhawax_not_valid(self):
		self.assertRaises(TypeError,get_business_helper.getLastValuesOfQhawax)
		self.assertRaises(TypeError,get_business_helper.getLastValuesOfQhawax,21)
		self.assertRaises(TypeError,get_business_helper.getLastValuesOfQhawax,None)

	#def test_set_last_value_of_qhawax_valid(self):
	#	self.assertAlmostEqual(get_business_helper.getLastValuesOfQhawax('qH001'),("Stand By","Se cambió a modo stand by",-1))
		#self.assertAlmostEqual(get_business_helper.getLastValuesOfQhawax('qH021'),("Cliente","Se cambió a modo cliente",0))

if __name__ == '__main__':
    unittest.main(verbosity=2)
