import awswrangler as w
import numpy as np
import pandas as pd
import json
class EmployeeSearch:

    def searchemp(self,search:str):
        
        conn=w.opensearch.connect(host='https://search-cignasearch-pfaps6fr43oxcn3oevrtwisd2e.us-east-1.es.amazonaws.com/',
                          port=443,
                          username='sandeepnr',
                          password='Sa9741226572@')
                       
        
        df=w.opensearch.search(client=conn,index='opensearch_dashboards_sample_data_ecommerce',
        search_body={'query':{
            'match':{ 'category':"Men's Clothing"} 
            }
       })
       
      
        json_list = json.loads(json.dumps(list(df.head().T.to_dict().values())))
        print(type(df.head()))
        return json_list