import random
from sqlalchemy import MetaData, Table, Column, Integer, String, Boolean

user_table = MetaData()

user = Table(
    "user",
    user_table,
    Column("id", Integer, primary_key=True),
    Column("username", String, nullable=False),
    Column("email", String, nullable=False),
    Column("hashed_password", String, nullable=False),
    Column("is_active", Boolean, default=True, nullable=False),
    Column("is_superuser", Boolean, default=False, nullable=False),
    Column("is_verified", Boolean, default=False, nullable=False),
    Column("salary", Integer, nullable=False, default=int(random.uniform(45000, 150000))),
    Column("salary_increase_date", String, nullable=False, default="01.01.2045"),

)
