# Processamento Digital de Imagens

**[DockerHub](https://cloud.docker.com/u/gfviegas/repository/docker/gfviegas/pdi)**

## Display
Lembre-se de passar a variável de ambiente `DISPLAY` com o caminho do xserver da sua interface gráfica.

## Exemplo de Uso
### Docker Run
Na pasta onde deseja salvar os arquivos do Jupyter:
```bash
docker run -e DISPLAY={$DISPLAY} -it -v "$PWD":/code -w /code gfviegas/pdi
```

### Docker Compose
Adicione o arquivo docker-compose.yml na pasta onde deseja salvar os arquivos do Jupyter, e execute:
```bash
docker-compose up
```
