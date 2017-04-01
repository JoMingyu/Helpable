from database import Database

Database().execute("DELETE FROM account")
Database().execute("DELETE FROM help_list")
Database().execute("DELETE FROM user_contribution")
