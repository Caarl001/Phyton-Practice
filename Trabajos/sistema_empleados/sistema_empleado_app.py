from Trabajos.sistema_empleados.empleado import Empleado
from Trabajos.sistema_empleados.empresa import Empresa

print(' --- Sistema De Empleados --- ')

# Crear una instancia de una empresa
empresa1 = Empresa('Movistar Arena')
empresa2 = Empresa('Entel pcs')
empresa3 = Empresa('Wow')
empresa4 = Empresa('Claro')

# Contratar algunos empleados}
empresa1.contratar_empleado('Juan', 'Ventas')
empresa1.contratar_empleado('Maria', 'Marketing')
empresa1.contratar_empleado('Pedro', 'Ventas')
empresa1.contratar_empleado('Ana', 'Recursos Humanos')

# Obtener el total de objetos de tipo empleado
print(f'Total de empleados: {Empleado.obtener_total_empleado()}')

# Obtener el numero de empleados en el departamento de ventas
print(f'Empleados en el departamento de Ventas: '
      f'{empresa1.obtener_numero_empleados_departamento('Ventas')}')
# Cuantos empleados tenemos por empresa

print(f'Total empleados: {empresa1.obtener_total_empleado()}')