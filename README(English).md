# Multi-Stage Hierarchical Intrusion Detection

Project for the Intrusion Detection course of the [Computer Engineering](https://portal.cin.ufpe.br/graduacao/#engenharia-da-computacao) undergraduation at [Centro de Informática (CIn)](https://portal.cin.ufpe.br/) of [Universidade Federal de Pernambuco (UFPE)](https://www.ufpe.br/), undertaken by the team from 2023 to 2024.

The course instructor provided some articles related to the use of artificial intelligence for security or security for AI-based systems. The students were divided into groups, and each group had to choose an article or propose to the instructor the selection of an article from outside those provided. After selecting the article, the group had to present a seminar on the article, replicate the article's experiment on the same dataset and also on another dataset. Additionally, the group could also attempt to make improvements to the article's system, and if successful, could create a paper and give a presentation demonstrating the improvement. For more information on the rules and requirements, please refer to the contents of the file `Especificação_do_seminário_e_do_projeto.pdf` in the `Docs` directory.

## Directory/File Organization

The directory:
 - `Artigos` contains the [base repository article](https://ieeexplore.ieee.org/document/10077796) and the article produced by our team.
 - `models` contains, in the `reproduction` folder, the models from the [base repository](https://gitlab.ilabt.imec.be/mverkerk/multi-stage-hierarchical-ids), and within the `melhorado` folder are the models made by our team to improve the system.
 - `Repositório_Base` contains the [base repository](https://gitlab.ilabt.imec.be/mverkerk/multi-stage-hierarchical-ids) of the article chosen by our team.
 - `data` contains the [dataset files](https://www.unb.ca/cic/datasets/) used.
 - `notebooks/utils` contains some [Python](https://www.python.org) files with functions that assist other files.
 - `notebooks/1º_Estágio(reprodução).ipynb` is the code for training, validating, and saving the model in the reproduction of the first stage.
 - `notebooks/1º_Estágio(melhorado).ipynb` is the code for training, validating, and saving the model in the enhancement of the first stage.
 - `notebooks/2º_Estágio(reprodução).ipynb` is the code for training, validating, and saving the model in the reproduction of the second stage.
 - `notebooks/2º_Estágio(melhorado).ipynb` is the code for training, validating, and saving the model in the enhancement of the second stage.
 - `notebooks/Tratamento_de_dados.ipynb` is the data preprocessing code.
 - `notebooks/SistemaHierarquico(reprodução).ipynb` is the code for reproducing the system from the article chosen by our team.
 - `notebooks/SistemaHierarquico(melhorado).ipynb` is the code for improving the system from the article chosen by our team.
 - `docs\Especificação_do_seminário_e_do_projeto.pdf` is the file describing the project specifications.
 - `docs\Seminário - Apresentação do artigo escolhido.pptx` is the presentation of the chosen article, which was presented in class.
 - `docs\Seminário - Melhoria do sistema.pdf` is the presentation of the system improvement, which was presented in class.
 - `docs\Artigos\A_Novel_Multi-Stage_Approach_for_Hierarchical_Intrusion_Detection.pdf` is the article chosen by the team.
 - `docs\Artigos\Uma Abordagem em Múltiplos Estágios para Detecção Hierárquica.docx.pdf` is the article produced by the team, also considered as a project report in general.
 - `requirements.txt` is a text file with the external libraries and their versions, required for the execution and/or reproduction of the project.

## Results

Our team achieved a considerable improvement in the execution time of the hierarchical system, while maintaining results very similar to those of the original article:

### Result of the [original article](https://ieeexplore.ieee.org/document/10077796):
![Results_Original_Pred](https://github.com/luiz-linkezio/Deteccao_de_Intrusao_Hierarquica_Multiestagio/assets/125787137/4c17f40c-60aa-4cb0-a567-38e5e62f49ea)
![Results_Original_Time](https://github.com/luiz-linkezio/Deteccao_de_Intrusao_Hierarquica_Multiestagio/assets/125787137/98dcf131-1e44-4ab3-8472-c1be621f8639)

### Result of the improvement made by our team:
![Results_Improve_Pred](https://github.com/luiz-linkezio/Deteccao_de_Intrusao_Hierarquica_Multiestagio/assets/125787137/1793fad0-ffdc-49da-a97c-06bc24590e24)
![Results_Improve_Time](https://github.com/luiz-linkezio/Deteccao_de_Intrusao_Hierarquica_Multiestagio/assets/125787137/4a2e24dc-5ff0-41ad-9d49-d8177cb6814e)

## Authors

| [<img src="https://github.com/luiz-linkezio.png" width=115><br><sub>Luiz Henrique</sub><br>](https://github.com/luiz-linkezio) <sub>[Linkedin](https://www.linkedin.com/in/lhbas/)</sub> | [<img src="https://github.com/Raafm.png" width=115><br><sub>Rodrigo Abreu</sub><br>](https://github.com/Raafm) <sub>[Linkedin](https://www.linkedin.com/in/rodrigo-abreu-/)</sub> |
| :-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: | :-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: |

