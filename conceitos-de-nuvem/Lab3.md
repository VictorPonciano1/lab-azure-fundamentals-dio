# LABORATÓRIO - TIPOS DE SERVIÇO EM NUVEM

Os tipos de serviço em nuvem são classificados em três categorias, cada uma com um nível diferente de responsabilidade entre o provedor (Azure) e o usuário:

- **IaaS (Infrastructure as a Service / Infraestrutura como Serviço)**
- **PaaS (Platform as a Service / Plataforma como Serviço)**
- **SaaS (Software as a Service / Software como Serviço)**

---

## O que cada serviço representa no Azure

### IaaS — Infraestrutura como Serviço

O Azure fornece a infraestrutura básica (servidores, rede, armazenamento) e o usuário gerencia todo o resto: sistema operacional, atualizações, aplicações e dados.

É como alugar um **terreno com estrutura básica**: água e luz estão lá, mas quem constrói a casa é você.

**Exemplos:** Máquinas Virtuais, Redes Virtuais, Azure Disks.

### PaaS — Plataforma como Serviço

O Azure fornece a infraestrutura **e** a plataforma já configurada. O usuário foca apenas no desenvolvimento da aplicação e nos dados.

É como alugar um **apartamento mobiliado**: a estrutura já está pronta, você só traz suas coisas.

**Exemplos:** Azure App Service, Azure SQL Database, Azure Container Instances.

### SaaS — Software como Serviço

O Azure fornece **tudo pronto**: infraestrutura, plataforma e a aplicação. O usuário simplesmente usa o software pelo navegador.

É como se hospedar em um **hotel**: tudo funcionando, você só aproveita.

**Exemplos:** Microsoft 365, Outlook Online, OneDrive.

---

### Tabela de Responsabilidade Compartilhada

| Responsabilidade | IaaS | PaaS | SaaS |
|-----------------|------|------|------|
| Dados | 👤 Usuário | 👤 Usuário | 👤 Usuário |
| Aplicações | 👤 Usuário | 👤 Usuário | ☁️ Azure |
| Sistema Operacional | 👤 Usuário | ☁️ Azure | ☁️ Azure |
| Infraestrutura | ☁️ Azure | ☁️ Azure | ☁️ Azure |

> De forma simples: quanto mais você "sobe" de IaaS para SaaS, **menos responsabilidade técnica** você tem e **mais o Azure cuida para você**.

---

## Relação com a Criação de Máquinas Virtuais

A criação de **Máquinas Virtuais** é o exemplo mais clássico de **IaaS**. O usuário escolhe o SO, instala as aplicações, gerencia atualizações e configura o firewall. O Azure cuida apenas do hardware físico.

Se o objetivo for apenas **hospedar uma aplicação web** sem gerenciar uma VM inteira, o ideal seria o **Azure App Service (PaaS)** — basta subir o código e o Azure cuida do resto.

E se for simplesmente **usar um software pronto** como o Teams, isso já é **SaaS** — basta fazer login.

---

## Banco de Dados SQL — Exemplo Prático de PaaS

O **Azure SQL Database** é um ótimo exemplo de PaaS. Ao criá-lo no portal, as principais configurações são:

- **Servidor Lógico SQL:** funciona como um "contêiner administrativo" que agrupa os bancos. É necessário definir nome, região e método de autenticação (SQL ou Microsoft Entra ID).
- **Camada de Computação:** define desempenho e custo — pode ser por **DTU** (pacotes pré-definidos) ou **vCore** (escolha flexível de núcleos e memória).
- **Redundância de Backup:** mesmos modelos do laboratório anterior (LRS, ZRS, GRS).
- **Regras de Firewall:** por padrão, **nenhum acesso externo é permitido**. É necessário liberar IPs específicos.

O ponto-chave é: você **não gerencia** o hardware, o SO nem as atualizações do SQL Server. O Azure cuida de tudo isso — você foca apenas nos **dados e nas consultas**. Por isso é PaaS.

> Se fosse necessário instalar o SQL Server manualmente em uma VM, gerenciando tudo por conta própria, aí seria **IaaS**.

---

## Calculadora de Preços e os Tipos de Serviço

A **Calculadora de Preços do Azure** ([azure.microsoft.com/pricing/calculator](https://azure.microsoft.com/pricing/calculator/)) permite estimar custos antes de criar recursos. A cobrança varia conforme o tipo de serviço:

| Tipo | O que você configura | Modelo de cobrança |
|------|---------------------|-------------------|
| **IaaS** | Hardware, SO, disco, rede, horas | Por uso (detalhado) |
| **PaaS** | Camada, capacidade, armazenamento | Por uso (simplificado) |
| **SaaS** | Número de usuários | Por licença/usuário |

> Uma boa prática antes de criar qualquer recurso é **sempre consultar a calculadora**. Isso evita surpresas na fatura, especialmente em contas gratuitas com crédito limitado.

---

## Governança e os Serviços de Nuvem

A governança garante que os recursos sejam usados de forma **organizada, segura e controlada**. No IaaS a responsabilidade de governança é maior (o usuário gerencia quase tudo), enquanto no SaaS é menor (o provedor cuida da maior parte). As principais ferramentas do Azure para isso são:

| Ferramenta | Função |
|-----------|--------|
| **Azure Policy** | Define regras sobre como os recursos devem ser configurados |
| **RBAC** | Define quem pode fazer o quê (leitura, escrita, exclusão) |
| **Resource Locks** | Impede exclusão ou modificação acidental de recursos |
| **Tags** | Rótulos para organizar recursos (ex: `ambiente: produção`) |
| **Cost Management** | Monitora e controla os gastos |

> Na prática, governança começa com atitudes simples: organizar recursos em grupos, nomear de forma clara, definir quem pode acessar o quê e acompanhar os custos.

---

Esse laboratório ajudou a entender que **IaaS, PaaS e SaaS** não são apenas conceitos teóricos, mas categorias que impactam diretamente em como criamos recursos, quanto pagamos e qual o nosso nível de responsabilidade no Azure.
