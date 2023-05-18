# <h1> Pj_07-000 Desarrollo de Dasboard para visulizar el engagement  de cursos virtuales de Data Science publicados en la web de 365 Data Science en el año 2022 </h1> 

<hr>

*El presente proyecto es el reto propuesto por [365 DataScience](https://365datascience.com/) en 2022. Busca analizar el engagement existente entre los usuarios de esta plataforma de E-learning y los cursos que ofrece a través de un dashboard en PowerBi*<br>

## 1. Introducción

Se analizan los datos suministrados por la plataforma de cursos digitales [365 DataScience](https://365datascience.com/) a través de 11 datasets. La información relaciona los cursos realizados por usuarios y sus desempeños durante el 2022. Se crea una BD relacional en MySQL para almacenar los datasets. Se desarrolla un Dashboard en Power BI que tenga las siguientes características. 

<img src="src/365_dashboard_skeleton.png" width="400" height="500px">

*La estructura del dashboard es un esquema guía planteado por [365 DataScience](https://365datascience.com/).*<br>
*El diccionario de los datos: [Data_dict](data_dict.md).*
<hr>

## 2. Objetivos

- Crear una base de datos en SQL para almacenar la información de los cursos.
- Generar 3 KPIs.
- Desarrollar un dashboard para a través de la visualización de los datos validar insighs.  

<hr>

## 3. Recursos implementados

Python 3.9, PyMySQL<br>
MySQL Workbench.<br>
Microsoft PowerBi. <hr>

## 4. Resultados

### 4.1 Base de datos

Se genenran dos scripts para crear una base de datos relacional con los 11 datasets suministrados por [365 Data Science](https://365datascience.com/).<br>

*[**Python Script**](/DB/createBD.py) <br>
*[**SQL Script**](/DB/createDB.sql)

*Los datasets pueden ser consultados en: [datasets](/data).*<br>
*El modelo de entidad-relación de la base de datos puede ser consultado en: [Modelo ER](/DB/ER-BD.png).*

### 4.2 Dashboard


<img src="src/image1.jpg" width="650" height="350px">

*Se puede consultar el dashboard realizado en: [Dashboard](https://app.powerbi.com/view?r=eyJrIjoiZDhjMTEwOTQtYmNlZS00MDFhLWFlMjItMzkxNzNlYzE4ODQwIiwidCI6ImRmODY3OWNkLWE4MGUtNDVkOC05OWFjLWM4M2VkN2ZmOTVhMCJ9)*

El dashboard presenta métricas de la plataforma como *(Cantidad de cursos, Estudiantes registrados, Compras en la Plataforma..)* entre otros.

**KPIs**

- Purchase Convertion: # usuarios registrados/ # usuarios que realizan compras
## 5. Conclusiones



