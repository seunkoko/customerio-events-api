# Customerio Events API

API for Customerio Events Data Summary. Find out more info [here](https://github.com/seunkoko/customerio-events-app).

Frontend APP hosted on netlify [here](https://customerio-events.netlify.app)
Backend API hosted on heroku [here](https://customerio-events-api.herokuapp.com/)

### Features
---

* Get all customer data summary with pagination.
* Post customer.
* Get single customer.
* Patch customer data summary attribute.
* Delete customer.

### Endpoints
---

This is the [link](https://customerio-events-api.herokuapp.com/) in which to access the api. 

Below are the collection of routes.


#### Routes
EndPoint          |   Functionality    |    Request body/params
------------------|--------------------|--------------------------------------------------------------
GET /customers     | Gets all customer   | params [page (int), per_page (int)]
POST /customers       | Creates customer    | body [customer (object)]        
GET /customers/customer_id      | Gets single user data summary    | 
PATCH /customers/customer_id       | Update user attribute    | body [customer (object)]  
DELETE /customers/customer_id  | Delete user attribute | 


### Technologies Used
---

- Python
- Flask
- Flask-Restful


### Installation
---

- Clone the project repository.
- Run git clone https://github.com/seunkoko/customerio-events-api.git.
- Change directory into the customerio-events-api directory.
- Create a virtual environment for the python app. You can refer to this [link](https://packaging.python.org/guides/installing-using-pip-and-virtualenv/).
- Activate your vitual environment.
- Install all necessary packages in the requirements.txt file. You can use the command `pip3 install -r requirements.txt`.
- Set up your environment variable. Checkout `.env.sample`  in the root folder to do this.
- Export your FLASK_APP in the terminal by running this command `export FLASK_APP=server.py`.
- To start your app locally, run `python3 server.py`.
- Use Postman or any API testing tool of your choice to access the endpoints defined above.
- To run tests, run `pytest -v`.


#### Contributing
---

1. Fork this repository to your account.
2. Clone your repository: git clone https://github.com/seunkoko/customerio-events-api.git.
4. Commit your changes: git commit -m "did something".
5. Push to the remote branch: git push origin new-feature.
6. Open a pull request.


### Future Futures
---
- Sort and search Customer Data
- Better structured response format


Copyright (c) 2021 Oluwaseun Owonikoko
