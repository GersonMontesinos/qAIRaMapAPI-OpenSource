import project.main.data.post_data_helper as post_data_helper
import project.main.data.get_data_helper as get_data_helper
import project.main.util_helper as util_helper
import project.main.same_function_helper as same_helper
import project.main.business.get_business_helper as get_business_helper
from flask import jsonify, make_response, request
from project import app, socketio
from datetime import timedelta
import dateutil.parser
import dateutil.tz
import datetime

@app.route('/api/processed_measurements/', methods=['GET'])
def getProcessedData():
    """ Lists all measurements of processed measurement of the target qHAWAX within the initial and final date """
    qhawax_name = request.args.get('name')
    try:
        interval_minutes = int(request.args.get('interval_minutes')) \
            if request.args.get('interval_minutes') is not None else 60
        final_timestamp = datetime.datetime.now(dateutil.tz.tzutc())
        initial_timestamp = final_timestamp - datetime.timedelta(minutes=interval_minutes)
        processed_measurements = get_data_helper.queryDBProcessed(qhawax_name, initial_timestamp, final_timestamp)
        if processed_measurements is not None:
            return make_response(jsonify(processed_measurements), 200)
        return make_response(jsonify('Measurements not found'), 200)
    except TypeError as e:
        json_message = jsonify({'error': '\'%s\'' % (e)})
        return make_response(json_message, 400)

@app.route('/api/dataProcessed/', methods=['POST'])
def handleProcessedData():
    """
    Records processed and valid processed measurements every five seconds
    qHAWAX: Record new measurement
    """
    flag_email = False
    data_json = request.get_json()
    try:
        product_id = data_json['ID']
        data_json = util_helper.validTimeJsonProcessed(data_json)
        data_json = util_helper.validAndBeautyJsonProcessed(data_json)
        post_data_helper.storeProcessedDataInDB(data_json)
        data_json['ID'] = product_id
        data_json['zone'] = "Undefined Zone"
        mode = same_helper.getQhawaxMode(product_id)
        inca_value = same_helper.getMainIncaQhawaxTable(product_id)
        if(mode == "Customer" and inca_value!=None):
            data_json['zone'] = get_business_helper.getNoiseData(product_id)
            minutes_difference,last_time_turn_on = get_business_helper.getHoursDifference(product_id)
            if(minutes_difference!=None):
                if(minutes_difference<5):
                    post_data_helper.validTimeOfValidProcessed(10,"minute",last_time_turn_on,data_json,product_id,inca_value)
                elif(minutes_difference>=5):
                    post_data_helper.validTimeOfValidProcessed(2,"hour",last_time_turn_on,data_json,product_id,inca_value)
        data_json = util_helper.setNoneStringElements(data_json)
        socketio.emit(data_json['ID'] + '_processed', data_json)
        return make_response('OK', 200)
    except TypeError as e:
        json_message = jsonify({'error': '\'%s\'' % (e)})
        return make_response(json_message, 400)


@app.route('/api/processed_measurements_andean_drone/', methods=['GET'])
def getProcessedDataFromAndeanDrone():
    """ Lists all measurements of processed measurement of the target drone within the initial and final date """
    qhawax_name = request.args.get('qhawax_name')
    initial_timestamp = datetime.datetime.strptime(request.args.get('initial_timestamp'), '%d-%m-%Y %H:%M:%S')
    final_timestamp = datetime.datetime.strptime(request.args.get('final_timestamp'), '%d-%m-%Y %H:%M:%S')
    try:
        processed_measurements = get_data_helper.queryDBProcessed(qhawax_name, initial_timestamp, final_timestamp)
        if processed_measurements is not None:
            return make_response(jsonify(processed_measurements), 200)
        return make_response(jsonify('Measurements not found'), 200)
    except TypeError as e:
        json_message = jsonify({'error': '\'%s\'' % (e)})
        return make_response(json_message, 400)
#<<<<<<< HEAD
#    try:
#=======
#    try:
#>>>>>>> 734858d6f1dba7eb81f5229b2cdc517e1a770e16
#        processed_measurements = get_data_helper.queryDBProcessed(qhawax_name, initial_timestamp, final_timestamp)
#        if processed_measurements is not None:
#            return make_response(jsonify(processed_measurements), 200)
#        return make_response(jsonify('Measurements not found'), 200)
#    except TypeError as e:
#        json_message = jsonify({'error': '\'%s\'' % (e)})
#        return make_response(json_message, 400)
#<<<<<<< HEAD
#=======

#>>>>>>> 734858d6f1dba7eb81f5229b2cdc517e1a770e16
