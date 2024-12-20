# Para configurar la identidad del git

### Primero. colocamos el nombre del usuario.
>git config --global user.name "Leonardo"

### Segundo. Ahora ingresamos el correo.
>git config --global user.email "leonardo@example.com"

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

### Con este codigo pedimos la rama la cual le copiara todo.
>git pull origin master --allow-unrelated-histories

### Resolver conflito si es que hay.
>git add archivo_con_conflicto

>git commit -m "Resolver conflictos de fusión"

>git push origin master

### Si después de estos pasos sigues teniendo problemas, una opción más drástica es forzar el push, aunque debe hacerse con precaución:

>git push origin master --force

### Si quieres abortar el Merge 
<<<<<<< HEAD

=======
>>>>>>> 36a520f1e86e726bc6225478aa0b8fca034d9659
> git merge --abort

----------------------------------------------------------------------------------------

