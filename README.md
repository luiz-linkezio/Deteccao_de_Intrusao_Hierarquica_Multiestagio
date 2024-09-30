# Detecção de Intrusão Hierárquica Multiestágio

Projeto da cadeira de Detecção de Intrusão do curso de [Engenharia da Computação (EC)](https://portal.cin.ufpe.br/graduacao/#engenharia-da-computacao) do [Centro de Informática (CIn)](https://portal.cin.ufpe.br/) da [Universidade Federal de Pernambuco (UFPE)](https://www.ufpe.br/), cadeira cursada pela equipe, de 2023 a 2024. 

O professor da cadeira disponibilizou alguns artigos relacionados ao uso de inteligência artificial para segurança ou à segurança para sistemas baseados em inteligência artificial, os alunos foram divididos em grupos e cada grupo tinha que escolher um artigo ou propor ao professor a escolha de um artigo de fora dos disponibilizados pelo professor. Após a escolha do artigo, o grupo tinha que apresentar um seminário sobre o artigo, reproduzir o experimento do artigo no mesmo conjunto de dados e também em outro conjunto de dados, além disso, o grupo também poderia tentar realizar melhorias no sistema do artigo escolhido, e se obtivesse sucesso, poderia criar um artigo e realizar uma apresentação demonstrando a melhora. Para mais informações sobre as regras e requisitos, verifique o conteúdo do arquivo `Especificação_do_seminário_e_do_projeto.pdf` no diretório `Docs`.

## Organização de Diretórios/Arquivos

O diretório:
 - `Artigos` contém o [artigo do repositório base](https://ieeexplore.ieee.org/document/10077796) e o artigo feito por nossa equipe.
 - `models` contém na pasta `reprodução` os modelos do [repositório base](https://gitlab.ilabt.imec.be/mverkerk/multi-stage-hierarchical-ids), e dentro da pasta `melhorado` estão os modelos feitos pela nossa equipe para a melhoria do sistema.
 - `Repositório Base` contém o [repositório base](https://gitlab.ilabt.imec.be/mverkerk/multi-stage-hierarchical-ids) do artigo escolhido pela nossa equipe.
 - `data` contém os arquivos de [conjunto de dados](https://www.unb.ca/cic/datasets/) usados.
 - `notebooks/utils` contém alguns arquivos [python](https://www.python.org) com funções que auxiliam outros arquivos.
 - `notebooks/1º_Estágio(reprodução).ipynb` é o código de treino, validação e salvamento do modelo na reprodução do primeiro estágio.
 - `notebooks/1º_Estágio(melhorado).ipynb` é o código de treino, validação e salvamento do modelo na melhora do primeiro estágio.
 - `notebooks/2º_Estágio(reprodução).ipynb` é o código de treino, validação e salvamento do modelo na reprodução do segundo estágio.
 - `notebooks/2º_Estágio(melhorado).ipynb` é o código de treino, validação e salvamento do modelo na melhora do segundo estágio.
 - `notebooks/Tratamento_de_dados.ipynb` é o código de tratamento de dados
 - `notebooks/SistemaHierarquico(reprodução).ipynb` é o código da reprodução do sistema do artigo escolhido pela nossa equipe.
 - `notebooks/SistemaHierarquico(melhorado).ipynb` é o código da melhora no sistema do artigo escolhido pela nossa equipe.
 - `docs\Especificação_do_seminário_e_do_projeto.pdf` é o arquivo que descreve as especificações do projeto.
 - `docs\Seminário - Apresentação do artigo escolhido.pptx` é a apresentação do artigo escolhido, apresentação esta que foi feita em sala de aula.
 - `docs\Seminário - Melhoria do sistema.pdf` é a apresentação da melhoria do sistema, apresentação esta que foi feita em sala de aula.
 - `docs\Artigos\A_Novel_Multi-Stage_Approach_for_Hierarchical_Intrusion_Detection.pdf` é o artigo escolhido pela equipe.
 - `docs\Artigos\Uma Abordagem em Múltiplos Estágios para Detecção Hierárquica.docx.pdf` é o artigo feito pela equipe, que também é considerado como relatório do projeto de forma geral.
 - `requirements.txt` é um arquivo de texto com as bibliotecas externas e suas versões, requeridas para a realização e/ou reprodução do projeto.

## Resultados

Nossa equipe conseguiu uma melhora considerável no tempo de execução do sistema hierárquico, mantendo os resultados bem similares aos resultados do artigo original:

### Resultado do [artigo original](https://ieeexplore.ieee.org/document/10077796):
![Results_Original_Pred](https://github.com/luiz-linkezio/Deteccao_de_Intrusao_Hierarquica_Multiestagio/assets/125787137/4c17f40c-60aa-4cb0-a567-38e5e62f49ea)
![Results_Original_Time](https://github.com/luiz-linkezio/Deteccao_de_Intrusao_Hierarquica_Multiestagio/assets/125787137/98dcf131-1e44-4ab3-8472-c1be621f8639)


### Resultado da melhora realizada pela nossa equipe:
![Results_Improve_Pred](https://github.com/luiz-linkezio/Deteccao_de_Intrusao_Hierarquica_Multiestagio/assets/125787137/1793fad0-ffdc-49da-a97c-06bc24590e24)
![Results_Improve_Time](https://github.com/luiz-linkezio/Deteccao_de_Intrusao_Hierarquica_Multiestagio/assets/125787137/4a2e24dc-5ff0-41ad-9d49-d8177cb6814e)

## Autores

| [<img src="https://github.com/luiz-linkezio.png" width=115><br><sub>Luiz Henrique</sub><br>](https://github.com/luiz-linkezio) <sub>[Linkedin](https://www.linkedin.com/in/lhbas/)</sub> | [<img src="https://github.com/Raafm.png" width=115><br><sub>Rodrigo Abreu</sub><br>](https://github.com/Raafm) <sub>[Linkedin](https://www.linkedin.com/in/rodrigo-abreu-/)</sub> | [<img src="https://github.com/Rayhene.png" width=115><br><sub>Rayhene Ranúzia</sub><br>](https://github.com/Rayhene) <sub>[Linkedin](https://www.linkedin.com/in/rayhene/)</sub> |
| :-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: | :-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: | :-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: |
