import os

script_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(script_dir)

database_dir = os.path.join(parent_dir, 'database')
database_path = os.path.join(database_dir, 'dataase.db')


print(database_path)