# Projeto PAC-7

# Rent prediction
O projeto tem como objetivo utilizar aprendizagem de máquina para que seja possível prever possíveis valores de imóveis da cidade de Joinville utilizando caracteristicas como localização, m² e quantidade de quartos. A partir da previsão feita, o usuário terá uma base do valor dos imóveis com as devidas características informadas

# Relevância
A relevância deste projeto é apresentar para o usuário uma previsão do valor aproximado dos imóveis disponíveis para compra com base nas características informadas, a previsão irá contribuir com a organização das pessoas para que visualizem de maneira rápida e fácil se o imóvel em que ele estava pensando é cabível em suas despesas ou não. Além disso o algoritmo tem como objetivo se manter sempre atualizado com base em novos valores inseridos nas principais imobiliárias, fazendo com que sempre traga uma média aproximada do valor real.

# Requisitos do protótipo
Para efetivação desta proposta, iremos utilizar a técnica de raspagem para coletar os dados de imóveis das regiões desejadas, assim como limpar dados "sujos", após isso iremos treinar a máquina para que consiga fazer previsões com base no dataset coletado

# Funcionalidades do projeto
- Página principal: Irá apresentar campos para informar a quantidade de quartos e m², após inserir os dados e realizar a busca, o sistema irá informar o valor aproximado da compra.
- Aprendizado de máquina: Irá analisar os dados coletados e realizar uma previsão de preço de acordo com os dados.
- Pré-processamento de Dados: analisará os dados coletados para garantir que estejam prontos para a modelagem.
- Modelagem: treinará e avaliará modelos de aprendizado de máquina em relação aos dados históricos.

# Técnicas e Tecnologias
- Back-end - Python
- Front-end - HTML/CSS e javascript
- Data Scraping
- Bibliotecas
   - CORS - Mecanismo que permite que recursos restritos em uma página da web sejam recuperados por outro domínio.
   - request - Permite fazer requests http usando o python.
   - jsonify - Manipulação de json.
   - Re - Expressões regulares para o tratamento dos dados.
   - Flask - Fornece as ferramentas básicas para criar aplicações web, como gerenciamento de rotas e requisições HTTP
   - BeaultifulSoup4 - Manipular HTML/XML para a raspagem dos dados.
   - Pandas - Datasets.
   - Sklearn - Machine learning

# Critérios escolhidos
- Documentação - 20%
- Estruturas de engenharia - 25%    
- Apresentação - 25%

# Resultado scraping
![image](https://user-images.githubusercontent.com/61556272/236065414-aff3288d-0528-4065-87c8-9c8b0c6e4cf8.png)

# Equipe
- Frederico Stein &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <a href="https://www.linkedin.com/in/frederico-bernardes-wust-stein-052bbb1a9/" target="_blank"><img src="https://img.shields.io/badge/-LinkedIn-%230077B5?style=for-the-badge&logo=linkedin&logoColor=white" target="_blank" width="80" height="20"></a>
- Leonardo Rodrigues &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  <a href="https://www.linkedin.com/in/leonardo-rodrigues-0a2043217/" target="_blank"><img src="https://img.shields.io/badge/-LinkedIn-%230077B5?style=for-the-badge&logo=linkedin&logoColor=white" target="_blank" width="80" height="20"></a>
- Matheus Tambosi &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <a href="https://www.linkedin.com/in/matheus-tambosi-a40b62196/" target="_blank"><img src="https://img.shields.io/badge/-LinkedIn-%230077B5?style=for-the-badge&logo=linkedin&logoColor=white" target="_blank" width="80" height="20"></a>
- Vitor Adriel &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <a href="https://www.linkedin.com/in/vitor-adriel-roecker-8571a11b0/" target="_blank"><img src="https://img.shields.io/badge/-LinkedIn-%230077B5?style=for-the-badge&logo=linkedin&logoColor=white" target="_blank" width="80" height="20"></a>
