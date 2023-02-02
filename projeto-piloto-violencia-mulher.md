# Projeto-piloto de abertura dos Dados de Violência contra a Mulher

## Ideia

Chamada para adesão à preparação e publicação de base já disponibilizada (semiestruturada) no site da SEJUSP, no bojo dos projeto-piloto de abertura no Portal de Dados Abertos (PdA), como fizemos com FHEMIG e SEJUSP

## Vinculação com Planejamento Estratégico da CGE

- Incremento da transparência ativa (Diretriz: _Promover melhora na gestão pública por meio de elevado grau de transparência ativa **nas secretarias e vinculadas** e menor necessidade de busca por transparência passiva_); articulação com planos de Integridade das SEJUSP/PCMG e fomento ao controle social 

- Aumento do número de conjunto de dados publicados no PdA: [Estratégia de Tecnologia de Informação e Comunicação do Estado](https://www.mg.gov.br/sites/default/files/planejamento/documentos/gestao-governamental/gestao-de-ti/estrategia_2021_-_consulta_gestores_de_tic_0.pdf), que prevê uma diretriz de implantar 10 novos conjuntos de dados no Portal de Dados Abertos (EIXO 7 - ACESSO À INFORMAÇÃO, PARTICIPAÇÃO E CONTROLE
SOCIAL - PROMOVER A TRANSPARÊNCIA, INCLUSÃO DIGITAL E AS SOLUÇÕES QUE APROXIMEM O ESTADO AO CIDADÃO).

## Contexto/Justificativa

- Publicação recente de [conjunto de Crimes Violentos no PdA](https://dados.mg.gov.br/dataset/crimes-violentos)

- [Divulgação de MG como estado mais seguro do Brasil](http://www.seguranca.mg.gov.br/component/gmg/story/4081-minas-e-o-estado-mais-seguro-do-brasil-segundo-ministerio-da-justica)

- Possibilidade de articulação de campanha governamental focada na segurança da mulher e outras políticas públicas associadas; protagonismo feminino; sororidade

- Dado já publicado em formato semiestruturado e com periodicidade de atualização definida

- Experiência da DCTA em auxiliar na publicação/atualização com ferramentas automatizadas (vide exemplos dos conjuntos: Acordo Vale, Doações, Termo de Parceria, Crimes Violentos)  

# Acessibilidade

Os dados estão disponibilizados num link no rodapé da página em http://www.seguranca.mg.gov.br/2018-08-22-13-39-06/dados-abertos. Baixas visibilidade e findability/discoverability

# Atualização

Os dados tabulares estão atualizados, até dezembro de 2022: 
- [Violência Doméstica e Familiar](http://www.seguranca.mg.gov.br/images/2023/Janeiro/Modelo_Sesp_Violencia%20Domestica%20e%20Familiar%20contra%20a%20Mulher.Jan20_Dez22.xlsx)
- [Vítimas de Feminicídios](http://www.seguranca.mg.gov.br/images/2023/Janeiro/Modelo_Sesp_Feminicdio.Jan20_Dez22.xlsx)

O [último relatório (diagnóstico)](http://www.seguranca.mg.gov.br/images/2021/Setembro/DIAGNSTICO%20-%20VDFCM%20nas%20RISPs%20-%201%20semestre-2021%20-%202021-08-06%201.pdf) data do primeiro semestre de 2021, disponível em http://www.seguranca.mg.gov.br/component/gmg/page/3118-violencia-contra-a-mulher.

# Formato

Os dados tabulares supracitados estão semiestruturados (contidos em abas de arquivos em excel) e, portanto, relativamente fácies de serem preparados e publicados em formato aberto (csv) no PdA (como o conjunto de Crimes Violentos). Temos scripts para fazer a conversão em cada atualização de forma automatizada (mensalmente, p. ex.). Bastaria a pactuação e documentação inicial (leiaute e descrição das colunas dos 2 arquivos)  

# Publicador

Os dados estão na página da SEJUSP, mas a autoria é da Superintendência de Informações e Inteligência da Polícia Civil

# Operacionalização

- Uso do pacote pandas do Python associado com o dataset template (ferramenta 'actions' no repositório Github) fará:
	- leitura da aba dos dados de violência doméstica e feminícídio,
	- conversão para formato aberto/csv, 
	- validação com dicionário de dados e 
	- publicação, na periodicidade definida pelo publicador

- Requisitos: será necessário
	- pactuação do leiaute (colunas, formatos) dos arquivos/tabelas;
	- elaboração do dicionário de dados
	- formulário no SEI de solicitação de cadastro de usuário da pessoa responsável pela publicação na PCMG

## Benefícios

- Maior visibilidade, acessibilidade e reuso dos dados já publicados

- Possibilidade de aplicação do template para outros fins nos ciclos de dados dos órgãos parceiros

- Fortalecimento da parceria com SEJUSP

- Fomento ao controle social

- Feedbacks para aprimoramento das políticas públicas associadas

## Possibilidades

- Agregaçao de paineis contendo gráficos e mapas dos relatórios (exemplos: IDE SISEMA, hotsite coronavirus SES)
