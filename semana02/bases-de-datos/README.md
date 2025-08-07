# PostgreSQL

## Crear tablas

## Busqueda con restricciones

- =, =!, <, >, >, <=, >=: Operadoresd de comparación para valores numéricos y de texto.

```sql
    SELECT * FROM movies WHERE year = 2003;
```

- **BETWEEN**: Filtrar por rango de valores.
  ```sql
  SELECT * FROM movies WHERE year BETWEEN 2000 AND 2010;
  ```
- **NOT BETWEEN**: Filtra excluyendo el rango de valores.

  ```sql
  SELECT * FROM movies WHERE year NOT BETWEEN 2000 AND 2010;
  ```

- **IN**: Filtrar por lista de valores.

  ```sql
  SELECT * FROM movies WHERE year IN (2000, 2005, 2010);
  ```

- **LIKE**: Filtrar por patrón de texto.

  ```sql
  SELECT * FROM movies WHERE title LIKE 'Toy%';
  ```

- **%**: Cualquier cadena de caracteres.

- **\_**: Cualquier caracter.

## ORDENAR RESULTADOS

- **ORDER BY**: Ordenar resultados.
  ```sql
  SELECT * FROM movies ORDER BY id DESC;
  ```
- **ASC**: Ordenar de forma ascendente.
- **DESC**: Ordenar de forma descendente.

## Limitar resultados

- **Limit**: Limitar cantidad de resultados.
  ```sql
  SELECT * FROM movies LIMIT 5;
  ```
- **OFFSET**: Desplazar resultados.
  ```sql
  SELECT * FROM movies LIMIT 5 OFFSET 5;
  ```

## OPERADORES AND, OR Y NOT

- **AND**: Operador lógico Y.

  ```sql
  SELECT * FROM movies WHERE year >= 200 AND year <= 2010;
  ```

- **OR**: Operador lógico O.

  ```sql
  SELECT * FROM movies WHERE year = 2003 OR year = 2010;
  ```

- **NOT**: Operador lógico NOT.
  ```sql
  SELECT * FROM movies WHERE NOT year = 2003;
  ```

## Operador UPDATE

- **UPDATE**: Actualizar registros.
  ```sql
  -- UPDATE movies SET year = 2020 WHERE id = 1;
  ```

## Operador DELETE

```sql
DELETE FROM movies WHERE id = 2;
```

## OPERADOR JOIN

- **JOIN**: Unir tablas.
  ```sql
  SELECT title, domestic_sales
  FROM movies
  JOIN boxoffice ON movies.id = boxoffice.movie_id;
  ```
