dictionary = {'name':'Alejandro','age':20}
print('Name: '+dictionary['name'],'| Age: '+str(dictionary['age']))
dictionary['address']='Venezuela'
print('Adress: '+dictionary['address'])
print('Modificando el diccionario')
name=input('Nombre: ')
age=input('Edad: ')
address=input('Dirección: ')
dictionary['name']=name
dictionary['age']=age
dictionary['address']=address
print('Name: '+dictionary['name'],'| Age: '+str(dictionary['age']))
print('Adress: '+dictionary['address'])
print('Borrando datos...')
del dictionary['name']
del dictionary['age']
del dictionary['address']
print(dictionary)