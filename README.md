Lixo
====
Jogo educativo com o objetivo de incentivar as crianças a cuidar do meio
ambiente mostrando como eles devem participar nesse processo chamado
reciclagem. Para isso, o jogador deve limpar os locais, jogando os lixos em
suas respectivas lixeiras de reciclagem.

Membros Desenvolvedores
-----------------------
 - Andrés Mantecon Ribeiro Martano
 - Jairo Toshio Tuboi
 - Marcos Limeira
 - Matheus Lin Truglio Alvarenga
 - Thiago Kronig
 - André Badawi Missaglia
 - Caio Cesar Pinheiro Flores

Requisitos
----------
 - Sistema Operacional Windows/Linux
 - Bibliotecas (já incluídas no pacote):
	+ Python 3.1 ou superior ( http://www.python.org/download/ , baixar versão 3.x )
	+ pygame 1.9.1 ou superior( http://pygame.org/download.shtml )
 - Mouse

Como rodar
----------

	python central.py

Como gerar releases
-------------------

	python setup.py build


Instruções do Jogo
------------------
 - Clique com o botão esquerdo do mouse próximo aos lixos para pegá-los;
 - Leve o mouse até onde quer deixar o lixo e clique novamente para soltá-lo;
 - O lixo deve ser jogado na sua respectiva lixeira para que ela o engula; Lixos jogados em lixeiras erradas retornam ao ambiente, onde estavam.

Novas fases
-----------
As fases devem estar dentro da pasta /fases e devem seguir o padrão de 99FaseExemplo.xml

Relatório de Atualizações
-------------------------
 - Versão 0.1:
	- Lixos e lixeiras colocados na tela;
	- Lixos e lixeiras podem ser "agarrados" pelo mouse e movidos. Podem ser soltos pelo mouse, também;
	- Quando um lixo é solto tocando uma lixeira, o lixo volta para sua posição anterior (caso não seja da mesmo tipo) ou é engolido pela lixeira, que realiza uma animação de "engordar", caso sejam do mesmo tipo.

