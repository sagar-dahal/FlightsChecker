from QatarAirways.qatarAirways import QatarAirways

def getFromQatar():
    qatar = QatarAirways()
    qatar.land_first_page()
    qatar.enterOrigin('new york')
    qatar.enterDestination('kathmandu')
    qatar.enterTripType()
    qatar.departDate('2023-08-05')
    qatar.showFlights()
    return qatar.getResult()

print(getFromQatar())