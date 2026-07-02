# Entrevista de Descoberta : As cinco perguntas


> O stakeholder dificimente chega com o problema. Ele chega com a solução que imagina. Seu trabalho é fazer a viagem de volta . 


**1. Qual é o comportamento atual que você quer mudar ?**
> ancora no presente e não no que devia existir

**2. O que acontece por causa disso ?**
> revela a consequência real, o impacto e o motivo do projeto

**3. Como você saberia que o problema foi resolvido?** 
> descobre a métrica

**4. Algo já foi tentado antes ? O que aconteceu ?**
> revela restrições ocultas e evita repetição de erros

**5. O que você não quer que aconteça ?**
> define o fora de escopo, restrições do projeto


*** 




> Se o stakeholder não consegue responder a pergunta 3, a métrica do PRD vai ser inventada e não descoberta.

***
# Como documentar a entrevista

| Campo | O que resgistrar |
|---|---|
| O que foi dito | Frase literal do stakeholder|
| O que eu interpretei| Sua leitura que foi dito |
| Perguntas em aberto| O que ainda precisa ser respondido |
| Próximo passos| Quem faz o quê até quando |

> A separação entre "o que foi dito" e "o que eu interpretei" evita que sua suposição vire requisito sem confirmação.

***

# O que é um PRD

> PRD responde uma pergunta simples: "O que estamos construindo e por quê. "

|  | PRD | Spec Técnica | Plano de Analise |
|---|---|---|---|
|Responde | O quê e por quê | Como Implantar | Como medir e interpretar |
| Dono | PM + time | Engenheiro | Analista |
|Escrito quando | Antes de tudo | Após o PRD | Em paralelo ao desenvolvimento


> A spec técnica nasce do PRD. Quando isso acontece ao contrário, engenharia toma decisões no vácuo de contexto de negócio. 

***

# Estrutura de um PRD

1. Problema - por que isso existe 
2. Contexto - o que levou até aqui
3. Objetivos - onde queremos chegar
4. Solução Proposta - o que vamos construir
5. Requisitos - o que o sistema deve fazer
6. Métricas - coo saberemos que funcionou
7. Fora de escopo - o que vamos fazer
8. Riscos e dependencias - o que pode bloquear

> Um PRD fraco é aquele onde alguma dessas perguntas ficou sem resposta. 

***


 || Requisito Funcional | Regra de negocio
|:---:|:---:|:---:|
 Descrever | O que o sistema faz | A lógica que governa o comportamento
|Exemplo | Cliente vê relatório de uso de funcionalidades da plataforma | Funcionalidades com uso < 30 dias não entram no cálculo de adoção
|Origem | Produto | Operação, Jurídico, Compliance


> Regra de negócio não documentada é a principal causa de dashboards inconsistentes

***

## PRD NO MUNDO DA IA

> Especificações estruturadas deixaram de ser documentação. Agora são input direto para IAs que constroem:

| **Código** |
| **Queries** |
| **Pipelines** |
| **Análise** |

**Antes da IA**
Ambiguidade -> Alinhamento -> Execução

| Antes da IA | Agora |
|---|---|
| Ambiguidade -> Alinhamento -> Execução | Ambiguidade -> Interpretação automática -> Erro em escala|
| alguém pergunta | a IA não pergunta |
| alguém responde | ela interpreta |
| o time converge | ela executa |
| o custo é distribuído| o erro escala rápido

> A qualidade do que você constrói com IA é limitada pela qualidade do que você consegue especificar.

***

**CASO - PERFIL DA EMPRESA**

> Contexto: Uma empresa SaaS B2B para times de vendas. Modelo de assinatura mensal.

| MRR | Churn Mensal Geral | Churn Mensal Enterprise |
|:---:|:---:|:---:|
| R$ 6,2M | 4,8% |**6,1%**|



| Ticket Médio Mensal Enterprise| CAC Enterprise| 11 meses |
|:---:|:---:|:---:|
| R$ 18k | R$ 42k | Payback |

***

## NPS Enterprise
> * Reclamação recorrente
> * Não conseguimos extrair insights claros do volume de dados
> * **41**

## Dos clientes enterprise
> * Usam menos de
> * 3 das 10 funcionalidades principais
> * **31%**

## Insights
> * Benchmark
> * Competidor lançou novo módulo de IA há 4 meses
> * **IA**

> O produto existe. Os dados existem. O valor não está sendo percebido.


***

> A diretoria responde com : 

> **"Precisamos usar IA para aumentar retenção enterprise"**

***
## A PROVOCAÇÃO

> Pergunta: Isso é um problema ou uma solução ?

**Resposta** : **solução disfarçada de problema.**

> O que as cinco perguntas teriam revelado antes de chegar aqui ?


***

>## Antes
**"Precisamos usar IA"**
> Solução como problema

>## Depois
**"Clientes não conseguem extrair insights dos dados"**
> Problema identificado

## PROBLEMA REAL
>Clientes enterprese acumulam dados na plataforma mas têm dificuldade em identificar insights acionávies,
levando à baixa adoção de funcionalidade, baixo valor percebido e churn elevado.


## HIPÓTESES
>Se identificarmos subutilização e entregarmos insights acionávies para gestores de vendas, então aumentaremos
a adoção das funcionalidades críticas, o que elevará percepção de valor e reduzirá churn Enterprise.

> **"Usar IA"** **pode significar muita coisa: chatbot, previsão de churn, dashboards automáticos, recomendações de uso, análise de pipeline e etc.
São produtos completamente diferentes, com complexidade e prazos diferentes.**


***

Aqui está a estruturação do conteúdo da imagem **image_3560c4.jpg** em formato Markdown, utilizando blocos de texto e tabelas para replicar visualmente a organização do slide original.

---

## ESCOPO — MUST / SHOULD / NEVER

> ### O QUE VAMOS CONSTRUIR
> 
> 
> Desenvolver um módulo de “AI Insights” que analisa o uso da plataforma para identificar funcionalidades que o cliente não está utilizando (subutilização), explicar por que isso é um problema ou uma oportunidade (insights) e sugerir ações claras sobre o que fazer em seguida (recomendações).

---

### Matriz de Priorização (Escopo)

| MUST | SHOULD | NEVER (por agora) |
| --- | --- | --- |
| **Identificação de funcionalidades subutilizadas** | **Benchmark com clientes similares** *(útil, mas não bloqueia o lançamento)* | **Chatbot completo** |
| **Geração automática de insights** | **Alertas de queda de uso** *(agrega valor, entra no ciclo seguinte)* | **Automação de campanhas** |
| **Recomendações acionáveis** |  | **Integração com CRM** |

---

### Versão em formato de Blocos (Visual Alternativo)

**"Cards"** coloridos da imagem:

🟩 **MUST**

* Identificação de funcionalidades subutilizadas
* Geração automática de insights
* Recomendações acionáveis

🟧 **SHOULD**

* Benchmark com clientes similares *(útil, mas não bloqueia o lançamento)*
* Alertas de queda de uso *(agrega valor, entra no ciclo seguinte)*

🟥 **NEVER (por agora)**

* Chatbot completo
* Automação de campanhas
* Integração com CRM


***



# MÉTRICAS DO CASO

> *Uma boa métrica precisa ser calculável e ter fonte de dados clara. Se o evento não foi implementado, o dado não existe.*

---

### 📊 TABELA DE MÉTRICAS

| Métrica | Meta | Prazo |
| --- | --- | --- |
| Churn enterprise | **6,1% → 4,5%** | 6 meses |
| Clientes usando ≥ 5 funcionalidades | **63% → 80%** | 6 meses |
| Clientes usando AI Insights semanalmente | **0 → 40%** | 3 meses pós-lançamento |

---

### 💡 NOTA DE DESTAQUE

> 🟦 *Métrica intermediária e de adoção existem para sinalizar se estamos no caminho antes de ver o churn cair.*



***


# O PRD COMPLETO DO CASO

---

### 🔴 PROBLEMA

> Clientes enterprise acumulam dados na plataforma mas têm dificuldade em identificar insights acionáveis, levando à baixa adoção de funcionalidades, baixo valor percebido e churn elevado.

### 🟠 CONTEXTO

> NPS enterprise: 41. Churn enterprise: 6,1% vs. 4,8% geral. 37% dos clientes usam menos de 3 das 10 funcionalidades principais.

### 🟡 OBJETIVOS

> Aumentar a percepção de valor do produto em contas enterprise ao transformar dados em insights acionáveis, elevando a adoção de funcionalidades críticas e reduzindo churn.

### 🟣 SOLUÇÃO PROPOSTA

> Desenvolver um módulo de “AI Insights” que analisa o uso da plataforma para identificar funcionalidades que o cliente não está utilizando (subutilização), explicar por que isso é um problema ou uma oportunidade (insights) e sugerir ações claras sobre o que fazer em seguida (recomendações).

---

### 🟢 REQUISITOS

> **Must:** geração automática de insights, identificação de funcionalidades subutilizadas, recomendações acionáveis.
> **Should:** benchmark com clientes similares, alertas de queda de uso.
> **Never:** chatbot completo, automação de campanhas, integração com CRM.

### 🔵 MÉTRICAS

> Churn enterprise: 6,1% → 4,5% em 6 meses.
> Adoção ≥ 5 funcionalidades: 63% → 80% em 6 meses.
> Uso semanal do AI Insights: 0 → 40% em 3 meses.
> ⚠️ *evento de tracking a implementar.*

### ⚪ DEPENDÊNCIAS

> Evento de uso do AI Insights implementado no backend.

### 🟤 FORA DE ESCOPO

> Chatbot completo, automação de campanhas, integração com CRM.


***


# TRÊS IDEIAS PARA LEVAR DAQUI

---

### 1️⃣ O PRD começa antes do documento.

> A qualidade do que você escreve depende da qualidade das conversas que você teve.

---

### 2️⃣ PRD não é trabalho só do PM.

> Engenheiros e analistas que sabem extrair e estruturar problemas têm mais autonomia e entregam mais impacto.

---

### 3️⃣ Clareza é respeito com o time.

> "Quando você não documenta o que quer construir, você transfere o custo da sua ambiguidade para as pessoas que vão trabalhar com você."