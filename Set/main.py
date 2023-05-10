# Set {}, conjunto sin orden (no hay indices) ni duplicados, permite agregar pero no modificar
planetas = {"marte","jupiter","venus"}
print(planetas)
print(len(planetas))
#ver si un elemento está en el set
print("marte" in planetas)
#agregar un elemento
planetas.add("tierra")
print(planetas)

# eliminar elementos
planetas.remove("tierra")
print(planetas)

planetas.discard("venus")
print(planetas)
# eliminar el contenido
planetas.clear()
print(planetas)

#eliminar por completo
del(planetas)
print(planetas)