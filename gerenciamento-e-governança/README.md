# 🏛️ Gerenciamento e Governança

> Módulo do repositório [Laboratórios Azure Essentials (DIO)](https://github.com/VictorPonciano1/lab-azure-fundamentals-dio)

Esta pasta reúne as anotações dos laboratórios focados em **gerenciamento, governança, implantação e monitoramento** no Microsoft Azure. Cada documento aborda um tema diferente, passando por controle de custos, conformidade, ferramentas de deploy e ferramentas de monitoramento.

---

## 📂 Laboratórios

| # | Arquivo | Tema | Destaques |
|---|---------|------|-----------|
| 1 | [Lab1.md](./Lab1.md) | **Gerenciamento de Custos** | Calculadora TCO, Calculadora de Preços do Azure, Monitoramento/Gerenciamento de Custos |
| 2 | [Lab2.md](./Lab2.md) | **Governança e Conformidade** | Portal de Confiança de Serviços, Tags, Microsoft Purview, Bloqueios de Recurso, Políticas (Policies) |
| 3 | [Lab3.md](./Lab3.md) | **Gerenciamento e Implantação** | Portal do Azure, Cloud Shell, Bicep (linguagem declarativa), escolha da ferramenta certa |
| 4 | [Lab4.md](./Lab4.md) | **Monitoramento** | Azure Monitor, Service Health, Advisor (recomendações de custo, segurança, performance) |

---

## 🧠 Resumo dos Conceitos Abordados

### Lab 1 — Gerenciamento de Custos
- **Calculadora TCO:** compara custos On-Premises vs Nuvem em 3 fases (definir cargas, ajustar suposições, exibir relatórios)
- **Calculadora de Preços:** focada nos serviços Azure em si (VMs, Storage, SQL, Functions, IA)
- Ambas calculam com base na **região selecionada** — preço varia por região
- **Monitoramento de Custos:** mostra overview dos gastos reais, permite criar alertas e exportar relatórios

### Lab 2 — Governança e Conformidade
- **Portal de Confiança de Serviços:** centraliza certificações, regulamentos e relatórios de auditoria (ISO 27001, SOC, GDPR, LGPD, HIPAA)
- **Tags:** pares nome/valor para organização — não são herdadas automaticamente pelos recursos do grupo
- **Microsoft Purview:** governança de dados unificada (mapa de dados, DLP, eDiscovery)
- **Bloqueios de Recurso:** ReadOnly (impede modificação) e Delete (impede exclusão) — são herdados em cascata
- **Policies:** regras automatizadas de conformidade, com opção de **enforce** para bloquear ações que violem a política

### Lab 3 — Gerenciamento e Implantação
- **Portal do Azure:** forma visual e intuitiva, ideal pra quem está começando
- **Cloud Shell:** terminal no navegador (PowerShell ou Bash), precisa de Storage Account
- **Bicep:** linguagem declarativa — você descreve o estado final e o Azure resolve os passos
- Abordagem **imperativa** (CLI) vs **declarativa** (Bicep) — cada uma tem seu cenário ideal

### Lab 4 — Monitoramento
- **Azure Monitor:** visão completa dos recursos (métricas, alertas, Application Insights)
- **Service Health:** mostra a saúde dos serviços da Microsoft (indisponibilidades e manutenções planejadas)
- **Advisor:** consultor gratuito com recomendações de custo, segurança, confiabilidade, performance e excelência operacional
