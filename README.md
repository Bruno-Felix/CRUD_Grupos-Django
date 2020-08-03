# Crud Grupos Musicais


## Sobre o Projeto

O projeto é um CRUD (Create, Read, Update e Delete) de Grupos Musicais onde se pode manipular os Grupos, os Artistas e as Músicas.


## Porque?

O projeto foi feito no intuito de servir como uma inicialização ao Django e ao Desenvolvimento Web.


## Funcionalidades

* Lista de Grupos:

  * Visualizar Grupo:
     * Editar Grupo;
     * Excluir Grupo;
     * Lista de Artistas do Grupo:
     
       * Visualizar Artista;
          * Editar Artista;
          * Excluir Artista.
     * Lista de Músicas do Grupo:
     
       * Visualizar Música.
            * Editar Música;
            * Excluir Música.
            
* Lista de todos Artistas;
* Lista de todas Músicas;
      

## Imagens

![Preview-Screens](https://github.com/Bruno-Felix/CRUD_Grupos/blob/master/novosGrupos/static/img/listaDeGrupos.png) 
![Preview-Screens](https://github.com/Bruno-Felix/CRUD_Grupos/blob/master/novosGrupos/static/img/visualizarGrupo.png)
<img src="https://github.com/Bruno-Felix/CRUD_Grupos/blob/master/novosGrupos/static/img/menuMobile.png" width="250">
<img src="https://github.com/Bruno-Felix/CRUD_Grupos/blob/master/novosGrupos/static/img/listaDeGruposMobile.png" width="250">
<img src="https://github.com/Bruno-Felix/CRUD_Grupos/blob/master/novosGrupos/static/img/visualizarGrupoMobile.png" width="250">

Para mais imagens, [clique aqui](https://drive.google.com/drive/folders/13_F1q7Dy3HBfuFGxwfPXQfPnM9hpzg1u?usp=sharing)


## Tecnologias

* Python
* Django
* VirtualEnv
* Crispy Forms
* HTML
* CSS


## Rodar Localmente

### Pré requisitos:

- Python
- Pip
- VirtualEnv
- Crispy forms

Instruções de instalação [aqui](https://github.com/Bruno-Felix/CRUD_Grupos/wiki/Pre-Requisitos)

### Instalando:

**Clonando Repositório**

```
$ git clone https://github.com/Bruno-Felix/CRUD_Grupos.git

$ cd CRUD_Grupos
```

**Ativando VirtualEnv**

```
$ cd venv

$ source bin/activate

$ cd ..
```

**Rodando o Projeto**

```
$ cd novosGrupos

$ python3 manage.py runserver
```
**Entrar no servidor de desenvolvimento**: http://127.0.0.1:8000/
