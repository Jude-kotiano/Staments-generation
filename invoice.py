from jinja2 import Template,Environment
from typing import Any, Dict, List
import datetime
from render import get_data_from_api,render_temp

def invoice_generation(orders: List[Dict[str, Any]], 
            invoice_number: str,customer_address:str,
            date: datetime.datetime, customer_name: str)->None:

    invoice_mess = ''' 
    < !DOCTYPE html>
    <html>
        <head></head>
        <body>
            <h2>INVOICE</h2>
            
            invoice number:{{invoice_number}}  Date of issue {{date}}
            
            Billed to:
            {{customer_name}}
            {{customer_address}}
            <section>
                <div></div>
                <div></div>
            </section>
            <div>
                <table>
                    <thead>
                        <tr>
                            <td> Name </td>
                            <td>  Quantity </td>
                            <td> Unit Price </td>
                            <td> Amount </td>
                        </tr>
                    </thead>
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
                </table>        
            </div>
        </body>
    </html>
    '''
    invoice_template=Template(invoice_mess)
    if __name__ =='main':
        api_data=get_data_from_api()
        rendered_invoice=render_temp(invoice_template,api_data=api_data)
