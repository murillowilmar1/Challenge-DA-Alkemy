# -*- coding: utf-8 -*-


# Importar libreria para conexión  a base de datos
from sqlalchemy import create_engine

# Importar carpeta propia para utilizar las vatiables 
from transformacion import uniq_table1, dynamic_table_cines, data_regis_provin

# Utilizar variable para conexión 

engine = create_engine ("postgresql://postgres:2369115@localhost:5432/challenge")

# Pasar tabla nunica  a SQL 
uniq_table1.to_sql("uniq_table_sql", con=engine, if_exists="replace")

# Pasar tabla con cantidad de pantallas, butacas y espcios a SQL 

dynamic_table_cines.to_sql("table_cines", con=engine, if_exists="replace")

# pasar tabla de registros y provincias a SQL
data_regis_provin.to_sql("table_resgis_fuen", con=engine, if_exists="replace")