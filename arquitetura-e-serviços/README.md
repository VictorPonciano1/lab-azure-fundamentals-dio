# 🏗️ Arquitetura e Serviços

> Módulo do repositório [Laboratórios Azure Essentials (DIO)](https://github.com/VictorPonciano1/lab-azure-fundamentals-dio)

Esta pasta reúne as anotações e desafios de código dos laboratórios focados em **arquitetura, serviços e segurança** no Microsoft Azure. Os documentos cobrem desde componentes de infraestrutura até identidade e controle de acesso, além de desafios práticos em Python.

---

## 📂 Laboratórios

| # | Arquivo | Tema | Destaques |
|---|---------|------|-----------|
| 1 | [Lab1.md](./Lab1.md) | **Componentes de Arquitetura do Azure** | Regiões e Datacenters (Brazil South/Southeast), Grupos de Recursos, Tags, Rede Virtual (VNet) |
| 2 | [Lab2.md](./Lab2.md) | **Computação e Rede** | Configurações de VMs (séries B, D, E, F, N), VMSS, Azure Virtual Desktop, Azure Functions (serverless) |
| 3 | [Lab3.md](./Lab3.md) | **Armazenamento** | Storage Account, Blob/File/Queue/Table Storage, camadas de acesso (Hot, Cool, Cold, Archive), migração de dados |
| 4 | [Lab4.md](./Lab4.md) | **Identidade, Acesso e Segurança** | Microsoft Entra ID, RBAC (Reader, Contributor, Owner), Defender for Cloud, Secure Score |
| 5 | [Lab5.py](./Lab5.py) | **Desafio de Código — Arquitetura** | Identificar componentes: Regiões, Zonas de Disponibilidade, Datacenters, Assinaturas, Grupos de Gerenciamento |
| 6 | [Lab6.py](./Lab6.py) | **Desafio de Código — Armazenamento** | Identificar serviços: Blob, Arquivos, Fila, Tabelas, Disco do Azure |
| 7 | [Lab7.py](./Lab7.py) | **Desafio de Código — Segurança** | Identificar recursos: RBAC, Entra ID, MFA, Key Vault, Security Center |

---

## 🧠 Resumo dos Conceitos Abordados

### Lab 1 — Componentes de Arquitetura
- **Regiões**: Brazil South (principal) e Brazil Southeast (Disaster Recovery)
- **Grupos de Recursos**: organizam recursos com mesmo ciclo de vida; tags ajudam no controle de custos
- **VNet**: rede interna onde os recursos se comunicam

### Lab 2 — Computação e Rede
- **VMs**: configurações de SO, tamanho (séries), disco, rede e região
- **VMSS**: escalonamento automático de VMs com balanceamento de carga
- **Azure Virtual Desktop**: desktop Windows na nuvem com multissessão
- **Azure Functions**: serverless, pay-per-execution, escala automática

### Lab 3 — Armazenamento
- **Storage Account**: nome único global, desempenho Standard/Premium, redundância (LRS, ZRS, GRS, GZRS)
- **Blob**: arquivos em geral | **File**: compartilhamento SMB | **Queue**: mensageria | **Table**: NoSQL
- **Camadas de acesso**: Hot → Cool → Cold → Archive (menos acesso = mais barato pra guardar)

### Lab 4 — Identidade, Acesso e Segurança
- **Entra ID**: gerenciamento de usuários, grupos, convidados (B2B) e MFA
- **RBAC**: controle de permissões por funções (Reader, Contributor, Owner) com herança
- **Defender for Cloud**: pontuação de segurança, recomendações e conformidade regulatória

### Labs 5, 6 e 7 — Desafios de Código (Python)
- Exercícios práticos usando `if/elif/else` pra identificar componentes, serviços de armazenamento e recursos de segurança do Azure
