import pyodbc
import pandas as pd
from sqlalchemy import create_engine

# Configuración de la conexión
server = r'DESKTOP-IB90627\SQLEXPRESS01'
database = 'Etapa3'
username = 'sa'
password = '2024Data*'
driver='ODBC Driver 17 for SQL Server'
connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'

'''
# Conexión a la base de datos
conn = pyodbc.connect(connection_string)
cursor = conn.cursor()

# Crear una tabla (si no existe)
cursor.execute(
    IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='Personas' AND xtype='U')
    CREATE TABLE Personas (
        Id INT PRIMARY KEY IDENTITY,
        Nombre NVARCHAR(50),
        Edad INT
    )
)
conn.commit()

# Insertar datos
cursor.execute(
    INSERT INTO Personas (Nombre, Edad) 
    VALUES (?, ?)
, ('Juan Perez', 28))
conn.commit()

# Insertar datos v2
Personas = [
    ('Juan Cardona', 28),
    ('Ana Jimenez', 34)
]'''
engine = create_engine(f'mssql+pyodbc://{username}:{password}@{server}/{database}?driver={driver}')
'''
df=pd.read_csv(r'C:\Bootcamp\AnalisisDeDatos\Proyecto\Etapa 3\data_combinada.csv')
df.columns = ['Date', 'Symbol', 'Cierre']
def load_data_to_sql(engine, df, table_name):
    """Cargar los datos de un DataFrame a una tabla d SQL SERVER"""
    try:
        df.to_sql(table_name, con=engine, if_exists='replace', index=False)
        print(f"Datos cargados correctamente en la tabla {table_name}")
    except Exception as e:
        print(f"Error al cargar los datos: {e}")
df.to_sql('Companies', con=engine, if_exists='replace', index=False)
load_data_to_sql(engine, df, 'Companies')

'''
df=pd.read_csv(r'C:\Bootcamp\AnalisisDeDatos\Componente_Tecnico\Proyecto\empresasSp500.csv')
df=df.drop(columns=['Presentación ante la SEC','Sub-industria GICS','Fecha de incorporación','Clave de índice central'])

df.columns=['Symbol', 'Company','Sector','Headquarters','Fechafudada']
def load_data_to_sql(engine, df, table_name):
    """Cargar los datos de un DataFrame a una tabla d SQL SERVER"""
    try:
        df.to_sql(table_name, con=engine, if_exists='replace', index=False)
        print(f"Datos cargados correctamente en la tabla {table_name}")
    except Exception as e:
        print(f"Error al cargar los datos: {e}")
df.to_sql('CompanyProfiles', con=engine, if_exists='replace', index=False)
load_data_to_sql(engine, df, 'CompanyProfiles')

'''
insert_query = 'INSERT INTO Personas (Nombre, Edad) VALUES (?, ?)'
for persona in Personas:
    cursor.execute(insert_query, persona)
conn.commit()
print("Registros insertados en la tabla 'Empleados'.")


# Consultar datos
cursor.execute('SELECT * FROM Personas')
rows = cursor.fetchall()

# Consultar datos v2
query = 'SELECT * FROM Personas WHERE Nombre = ?'
cursor.execute(query, ('Juan Cardona'))
rows = cursor.fetchall()

# Mostrar resultados de la consulta
for row in rows:
    print(f'Id: {row.Id}, Nombre: {row.Nombre}, Edad: {row.Edad}')

# Cerrar la conexión
cursor.close()
conn.close()
'''