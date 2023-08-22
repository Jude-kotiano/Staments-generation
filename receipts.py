from typing import Any,Dict,List
from jinja2 import Template
from render import get_data_from_api,render_temp
import datetime

def receipts_generation(orders: List[Dict[str, Any]], payment_date: str, 
             receipt_number: str
             , company_name: str, company_address: str, customer_name: str, customer_address: str)->None:
    receipt_mess='''
    <!DOCTYPE html>
    <html>
        <head></head>
        <body>
            <h1>RECEIPT</h1>
            <h5>Payment Date</h5> {{payment_date}}    <h5>Receipt Number</h5> {{receipt_number}}       
            <h6>From :                            Sold To : </h6>
            {{company_name}}                   {{customer_name}}
            {{company_address}                {{customer_address}}
            <section>
                <div></div>
                <div></div>
                
            </section>                    
            <div>
                <table>
                    <thead>
                        <tr>
                            <td>Description</td>
                            <td>Quantity</td>
                            <td>Unit Price</td>
                            <td>Total</td>
                            
                        </tr>
                        <tbody>
                            {% for items in orders %}
                                <tr>
                                    <td>{{items['name']}}</td>
                                    <td>{{items['quantity']}}</td>
                                    <td>{{items['price']}}</td>
                                    <td>{{items['amount']}}</td>
                                    
                                </tr>
                            {% endfor %}
                        </tbody>
                    </thead>
                </table>                                                    
            </div>
        </body>
    </html>
    '''
    receip_template=Template(receipt_mess)
    if __name__ == 'main':
        api_data=get_data_from_api()
        rendered_receipt=render_temp(receip_template,api_data=api_data)