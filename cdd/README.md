# Ciência de Dados

**[DockerHub](https://cloud.docker.com/u/gfviegas/repository/docker/gfviegas/cdd)**

## Port Foward
Lembre-se de encaminhar a porta 8888 para seu host (ou use o docker-compose.yml)

## Exemplo de Uso
### Docker Run
Na pasta onde deseja salvar os arquivos do Jupyter:
```bash
docker run -it -v "$PWD":/code -w /code -p 8888:8888 gfviegas/cdd
```

### Docker Compose
Adicione o arquivo docker-compose.yml na pasta onde deseja salvar os arquivos do Jupyter, e execute:
```bash
docker-compose up
```
