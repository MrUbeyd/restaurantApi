import sqlite3
from operator import itemgetter

#this import for distance function
import geopy.distance

#DATABESE CREATE AND FILL PROCESS
# con = sqlite3.connect('restaurants.db')
# cur = con.cursor()
# cur.execute('''CREATE TABLE IF NOT EXISTS restaurant_branches
#                (id integer PRIMARY KEY, name text NOT NULL, latitude real , longtitude real)''')
# cur.execute("INSERT INTO restaurant_branches VALUES (1,'Kosem et mangal',40.93863191722981, 29.15052954198023)")

# restaurant_list =[
#     (2,'Filiz ev yemekleri',40.93896586140217, 29.15163922824145),
#     (3,'Derman ev yemekleri',41.000071811889654, 29.06570811271299),
#     (4,'Akarsu rest.',40.94409079625333, 29.140019756329007),
#     (5,'1 kafe rest.',41.00045697812768, 29.100616210880222),
#     (6,'Razaki balık',40.96863466153063, 29.085713923859128),
#     (7,'Davet doner',40.97364403457255, 29.07765035732342),
#     (8,'Develi 1912',40.98635842720057, 29.107557002829264),
#     (9,'Cunda rest.',40.954837653043846, 29.093369208544924),
#     (10,'Doner sarayı',40.99182871492699, 29.059481814501876),
#     (11,'Misina balık',40.96932828999839, 29.058052828027193),
#     (12,'Kackar yoresel',40.970638456672134, 29.111027398052904),
#     (13,'Keyifli teras',40.992059843839826, 29.12562347418715),
#     (14,'Kundal rest',41.02340882151914, 29.06295221006121),
#     (15,'Alemdağ',41.02479491837381, 29.072138551684162),
#     (16,'Ritsa rest.',41.02196604681947, 29.035174710446164),
#     (17,'Kızıldağ rest.',41.0105678947184, 29.01373991332594),
# ]
#
# cur.executemany("INSERT INTO restaurant_branches VALUES (?,?,?,?)", restaurant_list)
# con.commit()
# con.close()

def distance(latitude,longtitude):
    # main location is 40.93398716270305, 29.141618426900923 - MALTEPE E5
    mainCoordinate = (40.93398716270305, 29.141618426900923)
    restCoordinate = (latitude,longtitude)
    return (geopy.distance.distance(mainCoordinate, restCoordinate).km)

def findFirst5Restaurant():
    con = sqlite3.connect('restaurants.db')
    cur = con.cursor()
    restaurantsMin = []
    for row in cur.execute('SELECT name,latitude,longtitude FROM restaurant_branches'):
        distBetween = distance(row[1], row[2])
        if (distBetween <= 10): # max 10km from customer
            restaurantsMin.append([row[0], distBetween])

    print("------------------------------------------------------------------------------")
    print("NEAREST 5 RESTAURANTS AND DISTANCE FROM CUSTOMER LOCATION")
    print(sorted(restaurantsMin, key=itemgetter(1))[:5])
    print("------------------------------------------------------------------------------")

findFirst5Restaurant()



