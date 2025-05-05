<h1>Relatório técnico do dataMartRH</h1>
<h2>Visão Geral do Projeto</h2>
<p>Este projeto tem como objetivo demonstrar uma arquitetura de pipeline de dados, utilizando tecnologias adotadas no mercado como Stored Procedures com PostgreSQL, Matplotlib e Apache Airflow. A solução visa facilitar o carregamento e processamento de dados tudo em um ambiente local e máquina virtual.</p>

<h2>Componentes da Arquitetura</h2>

<h3>1. dados na máquina virtual.</h3>
<ul>
  <li>Origem do arquivo no diretório /tmp.</li>
  <li>Ponto de partida para ingestão de dados no pipeline.</li>
</ul>

<h3>2. PostgreSQL</h3>
<ul>
  <li>passando os dados do arquivo csv para uma tabela temporária postgreSQL.</li>
  <li>Criação das Stored Procedures.</li>
</ul>

<h3>3. Matplotlib</h3>
<ul>
  <li>Usado para a visualização dos dados.</li>
</ul>

<h3>4. Apache Airflow</h3>
<ul>
  <li>Orquestrador de workflows.</li>
  <li>Apache Airflow na máquina real (Windows).</li>
</ul>

<h3>5. Google Colab</h3>
<ul>
  <li>Processamento do Matplotlib.</li>
</ul>
