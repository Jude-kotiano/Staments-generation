from jinja2 import Template
from render import get_data_from_api,render_temp
import datetime
from typing import List,Dict,Any


def quotation_generation(orders: List[Dict[str, Any]], company_name: str
              , customer_name: str,
              date:datetime.datetime,customer_address:str)->None:
    qoute_mess='''
    
    < ! DOCTYPE html>
    <html>
    <head></head>
        <body>
    
            <h3>{{company_name}}</h3>                  <h1>QUOTATION</h1>
                                            <h3>Date</h3> {{date}}
                                            quatation {{quotation_number}}
                                            
            <h3>Quotation For</h3>
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
                            <td>Quantity</td>
                            <td>Description</td>
                            <td>Unit Price</td>
                            <td>Amount</td>
                            

                        </tr>
                    </thead>
                    <tbody>
                        {% for items in order %}
                                <td>{{items['quantity']}}</td>
                                <td>{{items['name']}}</td>
                                <td>{{items['price']}}</td>
                                <td>{{items['amount']}}</td>
                            
                        {% endfor %}
                    </tbody>
               </table>                                                         
            </div>
        </body>
    </html>
    
    '''
    quotation_template=Template(qoute_mess)
    if __name__ == 'main':
        api_data=get_data_from_api()
        rendered_quotation=render_temp(quotation_template,api_data=api_data)
