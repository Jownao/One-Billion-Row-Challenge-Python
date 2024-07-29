# Minha Contribuição

Foi criado um arquivo chamado **to_parquet.py**, onde fiz a conversão de .txt para .parquet. O código foi implementado de maneira simples, sem tratamento de exceções nem feedback visual no console (prints). Também foi criado outro arquivo chamado **using_duckdb_parquet.py** que, como o próprio nome já diz, é o mesmo código, mas feito para ler arquivos .parquet.

## Comparação entre (DuckDB + Python) e (DuckDB + Python + Parquet)

### 1 milhão de linhas
* **DuckDB + Python:** 0.11 segundos
* **DuckDB + Python + Parquet:** 0.10 segundos

### 10 milhões de linhas
* **DuckDB + Python:** 0.28 segundos
* **DuckDB + Python + Parquet:** 0.14 segundos

### 100 milhões de linhas
* **DuckDB + Python:** 1.94 segundos
* **DuckDB + Python + Parquet:** 0.90 segundos

### 500 milhões de linhas
* **DuckDB + Python:** 76.47 segundos
* **DuckDB + Python + Parquet:** 4.87 segundos