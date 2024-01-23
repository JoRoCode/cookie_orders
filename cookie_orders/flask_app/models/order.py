
from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash, session
# import re
# import re
# from flask_bcrypt import Bcrypt
# bcrypt = Bcrypt(app)
# The above is used when we do login registration, flask-bcrypt should already be in your env check the pipfile

# Remember 'fat models, skinny controllers' more logic should go in here rather than in your controller. Your controller should be able to just call a function from the model for what it needs, ideally.

class Order:
    db = "cookie_orders" #which database are you using for this project
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.cookie_type = data['cookie_type']
        self.number_of_boxes = data['number_of_boxes']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        # What changes need to be made above for this project?
        #What needs to be added here for class association?



    # Create Users Models
    @classmethod
    def create_new_order(cls,data):
        if not cls.validate_order(data): return False
        query = """
            INSERT INTO orders (name, cookie_type, number_of_boxes)
            VALUES (%(name)s, %(cookie_type)s, %(number_of_boxes)s);"""
        results = connectToMySQL(cls.db).query_db(query,data)
        return results


        # Read Users Models
    @classmethod
    def get_order_by_id(cls, id):
        data = {'id': id}
        query = """
            SELECT * FROM orders
            WHERE id = %(id)s;"""
        results = connectToMySQL(cls.db).query_db(query,data)
        order_data = cls(results[0])
        return order_data
        


    @classmethod
    def get_all_orders(cls):
        query = """
            SELECT *
            FROM orders
            ;"""
        results = connectToMySQL(cls.db).query_db(query)
        print (results)
        all_orders = []
        for result in results:
            all_orders.append(result)
            print(all_orders, "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        return all_orders

    # Update Users Models

    @classmethod
    def edit_one_order(cls,data):
        if not cls.validate_order(data): return False
        data = {'id': data['id'],
                'name': data['name'],
                'cookie_type': data['cookie_type'],
                'number_of_boxes': data['number_of_boxes']
                }
        query = """
            UPDATE orders
            SET name = %(name)s, cookie_type = %(cookie_type)s, number_of_boxes = %(number_of_boxes)s
            WHERE id = %(id)s;"""
        results = connectToMySQL(cls.db).query_db(query,data)
        return results

    # Delete Users Models
    
    
    
    # validations:
    
    @classmethod
    def validate_order(cls, data):
        is_valid = True
        if len(data['name']) < 1:
            flash("Name is required.")
            is_valid = False
        if len(data['name']) < 2:
            flash("Name must be at least 2 charicters.")
            is_valid = False
        if len(data['cookie_type']) < 1:
            flash("Cookie Type is required.")
            is_valid = False
        if len(data['cookie_type']) < 2:
            flash("Cookie Type must be at least 2 charicters.")
            is_valid = False
        if len(data['number_of_boxes']) < 1:
            flash("Please enter a valid number.")
            is_valid = False
        return is_valid