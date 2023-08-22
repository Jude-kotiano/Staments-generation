from jinja2 import Template
import datetime
import pytest
dat='21/08/2023'
num='123'
cust='jude'

from invoice import invoice_generation
from quotation import quotation_generation
from receipts import receipts_generation

sample_order = [{'name': 'Product A', 'quantity': 2, 'price': 10, 'amount': 20},
    {'name': 'Product B', 'quantity': 3, 'price': 15, 'amount': 45}
]

@pytest.fixture
def sample_date():
    return datetime.datetime.now().strftime('%Y-%m-%d')

@pytest.fixture
def sample_number():
    return '12345'


@pytest.fixture
def sample_names():
    return {
        'company_name': 'CoCo Aviation',
        'customer_name': 'Jude Kotiano'
    }

@pytest.fixture
def sample_addresses():
    return {
        'company_address': '123 Main St, City',
        'customer_address': '456 Another St, Town'
    
    }
    

#def test_invoice_generation(sample_date, sample_number, sample_names, sample_order):
    #invoice(sample_order, sample_number, sample_date, sample_names['customer_name'])

#def test_quotation_generation(sample_date, sample_names, sample_addresses, sample_order):
    #quotation(sample_order, sample_names['company_name'], sample_names['customer_name'], sample_date, sample_addresses['customer_address'])

#def test_receipt_generation(sample_date, sample_number, sample_names, sample_addresses, sample_order):
    #receipts(sample_order, sample_date, sample_number, sample_names['company_name'], sample_addresses['company_address'], sample_names['customer_name'], sample_addresses['customer_address'])
    
def test_invoice():
    inv=invoice_generation(sample_order,dat,cust)

if __name__ == '__main__':
    pytest.main()