from models import Customer
from table import Table
from table.columns import Column

class CustomerTable(Table):
    id = Column(field='id')
    name = Column(field='customerName')
    email = Column(field='customerEmail')
