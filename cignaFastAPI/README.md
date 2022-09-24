1) visit floder cignaFastAPI

2)create vevn 
    python -m  venv venv 

3) Activate venv
  venv/Scripts/Activate

 4) insatall all dependence 

   pip install -r requirements.txt
   
5) run the app

unicorn main:app --reload 

note : create following table and edit db.py config file store data In DynomoDB 

 List of table required to create 
   employee,analytics (no sort key , partition key will "id" and data type should be str for the both table  )


