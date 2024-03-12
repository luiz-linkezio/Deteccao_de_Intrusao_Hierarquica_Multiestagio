# Detecção de Intrusão Hierárquica Multiestágio

Projeto da cadeira de Detecção de Intrusão do curso de [Engenharia da Computação (EC)](https://portal.cin.ufpe.br/graduacao/#engenharia-da-computacao) do [Centro de Informática (CIN)](https://portal.cin.ufpe.br/) da [Universidade Federal de Pernambuco (UFPE)](https://www.ufpe.br/), cadeira cursada pela equipe, de 2023 a 2024. 

O professor da cadeira disponibilizou alguns artigos relacionados ao uso de inteligência artificial para segurança ou à segurança para sistemas baseados em inteligência artificial, os alunos foram divididos em grupos e cada grupo tinha que escolher um artigo ou propor ao professor a escolha de um artigo de fora dos disponibilizados pelo professor. Após a escolha do artigo, o grupo tinha que apresentar um seminário sobre o artigo, reproduzir o experimento do artigo no mesmo conjunto de dados e também em outro conjunto de dados, além disso, o grupo também poderia tentar realizar melhorias no sistema do artigo escolhido, e se obtivesse sucesso, poderia criar um artigo e realizar uma apresentação demonstrando a melhora. Para mais informações sobre as regras e requisitos, verifique o conteúdo do arquivo `Especificação_do_seminário_e_do_projeto.pdf`.

## Organização de Diretórios/Arquivos

O diretório:
 - `Artigos` contém o artigo do repositório base e o artigo feito por nossa equipe.
 - `Models` contém os modelos do repositório base, e dentro da pasta `melhorado` estão os modelos feitos pela nossa equipe.
 - `Repositório Base` contém o repositório base do artigo escolhido pela nossa equipe.
 - `data` contém os arquivos de conjunto de dados usados.
 - `utils` contém alguns arquivos [python](https://www.python.org) com funções que auxiliam os arquivos principais.
 - `1º_Estágio(reprodução).ipynb` é o treino, validação e salvamento do modelo na reprodução do primeiro estágio.
 - `1º_Estágio(melhorado).ipynb` é o treino, validação e salvamento do modelo na melhora do primeiro estágio.
 - `2º_Estágio(reprodução).ipynb` é o treino, validação e salvamento do modelo na reprodução do segundo estágio.
 - `2º_Estágio(melhorado).ipynb` é o treino, validação e salvamento do modelo na melhora do segundo estágio.
 - `Especificação_do_seminário_e_do_projeto.pdf` é o arquivo que descreve as especificações do projeto.
 - `Tratamento_de_dados(reprodução).ipynb` é o tratamento de dados da reprodução.
 - `Tratamento_de_dados(melhorado).ipynb` é o tratamendo de dados da melhora.
 - `SistemaHierarquico(reprodução).ipynb` é a reprodução do sistema escolhido pela nossa equipe.
 - `SistemaHierarquico(melhorado).ipynb` é a melhora no sistema do artigo escolhido pela nossa equipe.

Para obter o arquivo do conjunto de dados `cic_ids_2017`, pelo fato do arquivo ser muito grande, será necessário o uso do [Git Large File Storage (LFS)](https://git-lfs.com), que é uma extensão do Git que facilita o gerenciamento de arquivos grandes em repositórios Git, ele permite armazenar arquivos grandes fora do repositório principal do Git, reduzindo assim o tamanho do repositório e melhorando a eficiência do versionamento. Para utilizar esta ferramenta, siga os seguintes passos:
- Baixe e instale o Git LFS através deste link: https://git-lfs.com
- Clone o repositório com o comando: `git clone git@github.com:luiz-linkezio/Deteccao_de_Intrusao_Hierarquica_Multiestagio.git`
- Use o comando: `git lfs pull`

## Resultados

Nossa equipe conseguiu uma melhora considerável no tempo de execução do sistema hierárquico, mantendo os resultados bem similares aos resultados do artigo original:

### Resultado do artigo original:
![Imagem do WhatsApp de 2024-03-11 à(s) 21 19 15_396c5c5c](https://github.com/luiz-linkezio/Deteccao_de_Intrusao_Hierarquica_Multiestagio/assets/125787137/4c17f40c-60aa-4cb0-a567-38e5e62f49ea)
![Imagem do WhatsApp de 2024-03-11 à(s) 21 19 24_ddeec412](https://github.com/luiz-linkezio/Deteccao_de_Intrusao_Hierarquica_Multiestagio/assets/125787137/98dcf131-1e44-4ab3-8472-c1be621f8639)


### Resultado da melhora realizada pela nossa equipe:
![Imagem do WhatsApp de 2024-03-11 à(s) 21 19 38_fadcc23e](https://github.com/luiz-linkezio/Deteccao_de_Intrusao_Hierarquica_Multiestagio/assets/125787137/1793fad0-ffdc-49da-a97c-06bc24590e24)
![Imagem do WhatsApp de 2024-03-11 à(s) 21 20 01_eccfba28](https://github.com/luiz-linkezio/Deteccao_de_Intrusao_Hierarquica_Multiestagio/assets/125787137/4a2e24dc-5ff0-41ad-9d49-d8177cb6814e)


## Links

Conjunto de dados: https://www.unb.ca/cic/datasets/

Repositório Base: https://gitlab.ilabt.imec.be/mverkerk/multi-stage-hierarchical-ids

Artigo escolhido: https://ieeexplore.ieee.org/document/10077796

Git Large File Storage (LFS): https://git-lfs.com

Python: https://www.python.org

Jupyter Notebook: https://jupyter.org

Centro de Informática (CIN): https://portal.cin.ufpe.br/

Site da graduação em Engenharia da Computação (EC): https://portal.cin.ufpe.br/graduacao/#engenharia-da-computacao

Universidade Federal de Pernambuco (UFPE): https://www.ufpe.br

## Autores

| [<img src="https://github.com/luiz-linkezio.png" width=115><br><sub>Luiz Henrique</sub><br>](https://github.com/luiz-linkezio) <sub>[Linkedin](https://www.linkedin.com/in/lhbas/)</sub> | [<img src="https://github.com/Raafm.png" width=115><br><sub>Rodrigo Abreu</sub><br>](https://github.com/Raafm) <sub>[Linkedin](https://www.linkedin.com/in/rodrigo-abreu-/)</sub> | [<img src="https://github.com/Rayhene.png" width=115><br><sub>Rayhene Ranúzia</sub><br>](https://github.com/Rayhene) <sub>[Linkedin](https://www.linkedin.com/in/rayhene/)</sub> |
| :-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: | :-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: | :-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: |
