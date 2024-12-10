# Para configurar la identidad del git
...
git config --global user.name "Leonardo"
...
git config --global user.email "leonardo@example.com"

git remote add origin https://github.com/tuusuario/tu-repositorio.git

----------------------------------------------------------------------------------------
 # Comandos git para subir al repositorio

git status

git add .

git commit -m "Tu mensaje descriptivo sobre los cambios"

git push origin nombre_de_la_rama

----------------------------------------------------------------------------------------
# Rama local desactualizada en comparación con la rama remota

git pull origin master --allow-unrelated-histories

 #### Resolver conflito si es que hay:
 git add archivo_con_conflicto

git commit -m "Resolver conflictos de fusión"

git push origin master

#### Si después de estos pasos sigues teniendo problemas, una opción más drástica es forzar el push, aunque debe hacerse con precaución:

git push origin master --force

