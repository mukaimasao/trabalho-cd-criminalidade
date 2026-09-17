# Onde e quando patrulhar?
### Roteiro de apresentação — 15 minutos

Padrões espaciais e temporais da criminalidade no Rio Grande do Sul,
por município e mesorregião.

**Trabalho Final de Ciência de Dados — Tema 6** · UNESP / FC Bauru
**Apresentadores:** Mário Masao Mukai e Davi Ferreira de Souza

---

12 slides, 13:25 no total. A "fala" é para falar, não para pôr no slide; o
slide leva só a imagem e as linhas marcadas. [A] e [B] marcam quem fala, com a
troca no slide 5. Os slides 2, 6, 8 e 9 são os que sustentam o argumento; se
atrasar, encurte o 4 e o 10.

---

## Slide 1 — Capa (0:00 – 0:30) **[A]**

**No slide**
> **Onde e quando patrulhar?**
> Padrões espaciais e temporais da criminalidade no RS (2022–2025)
> Mário Masao Mukai · Davi Ferreira de Souza — Tema 6

**Imagem:** `figuras/f8_mapa_mesorregioes.png` clara, ao fundo. Ou capa limpa.

**Fala**
> Boa tarde. Nosso trabalho parte de uma pergunta concreta de gestão pública: uma
> secretaria de segurança tem efetivo limitado e um estado inteiro para cobrir.
> Onde ela coloca a viatura, e em que horário? Fomos responder isso com dado
> aberto, para o Rio Grande do Sul, de 2022 a 2025.

---

## Slide 2 — O problema real (0:30 – 1:40) ★

**Imagem:** `figuras/f9_volume_vs_taxa.png`
*(os 10 maiores municípios por volume bruto contra os 10 maiores por taxa, entre
os de 50 mil+ hab.; em laranja quem aparece só de um lado)*

**No slide**
> 497 municípios, efetivo finito
> O critério usual é o **volume bruto** — que mede o tamanho da cidade, não o risco

**Fala**
> Essa figura é o trabalho inteiro em um slide. À esquerda, os dez maiores
> municípios por volume bruto de ocorrências, que é o critério usual quando não
> há evidência orientando. À direita, os dez maiores por taxa por habitante.
> Só municípios de 50 mil habitantes ou mais, para serem comparáveis.
>
> Das dez cidades da esquerda, **só três aparecem na direita**: Porto Alegre,
> Canoas e Santa Maria. As sete em laranja saem da lista. E entram sete outras,
> como Tramandaí, Vacaria, Cruz Alta e Santo Ângelo, que por volume nunca
> entrariam na conversa. Porto Alegre ainda cai de primeiro para quarto.
>
> Trocar o critério troca sete dos dez nomes. O volume bruto favorece
> automaticamente a cidade grande, onde há mais gente e portanto mais registro,
> sem dizer nada sobre o risco que o cidadão enfrenta nem sobre quando o crime
> acontece. É essa lacuna que fomos preencher.

---

## Slide 3 — A pergunta central (1:40 – 2:30)

**No slide**
> **No RS, os tipos de ocorrência têm padrão espacial (município/mesorregião) e
> temporal (dia, horário) identificável, a ponto de justificar a priorização de
> recursos por região e turno?**
>
> RS inteiro · 2022–2025 · por município · agrupado em mesorregião

**Imagem:** nenhuma.

**Fala**
> Essa é a pergunta, já ajustada para ser acionável por um órgão estadual.
>
> Uma escolha que vale explicar, porque é um desvio do enunciado: o Tema 6 fala
> em bairros, e nós subimos para município. Tentamos bairro — a auditoria da
> fusão de grafias está no repositório. Dois problemas mataram: o campo é de
> preenchimento livre, sem padrão entre delegacias, e não existe população por
> bairro no Censo. Sem denominador, a análise por bairro só produz contagem
> bruta, que é exatamente o critério que o slide anterior acabou de derrubar.
>
> No município a gente tem população, tem mesorregião, e é a unidade sobre a qual
> a SSP-RS de fato decide.

---

## Slide 4 — Dados e preparação (2:30 – 3:50) **[A]**

**Imagem:** `figuras/f10_composicao_macro.png`
*(participação de cada macrocategoria; em azul as 9 que formam os crimes de rua)*

**No slide**
> **SSP-RS** 2022–2025 → **3.117.592** ocorrências · **IBGE** Censo 2022 + mesorregiões
> 314 tipos de enquadramento → **18 macrocategorias** → **33,4% "crimes de rua"**
> Taxa média anual por 100 mil hab. = ocorrências ÷ população ÷ 4 anos × 100.000

**Fala**
> Duas fontes públicas, sem dado pessoal. Da SSP-RS vieram os microdados: cada
> linha é uma ocorrência, com data, hora, tipo e município. 3,1 milhões de
> registros. Do IBGE vieram as duas coisas que a SSP não tem: população por
> município, pelo Censo de 2022, e a mesorregião de cada um.
>
> O pipeline remove duplicata, deriva os atributos temporais — inclusive o turno,
> que é a hora cortada em quatro faixas — faz o join com o IBGE e agrupa os 314
> tipos de enquadramento em 18 macrocategorias.
>
> Aí veio a decisão que essa figura mostra: marcamos os **crimes de rua**, que é o
> azul, as categorias sensíveis a patrulhamento ostensivo. Olhem o cinza no topo:
> ameaça e violência doméstica, 17,6%; fraude, 17,2%. Isso é registrado na
> delegacia, mas não depende de onde a viatura está. Sobram nove categorias,
> 33,4%, cerca de 1 milhão de registros.
>
> A métrica de comparação é a taxa média anual por 100 mil habitantes. A divisão
> pelo número de anos não é detalhe: sem ela o numerador soma quatro anos e o
> denominador é a população de um ano só.

---

## Slide 5 — Cada crime tem sua hora (3:50 – 4:50) **[B]**

**Imagem:** `figuras/f2_perfil_horario_por_tipo.png`

**No slide**
> Furto comum: **de dia** · Roubo e lesão: **à noite** · Arrombamento: **madrugada**
> Muda não só *quanto* crime, mas *que tipo* de crime

**Fala**
> Vamos ao tempo. Cada linha aqui é uma macrocategoria, e a curva mostra como as
> ocorrências daquele tipo se distribuem nas 24 horas, normalizadas para tipos de
> volume diferente caberem no mesmo gráfico.
>
> As curvas não são iguais, e é esse o ponto. O furto comum é diurno: sobe de
> manhã, fica alto à tarde, praticamente some de madrugada. Roubo e lesão fazem o
> caminho oposto, subindo à noite.
>
> Isso muda a recomendação. Se todos os crimes tivessem o mesmo perfil, bastaria
> escalar mais gente no pico. Como o perfil muda, o que muda de turno para turno
> não é só o volume, é a composição — e tipo diferente pede policiamento
> diferente. Guardem essa figura, porque o teste daqui a pouco é sobre ela.

---

## Slide 6 — Onde a taxa é maior (4:50 – 5:50) ★

**Imagem (duas colunas):** `figuras/f3_taxa_municipio.png` à esquerda,
`figuras/f3b_taxa_municipio_grandes.png` à direita

**No slide**
> Top 15 bruto: 8 dos 15 são litorâneos, e há cidades de 3 mil habitantes
> Controlando o porte (≥ 50 mil hab.): **Tramandaí, Capão da Canoa, Vacaria, Porto Alegre, Cruz Alta**

**Fala**
> Agora o espaço. À esquerda, os 15 municípios de maior taxa. Duas coisas
> chamam a atenção: oito dos quinze são litorâneos, e aparecem cidades muito
> pequenas, como Esmeralda, com três mil habitantes. Os dois casos são artefatos,
> e eu volto neles nas limitações.
>
> Por isso o gráfico da direita: a mesma taxa, só entre municípios de 50 mil
> habitantes ou mais, o que estabiliza o denominador. Tramandaí e Capão da Canoa
> continuam no topo, mas aparecem Vacaria e Cruz Alta, cidades do interior sem
> praia nenhuma, ao lado de Porto Alegre.
>
> A leitura é essa: taxa alta não é exclusividade da capital nem do litoral. Por
> volume, Vacaria e Cruz Alta nunca entrariam na conversa, e elas têm risco por
> habitante maior que o de Caxias do Sul.

---

## Slide 7 — O mapa (5:50 – 6:40)

**Imagem:** `figuras/f8_mapa_mesorregioes.png`

**No slide**
> Metropolitana de POA ≈ **8.000** /100 mil/ano → Centro Oriental ≈ **5.900**
> (taxa ponderada pela população da região)

**Fala**
> Subindo um nível: as sete mesorregiões do IBGE, com a taxa ponderada pela
> população de cada uma. A malha veio da API de malhas do IBGE.
>
> A mancha mais escura é a Metropolitana de Porto Alegre, no leste, junto com o
> Centro Ocidental. A mais clara é o Centro Oriental, com cerca de 5.900 contra
> os 8.000 da Metropolitana — quase um terço de diferença.
>
> Só que essa é a taxa **ponderada**, que trata a região como um bloco e é puxada
> pelas cidades grandes dela. Quando eu chegar nos testes, vou mostrar que
> olhando município a município a ordem muda. Guardem isso.

---

## Slide 8 — O pico é a noite em todo o estado (6:40 – 8:00) ★

**Imagem:** `figuras/f7_turno_mesorregiao.png`

**No slide**
> Noite é o turno de pico nas 7 mesorregiões
> Margem sobre a tarde: **1 ponto** na Metropolitana e no Nordeste, 3 a 5 nas demais
> A diferença regional clara está na madrugada: **21%** no interior vs. **15%** na Metropolitana

**Fala**
> Esse slide cruza as duas dimensões e é o que mais simplifica a decisão. Cada
> linha é uma mesorregião, cada coluna um turno, e o número é o percentual dos
> crimes de rua daquela região que caem naquele turno.
>
> A noite é o turno de maior concentração nas sete regiões, sem exceção. O padrão
> temporal é estável no estado inteiro, então o reforço noturno não precisa de
> política diferente por região.
>
> Mas quero ser honesto sobre a margem. Na Metropolitana é 31% na noite contra
> 30% na tarde. Um ponto. No Nordeste, a mesma coisa. Nas outras cinco a folga é
> de 3 a 5 pontos. Então a leitura correta não é "a noite domina": é que noite e
> tarde formam um bloco contínuo de maior atividade, e a noite fica na ponta dele
> em todas as regiões.
>
> A diferença regional que é de fato nítida está na madrugada: 21% no Sudoeste,
> no Sudeste e no Centro Ocidental, contra 15% na Metropolitana. O pico é igual
> no estado todo; o segundo turno crítico é que muda.

---

## Slide 9 — Os testes de hipótese (8:00 – 9:55) ★

**Imagem:** `figuras/f5_residuos_chi2.png`

**No slide**
> | Teste | Estatística | p | Efeito |
> |---|---|---|---|
> | χ² macro × turno | 40.607 (gl 24) | ≈ 0 | V = 0,11 |
> | χ² macro × mesorregião | 50.368 (gl 48) | ≈ 0 | V = 0,09 |
> | Kruskal-Wallis taxa municipal | H = 30,3 (gl 6) | 3,4×10⁻⁵ | η² = 0,05 |
>
> Premissas da ANOVA falham (Shapiro-Wilk p ≈ 5×10⁻¹¹, Levene p = 0,004) → Kruskal-Wallis

**Fala**
> O qui-quadrado entre macrocategoria e turno rejeita a independência: 40.607,
> 24 graus de liberdade, p praticamente zero. O tipo de ocorrência não é
> independente do turno.
>
> Mas quero ser honesto sobre esse p. Com 3,1 milhões de registros a
> significância é garantida. Por isso reportamos o **V de Cramér**: 0,11.
> Associação real, porém modesta — o turno molda *que tipo* de crime acontece,
> não *se* haverá crime.
>
> O que interessa é o padrão, nessa figura: os resíduos padronizados. Vermelho
> ocorre mais que o esperado sob independência, azul menos. Arrombamento na
> **madrugada**, furto comum de **manhã e tarde**, roubo e lesão à **noite**. E o
> azul conta a mesma história pelo avesso: o furto comum some à noite.
>
> Sobre o Kruskal-Wallis, duas coisas. Por que ele e não ANOVA: testamos as
> premissas e as duas falham. Shapiro-Wilk rejeita a normalidade, em quatro das
> sete regiões; Levene rejeita a homogeneidade das variâncias.
>
> E o ponto mais delicado do trabalho: o Kruskal-Wallis compara municípios, cada
> um valendo um, e **não** é a mesma coisa que o mapa anterior. Pela taxa
> ponderada a Metropolitana lidera; pela mediana municipal ela cai para
> **terceira**, porque junta 98 municípios muito desiguais. E o tamanho de efeito
> fecha o argumento: **eta quadrado de 0,05**. A mesorregião explica 5% da
> variação entre municípios; os outros 95% estão *dentro* das regiões.

---

## Slide 10 — Sazonalidade: o efeito do veraneio (9:55 – 10:50)

**Imagem:** `figuras/f6_sazonalidade_litoral.png`

**No slide**
> Litoral em janeiro: **12,5%** de suas ocorrências · resto do estado: 8,6%
> Não é alta permanente — é **sazonal**

**Fala**
> Falta explicar o litoral, que dominou o ranking do slide 6. A hipótese óbvia era
> população flutuante, e dá para testar com o próprio dado.
>
> A linha azul é o resto do estado: praticamente plano, entre 8 e 9% em cada mês.
> A laranja é o litoral, que salta para **12,5% das suas ocorrências em janeiro**
> contra 8,6% no resto, com segundo pico em dezembro.
>
> Coincide com a temporada de veraneio, quando a população presente é muito maior
> que a residente, que é o nosso denominador. A taxa anual do litoral é inflada
> por construção. A consequência prática é boa: o litoral não é prioridade
> permanente, é reforço concentrado no verão.

---

## Slide 11 — Limitações (10:50 – 12:00)

**Imagem:** `figuras/f11_taxa_vs_populacao.png`
*(dispersão taxa × população, escala log, os 497 municípios)*

**No slide**
> 1. Ocorrência **registrada** ≠ crime real (subnotificação desigual)
> 2. População **residente**, não presente
> 3. Municípios pequenos: taxa instável
> 4. Macrocategorias são nossas; `OUTROS` retém 13% dos registros
> 5. Recorte RS 2022–2025

**Fala**
> Cinco limitações, e elas são honestas, não protocolares.
>
> A mais séria: o dado mede ocorrência **registrada**, não crime real. A
> subnotificação varia por tipo e por região, então parte do padrão espacial pode
> ser diferença na propensão a registrar.
>
> A segunda e a terceira estão nessa dispersão: cada ponto é um município,
> população em escala log. À esquerda o leque vai de 2 mil a 11 mil; conforme a
> população cresce, a nuvem se fecha. Esmeralda, no alto à esquerda, tem 3.195
> habitantes e ficou em quinto no ranking bruto. Foi para isso que cortamos em 50
> mil, a linha tracejada. E os triângulos laranja, os municípios de veraneio,
> ocupam quase todo o topo.
>
> A quarta: as 18 macrocategorias são classificação nossa, e `OUTROS` ficou com
> 13% dos registros. A quinta: o recorte é o RS de 2022 a 2025.

---

## Slide 12 — Conclusão e recomendação (12:00 – 13:25) **[A]**

**No slide**
> **Existe padrão, e ele é acionável.**
> **Uniforme no pico:** reforço noturno em todo o estado
> **Diferenciado na composição:** noite → roubo/lesão nos centros urbanos ·
> madrugada → arrombamento, com peso maior no interior
> **Priorizar município a município pela taxa/habitante** — não por região, não por volume
> **Litoral:** reforço sazonal no verão

**Imagem:** montagem pequena com `f2`, `f7` e `f3b` lado a lado.

**Fala**
> Fechando. A criminalidade no RS não se distribui ao acaso, nem no tempo nem no
> espaço.
>
> No tempo, o tipo de ocorrência depende do turno, com padrão nítido:
> arrombamento de madrugada, furto de dia, roubo e lesão à noite. No espaço, a
> taxa difere entre mesorregiões, mas de forma fraca: a região explica só 5% da
> variação. E o cruzamento simplifica: o pico é a noite em todas.
>
> Portanto, a recomendação para a SSP-RS é uma escala **uniforme quanto ao pico**,
> com reforço noturno no estado inteiro, e **diferenciada quanto à composição**:
> patrulhamento noturno contra roubo e lesão nos centros urbanos, vigilância de
> madrugada contra arrombamento, com peso maior no interior.
>
> Entre cidades, o critério é a taxa por habitante, e a priorização deve ser
> **município a município, não por região** — porque, com a região explicando só
> 5% da variação, tratar uma mesorregião inteira como prioritária desperdiça
> efetivo nos municípios de taxa baixa dela.
>
> Com a ressalva de que o dado é de ocorrência registrada; de que o litoral
> parece de alto risco permanente quando seu problema é sazonal; e de que a
> associação encontrada, embora real, é modesta. Ela deve orientar a alocação,
> não substituir o conhecimento operacional de cada comando regional. Obrigado.

---

## Slides de reserva (depois do "obrigado", só se perguntarem)

Deixe estes no fim do arquivo, sem numeração e sem entrar no tempo. Não passe
por eles na apresentação: abra só se a pergunta pedir.

| Reserva | Arquivo | Quando abrir |
|---|---|---|
| **Heatmap dia × hora** | `figuras/f1_heatmap_dia_hora.png` | "e o padrão da semana?" / "o fim de semana é diferente?" — mostra a madrugada de sábado e domingo carregada |
| **Barras por mesorregião** | `figuras/f4_taxa_mesorregiao.png` | se pedirem os números exatos por região, em vez do mapa |
| **Tabela 2 do relatório** | print da tabela | se perguntarem sobre ponderada × mediana; tem as duas colunas lado a lado |
| **Composição das macrocategorias** | `figuras/f10_composicao_macro.png` | já é o slide 4, mas volte a ele se perguntarem "o que é crime de rua?" |

O heatmap é o mais provável de ser cobrado: é a única figura do relatório que
não aparece na apresentação, e o padrão de fim de semana só está nele.

## Perguntas prováveis

| Pergunta | Resposta curta |
|---|---|
| "A Metropolitana é primeira no mapa e terceira na mediana. Qual está certa?" | As duas. A ponderada responde quanto efetivo a região inteira precisa, porque efetivo atende pessoas. A mediana responde se o município típico dali corre mais risco. O teste usa a segunda. |
| "Por que não regressão ou modelo preditivo?" | A pergunta é de associação entre categóricas e de comparação entre grupos, não de previsão. Consideramos Poisson com população como offset, mas exigiria covariáveis municipais fora do recorte e responderia a uma pergunta de causa que o Tema 6 não faz. |
| "Por que Kruskal-Wallis e não ANOVA?" | Testamos as premissas: Shapiro-Wilk rejeita normalidade (p ≈ 5×10⁻¹¹, e em 4 das 7 regiões), Levene rejeita variâncias homogêneas (p = 0,004). |
| "Por que χ² e não teste G?" | Equivalentes nesse regime de amostra. Ficamos com o χ² pela leitura direta dos resíduos padronizados, que é o que interpretamos. A menor frequência esperada está na ordem de centenas, muito acima do mínimo de 5. |
| "O que é V de Cramér? E η²?" | Tamanhos de efeito. V mede associação em tabela de contingência (0,11 = fraca). η² = 0,05 é a fração da variação nos postos explicada pela região. São o antídoto contra p-valor inflado por amostra gigante. |
| "Vocês não olharam bairro, que era o tema." | Tentamos; a auditoria da fusão de grafias está no repo. O campo é livre e não há população por bairro no Censo, ou seja, sem denominador para taxa. Está justificado na Seção 3.6 do relatório. |
| "Como trataram nomes de município?" | Normalização (maiúsculas, sem acento/pontuação) + dicionário de 4 correções, tipo Sant'Ana do Livramento. Cobertura integral dos registros. |
| "Por que 2022 como início?" | É o ano do Censo, que dá o denominador. |

---

## Antes de apresentar

- Cronometrar uma vez inteiro. Alvo 13:25, teto 15:00.
- Rodar `python src/figuras_extra.py` para gerar F9, F10 e F11.
- Testar o mapa (F8) e os resíduos (F5) no projetor; as cores claras somem em
  sala clara.
- Combinar quem responde o quê nas perguntas.
