# Inserir dados de planilhas no Banco de Dados Postgres usando Python, de forma performática.

## Enunciado

Fazer um script Python que leia as fontes de dados e insira os dados no banco de dados PostgreSQL. As fontes de dados são os seguintes datasets:

- [NBA Players and Team Data](https://www.kaggle.com/datasets/loganlauton/nba-players-and-team-data)
- [Top Tech Startups Hiring 2023](https://www.kaggle.com/datasets/chickooo/top-tech-startups-hiring-2023?select=json_data.json) (somente o arquivo `json_data.json`).

O objetivo é incluir todas as fontes de dados do dataset da NBA e do dataset Top Tech Startups, mas apenas usando o arquivo `json_data.json`.

Recomenda-se criar um esquema separado no banco de dados PostgreSQL e uma tabela separada para cada dataset. Os dados devem ser armazenados na tabela utilizando o data type mais apropriado (é recomendável utilizar id autoincremental e data de criação do registro). Deve-se parsear o JSON para incluir cada chave como se fosse uma coluna na tabela do PostgreSQL.

Busque utilizar boas práticas de programação para criar o script e não hesite em compartilhar entre si boas práticas para elaborar os exercícios.

Envie o link do GitHub com o projeto realizado no canal `desafio-1-março-2023`. Apresente no seu projeto provas de que a solução funciona.

Na próxima aula, pelo menos uma pessoa deve apresentar (explicar) o código utilizado e então vamos discutir juntos para compartilharmos boas práticas.

## Solução Proposta:

![Solução Proposta](/img/replication_data_how_bootcamp.png)

A Solução consiste em conectar via API no Kaggle e realizar a extração dos datasets solicitados e realizar a ingestão no postgres.

## Como utilizar:

1 - Crie o container do Postgres utilizando o `docker-compose.yml`. 
- O docker deve tá configurado em sua máquina. [Mais informações](https://docs.docker.com/engine/install/ubuntu/)

2 - Para melhor execução do replication data, crie um ambiente virtual do python utilizando o virtualenv. [Mais informações](https://docs.python.org/pt-br/3/library/venv.html)

3 - Intale os `requirements.txt` usando o pip3:
 ```pip3 install -r requirements.txt```

4 - Configure as credenciais do Kaggle. [Mais informações](https://www.kaggle.com/docs/api)

5 - Execute o script de extração `download-datasets-kaggle.sh`.
-   Este conecta via api no kaggle e faz o download do files para o diretório datasets do projeto.

6 - Execute o script de ingestão de dados no postgres `replication_data.py`.
- Este utiliza-se de uma classe **Database** em **db_utils**, essa abstrai as interações com o banco postgres, para realizar a conexão com a base, ler os CSVs e JSONs disponíveis no datasets, faz as tratativas necessárias e os insere no postgres, atribuindo o nome do arquivo ao nome da tabela a criada.

# Resultado:

![Resultado](/img/postgres_how.png)
