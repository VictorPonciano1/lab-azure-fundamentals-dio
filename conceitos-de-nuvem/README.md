# 📘 Conceitos de Nuvem

> Módulo do repositório [Laboratórios Azure Essentials (DIO)](https://github.com/VictorPonciano1/lab-azure-dio)

Esta pasta reúne as anotações dos três primeiros laboratórios do curso, focados nos **fundamentos da computação em nuvem** no Microsoft Azure. Cada documento aborda um tema diferente, partindo da exploração do portal até os modelos de serviço.

---

## 📂 Laboratórios

| # | Arquivo | Tema | Destaques |
|---|---------|------|-----------|
| 1 | [Lab1.md](./Lab1.md) | **Localizando Serviços por Categoria** | Disponibilidade de serviços por região/assinatura, Azure Bastion e o conceito de Jump Server |
| 2 | [Lab2.md](./Lab2.md) | **Benefícios da Computação em Nuvem** | Tabela de SLA, opções de criação de VMs, modelos de redundância (LRS, ZRS, GRS, GZRS) |
| 3 | [Lab3.md](./Lab3.md) | **Tipos de Serviço em Nuvem** | IaaS vs PaaS vs SaaS, Azure SQL Database como exemplo de PaaS, Calculadora de Preços, Governança |

---

## 🧠 Resumo dos Conceitos Abordados

### Lab 1 — Localizando Serviços por Categoria
- Nem todos os serviços estão disponíveis para todas as assinaturas e regiões
- **Azure Bastion:** acesso seguro a VMs pelo navegador, sem expor portas públicas
- Conceito de **Jump Server** como camada de proteção

### Lab 2 — Benefícios da Computação em Nuvem
- **SLA:** quanto mais "noves", maior a disponibilidade (de 99% até 99,999%)
- Configurações essenciais de uma VM: região, imagem, tamanho, disco, rede
- **Redundância de armazenamento:** LRS (11 noves) → ZRS (12 noves) → GRS/GZRS (16 noves)

### Lab 3 — Tipos de Serviço em Nuvem
- **IaaS:** você gerencia quase tudo (ex: VMs)
- **PaaS:** você gerencia dados e aplicação (ex: Azure SQL Database)
- **SaaS:** você só usa (ex: Microsoft 365)
- Ferramentas de governança: Azure Policy, RBAC, Resource Locks, Tags
