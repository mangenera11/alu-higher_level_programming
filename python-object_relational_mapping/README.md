# python-object_relational_mapping

Scripts that connect Python to MySQL, first with MySQLdb and then with the
SQLAlchemy ORM.

## Requirements
- Ubuntu, Python 3, MySQL
- python3-mysqldb and python3-sqlalchemy

## Files
- 0 to 5: MySQLdb scripts (select, filter, SQL-injection-safe queries, joins)
- model_state.py, model_city.py: SQLAlchemy models
- 7 to 13: SQLAlchemy scripts (list, filter, get, insert, update, delete)
- 14-model_city_fetch_by_state.py: lists cities with their state
