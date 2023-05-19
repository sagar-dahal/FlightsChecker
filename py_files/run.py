from QatarAirways.qatarAirways import QatarAirways
import argparse

def getFromQatar(origin, destination, date):
    qatar = QatarAirways()
    qatar.land_first_page()
    qatar.enterOrigin(origin)
    qatar.enterDestination(destination)
    qatar.enterTripType()
    qatar.departDate(date)
    qatar.showFlights()
    return qatar.getResult()

parser = argparse.ArgumentParser(description='Get flight info for a particular date')
parser.add_argument('origin', type=str, help='Put the departure location or airport')
parser.add_argument('destination', type=str, help='Put the arrival location or airport')
parser.add_argument('date', type=str, help='Put the departure date in the format yyyy-mm-dd')
args = parser.parse_args()

print(getFromQatar(args.origin, args.destination, args.date))