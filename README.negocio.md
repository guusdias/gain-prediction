## Domínio do Problema, Pergunta de Negócio e Objetivo do Modelo

### Domínio do problema

O projeto se insere no contexto de **desigualdade de renda** e **análise socioeconômica de indivíduos**. Governos, empresas e instituições financeiras precisam entender **quais características de uma pessoa** (idade, escolaridade, tipo de emprego, horas trabalhadas por semana, país de origem etc.) estão associadas a níveis mais altos de renda. Esse entendimento apoia decisões como:

- desenho de **políticas públicas** de inclusão e capacitação profissional;
- definição de **estratégias de crédito e marketing** (por exemplo, ofertas de produtos financeiros ou educacionais);
- planejamento de **recursos humanos** (identificar perfis mais propensos a atingir determinadas faixas salariais).

Para isso, utilizamos o dataset **Adult (Adult Income)**, que contém registros de indivíduos com diversas variáveis socioeconômicas e uma indicação se a renda anual é **maior que US$50.000** ou **menor/igual a US$50.000**.

### Pergunta de negócio

Com base nesse contexto, a pergunta de negócio que guia o projeto é:

> **“Dado o perfil socioeconômico de um indivíduo, conseguimos prever se a sua renda anual será maior que US$50.000?”**

Essa pergunta é **adequada para um problema de classificação binária**, pois a variável alvo assume dois valores possíveis (renda > US$50K ou renda ≤ US$50K). A resposta permite identificar quais fatores estão mais associados a rendas mais altas e utilizar essas informações em decisões de negócio e políticas públicas.

### Objetivo do modelo preditivo/classificador

O objetivo do modelo é:

- **Construir e avaliar um classificador binário** capaz de prever se um indivíduo pertence ao grupo de renda anual **> US$50K** ou **≤ US$50K** a partir de suas características socioeconômicas;
- **Comparar diferentes algoritmos de classificação** (por exemplo, Regressão Logística, Árvore de Decisão e Random Forest), utilizando pelo menos **três métricas de desempenho** (como acurácia, precisão, recall, F1-score);
- **Selecionar o melhor modelo** de acordo com o equilíbrio entre desempenho técnico (métricas) e **coerência com o objetivo de negócio**, discutindo trade-offs (por exemplo, priorizar recall ou precisão dependendo do uso do modelo);
- **Disponibilizar o modelo treinado** (deploy) de forma que possa ser reutilizado para fazer novas previsões fora do ambiente de desenvolvimento, salvando-o em arquivo (`modelo_final.pkl`) e demonstrando seu uso em novos exemplos.

Assim, o projeto atende simultaneamente às disciplinas de **Ciência de Dados** (definição clara de problema, pergunta e objetivos) e **Análise Preditiva** (foco em um modelo preditivo/classificador concreto, treinado e avaliado sobre um pipeline de dados bem definido).


