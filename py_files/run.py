from QatarAirways.qatarAirways import QatarAirways

qatar = QatarAirways()
qatar.land_first_page()
qatar.enterOrigin('new york')
qatar.enterDestination('kathmandu')
qatar.enterTripType()
qatar.departDate('2023-09-20')
qatar.showFlights()
qatar.getResult()
qatar.JSONify()
input('Herau ')