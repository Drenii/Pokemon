Read Me:

Framework Version : Django 3.1.7
Python Version : 3.9.6
Database: Postgresql(pgAdmin 4)
Editor:Pycharm



Structure:
pokemon 
 pokemon
 pokemonApp
 templates
   - home.html



Opened pgAdmin 4 tool and created a database named pokemon.
In models.py created the model Pokemon with properties id_pokemon, name, type1,type2, total, hp, attack,defense,sp_atk,sp_def,speed, generation,legendary.
Then imported the csv file to PgAdmin4 to pokemonApp_pokemon table.
Made migrations
In urls.py - pokemonApp added the route to index.
In views added the logic for sorting ascending based on name column and descending based in total, you have to click 
in name to see the ascending order(based on names) and  click total to see the descending order (baset on total).
Use the search field to filer data based on Type 1 or Type 2.


 