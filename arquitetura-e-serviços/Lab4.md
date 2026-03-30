# LABORATÓRIO - IDENTIDADE, ACESSO E SEGURANÇA

## Microsoft Entra ID (antigo Azure AD)

O Microsoft Entra ID é o serviço de **gerenciamento de identidades** do Azure. É ele que cuida de quem pode acessar o quê. Basicamente, é onde a gente cria usuários, grupos e gerencia as permissões de todo mundo.

Algumas coisas que dá pra fazer no Entra ID:

- **Criar usuários**: cada pessoa que precisa acessar o Azure ganha um usuário com login e senha.
- **Criar grupos**: junta vários usuários num grupo só pra facilitar na hora de dar permissões (ex: grupo "Desenvolvedores", grupo "Financeiro").
- **Usuários convidados (B2B)**: dá pra convidar pessoas de fora da organização pra acessar recursos específicos, sem precisar criar uma conta interna pra elas.
- **Autenticação Multifator (MFA)**: além da senha, o usuário precisa confirmar a identidade por outro meio (ex: código no celular). Isso deixa o acesso muito mais seguro.

> O Entra ID é tipo a recepção de um prédio comercial: ele confere quem você é (autenticação) e verifica se você tem permissão pra entrar naquele andar (autorização).

---

## RBAC — Controle de Acesso Baseado em Funções

O **RBAC (Role-Based Access Control)** é o modelo que o Azure usa pra controlar quem pode fazer o quê nos recursos. Em vez de dar permissão individualmente pra cada pessoa, a gente atribui **funções (roles)** que já vêm com um conjunto de permissões pré-definidas.

As três funções mais comuns:

| Função | O que pode fazer |
|--------|-----------------|
| **Leitor (Reader)** | Só visualiza os recursos, não altera nada |
| **Colaborador (Contributor)** | Cria, altera e exclui recursos, mas não gerencia permissões |
| **Proprietário (Owner)** | Faz tudo, inclusive gerencia quem tem acesso |

O RBAC funciona com **herança**: se a gente dá uma permissão no nível da assinatura, ela desce pra todos os grupos de recursos e recursos abaixo. A atribuição é feita pelo menu **Controle de Acesso (IAM)** no portal.

> Resumindo: o RBAC é o "crachá" de cada pessoa. Dependendo do crachá que você tem, pode entrar em mais ou menos salas do prédio.

---

## Microsoft Defender for Cloud

O **Defender for Cloud** é a ferramenta de segurança do Azure que analisa o ambiente e mostra o que tá seguro e o que precisa de atenção. Ele dá uma **pontuação de segurança (Secure Score)** que vai de 0 a 100% — quanto maior, melhor.

O que ele faz na prática:

- **Recomendações de segurança**: mostra uma lista do que precisa ser corrigido (ex: "habilite MFA pra todos os usuários", "feche portas desnecessárias").
- **Alertas de segurança**: avisa quando detecta algo suspeito no ambiente.
- **Conformidade regulatória**: mostra se o ambiente tá de acordo com padrões como ISO 27001, NIST, LGPD, etc.

> O Defender for Cloud é tipo um "check-up médico" do seu ambiente Azure. Ele examina tudo, dá uma nota geral de saúde e fala exatamente o que você precisa melhorar.

---

Esse laboratório mostrou que segurança no Azure não é só colocar senha forte. Envolve gerenciar identidades (Entra ID), controlar permissões com precisão (RBAC) e monitorar o ambiente continuamente (Defender for Cloud). Os três trabalhando juntos é o que garante um ambiente seguro de verdade.
