# -*- coding: utf-8 -*-


import pandas as pd

"""# Crear tabla unica """

#crear tabla unica 
uniq_table1 = pd.DataFrame(columns=["cod_localidad","id_provincia","id_departamento","categoría", "provincia","localidad","nombre","domicilio","código postal", "número de teléfono", "mail","web"])
uniq_table1

"""# Información de museos """

# Verificar Dataframe museos 

data=pd.read_csv("data/museos/2022-octubre/museos-13-10-2022.csv")
data 

print(data.columns.values)

# Borrar columnas no necesarias de museos 
data_museos1 = data.drop(["Observaciones", "subcategoria", "piso","cod_area","Latitud","Longitud","TipoLatitudLongitud","Info_adicional","fuente","jurisdiccion","año_inauguracion","actualizacion" ], axis=1)
print(data_museos1.columns.values)

# renombrar titulos de data_museos 
data_museos1 = data_museos1.rename(columns={"Cod_Loc":"cod_localidad","IdProvincia":"id_provincia", "IdDepartamento":"id_departamento","categoria":"categoría", "provincia":"provincia","direccion":"domicilio","CP":"código postal", "telefono":"número de teléfono","Mail":"mail","Web":"web"})
print(data_museos1.columns.values)

"""# Información de cines """

# Verificar Dataframe cines

data_1= pd.read_csv("data/cine/2022-octubre/cine-13-10-2022.csv")
data_1
print(data_1.columns.values)

#Borrar columnas no necesarias cines 

data_cines = data_1.drop(["departamento", "piso","latitud","longitud","tipo_latitud_longitud","sector","fuente","pantallas","butacas","año_actualizacion", "tipo_de_gestion","espacio_incaa" ], axis=1)
print(data_cines.columns.values)

# renombrar titulos de data_cines 
data_cines = data_cines.rename(columns={"direccion":"domicilio", "cp":"código postal","categoria":"categoría"})
print(data_cines.columns.values)
data_cines

"""# Información de bibliotecas """

# Verificar Dataframe bibliotecas 

data_2 = pd.read_csv("data/bibliotecas/2022-octubre/bibliotecas-13-10-2022.csv")
data_2
print(data_2.columns.values)

#Borrar columnas de bibliotecas  

data_biblio = data_2.drop(["Observacion", "Subcategoria", "Piso","Departamento","Cod_tel","Latitud","Longitud","TipoLatitudLongitud","Información adicional","Fuente","Tipo_gestion","año_inicio","Año_actualizacion", ], axis=1)
print(data_biblio.columns.values)

# renombrar titulos de data_museos 
data_biblio = data_biblio.rename(columns={"Cod_Loc":"cod_localidad","Nombre":"nombre","IdProvincia":"id_provincia", "IdDepartamento":"id_departamento","Categoría":"categoría","Localidad":"localidad", "Provincia":"provincia","Domicilio":"domicilio","CP":"código postal", "Teléfono":"número de teléfono","Mail":"mail","Web":"web"})
print(data_biblio.columns.values)
data_biblio

"""# Crear tabla unica con append y concat """

# crear tabla unica anexando datos con append 
uniq_table1 = uniq_table1.append(data_museos1)
uniq_table1=uniq_table1.append(data_cines)
uniq_table1 = uniq_table1.append(data_biblio)


uniq_table1

uniq_table1 = pd.concat([data_museos1,data_cines,data_biblio],axis=0)
uniq_table1

"""# crear tabla información cines"""

# convertir categorica a entero 
data_1["espacio_incaa"].replace(["Si", "No"],[1,0], inplace=True)

prov = data_1["provincia"]
pant = data_1["pantallas"]
but = data_1["butacas"]
espa_in = data_1["espacio_incaa"]

tabla_cines = pd.concat([prov,pant,but,espa_in], axis=1)

tabla_cines.info()

tabla_cines

dynamic_table_cines = pd.pivot_table(tabla_cines,index=["provincia"], values=["pantallas","butacas","espacio_incaa"],aggfunc="sum")

dynamic_table_cines

"""# Tabla para totalizar """

data

data_museos2 = data.rename(columns={'fuente':'Fuente', 'categoria':'Categoría', 'provincia':'Provincia', 'nombre':'Nombre'})

data_u = data_museos2.append(data_1).append(data_2)
data_u

df = data_u.drop(['Cod_Loc', 'IdProvincia', 'IdDepartamento', 'Observaciones', 'subcategoria', 'localidad', 'direccion', 'piso', 'CP', 'cod_area', 'telefono', 'Mail', 'Web', 'Latitud', 'Longitud', 'TipoLatitudLongitud', 'Info_adicional', 'jurisdiccion', 'año_inauguracion', 'actualizacion', 'Departamento', 'Localidad', 'Piso', 'Teléfono', 'Información adicional', 'Tipo_gestion', 'pantallas', 'butacas', 'espacio_incaa', 'año_actualizacion', 'Observacion', 'Subcategoria', 'Domicilio', 'Cod_tel', 'Tipo_gestion', 'año_inicio', 'Año_actualizacion'], axis=1)

df

# crear tabla 

data_regis_provin= df.pivot_table(values='Nombre', index=['Fuente', 'Categoría'], columns=['Provincia'], aggfunc='count', margins=True)
data_regis_provin

