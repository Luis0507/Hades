#from django.test import TestCase
from config.wsgi import *
from core.erp.models import Type #Importamos el modelo

# Listar
# query = Type.objects.all()
# print(query)

# Insercion
# t = Type()
# t.name = 'Prueba02'
# t.save()

# Ediccion

# t = Type.objects.get(id=1)
# t.name = 'Presidente'
# t.save()

# Capturar Error
# try:
#     t = Type.objects.get(id=1)
#     t.name = 'Presidente'
#     t.save()
# except Exception as e:
#     print(e)

# Eliminacion
# t = Type.objects.get(id=1)
# t.delete()

#icontains = like
obj = Type.objects.filter(name__icontains='terry')
print(obj)