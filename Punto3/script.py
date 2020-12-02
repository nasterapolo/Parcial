import requests
import requests
import json
import pprint


api= 'http://192.168.80.3:5000/books'
api_put = 'http://192.168.80.3:5000/books/2'
api_delete = 'http://192.168.80.3:5000/books/6'



# METODO GET

get = requests.get(url = api)


# Imprimimos el resultado si el codigo de estado HTTP es 200 (OK)
m = '\nMensaje obtenido con GET: \n \n'
if get.status_code == 200:
        print m + get.text

# METODO POST
post_d = {'title': 'Nuevo libro'}
data_json = json.dumps(post_d)
headers = {'Content-type': 'application/json'}
post= requests.post(url=api, data= data_json, headers = headers)
m1 = '\nMensaje obtenido con POST: \n \n'
if get.status_code == 200:
        print m1 + post.text


# METODO PUT

put_d = {'author': 'Gabo3'}
data_p_json = json.dumps(put_d)
put = requests.put(url = api_put, data = data_p_json, headers=headers)
m2 = '\nMensaje obtenido con PUT: \n \n'
if get.status_code == 200:
        print m2 + put.text

# METODO DELETE

delete = requests.delete(url = api_delete)
m3 = '\nMensaje obtenido con DELETE: \n \n'
if get.status_code == 200:
        print m3 + delete.text