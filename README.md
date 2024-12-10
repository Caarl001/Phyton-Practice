# Para configurar la identidad del git
<<<<<<< HEAD

### Primero. colocamos el nombre del usuario.
>it config --global user.name "Leonardo"

### Segundo. Ahora ingresamos el correo.
>git config --global user.email "leonardo@example.com"
=======
...
git config --global user.name "Leonardo"
...
git config --global user.email "leonardo@example.com"

git remote add origin https://github.com/tuusuario/tu-repositorio.git
>>>>>>> 27c3897ef37f2088ab3909795ab0d91f94da866a

### Tercero. Tenemos que enlazar el repositorio.
>git remote add origin https://github.com/tuusuario/tu-repositorio.git
----------------------------------------------------------------------------------------
 # Comandos git para subir al repositorio

### Mostrar el estaso de las cosas que cambiamos o modificamos.
>git status
### Agregamos los cambios 
>git add .
### Aca se agregan con comentarios. pero no se suben todavias.
>git commit -m "Tu mensaje descriptivo sobre los cambios"
### Aca se suben a la rama que escribimos.
>git push origin nombre_de_la_rama

----------------------------------------------------------------------------------------
# Rama local desactualizada en comparación con la rama remota

git pull origin master --allow-unrelated-histories

 #### Resolver conflito si es que hay:
 git add archivo_con_conflicto

git commit -m "Resolver conflictos de fusión"

git push origin master

#### Si después de estos pasos sigues teniendo problemas, una opción más drástica es forzar el push, aunque debe hacerse con precaución:

git push origin master --force

