# Basic-Inventory-Management-System
A small local grocery store currently keeps track of their groceries inventory on a piece of paper. So I built a basic inventory management system for them where they can do four different things:  Add an item to the inventory system. (1)The item needs to have an id, name, price, and stock level  (2)Remove an item from the inventory  (3)Increase the stock of an item by a specific amount (4)Decrese the stock of an item by a specific amount



so i created two classes, one that represents the Grocery Item object and one that represents the Inventory object. Using these methods the user of the application should be able to manage the inventory from the console (see example at bottom).

The Grocery Item class should have the following methods and attributes:
Attributes:
id, name, price, stock

Methods which i used:
print_item - this prints the items information

The Inventory class should have the following methods:
Methods:
add_item - this takes an item as a parameter and saves it to the database

remove_item - this takes an item as a parameter and removes it from the database

add_stock - this takes an item and a number as a parameter and increases the items stock in the database by the number

remove_stock - this takes an item and a number as a parameter and decreases the items stock in the database by the number

print_inventory - this prints out every item in the database using the items id, name, price, and stock

