# Restaurant Api 

This API serves to bring the first 5 restaurants with a maximum distance of 10 km from the restaurant network to the customer.
###How it works?

- First, data is entered into the local database created with Sqlite3 on the lines that have been commented out.
- Distance function calculates the distance between the customer location and any specified location.
- The findFirst5Restaurant function calculates the distance from the customer to all records in the database using the distance function. It then adds records that are 10km or less away to a list. Finally, the list is sorted from smallest to largest according to the distance column and the first 5 records are printed on the screen.


### How to run?
While in the same directory, you can run it from the terminal with the command "python main.py".

## Sample output screenshot
![](https://github.com/MrUbeyd/restaurantApi/blob/master/restaurantApiSS.PNG?raw=true)
