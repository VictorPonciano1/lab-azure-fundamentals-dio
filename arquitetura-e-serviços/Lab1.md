# LABORATÓRIO - COMPONENTES DE ARQUITETURA DO AZURE

Neste laboratório foram explorados os principais componentes que formam a base da arquitetura do Azure: as **regiões e datacenters**, os **grupos de recursos** e as **redes virtuais**. Entender esses componentes é essencial para saber onde os recursos ficam hospedados, como organizá-los e como eles se comunicam entre si.

---

## Regiões e Datacenters

O Azure possui datacenters espalhados pelo mundo inteiro, organizados em **regiões**. Cada região é um conjunto de datacenters próximos entre si, conectados por uma rede de baixa latência. A escolha da região impacta diretamente na **velocidade de acesso**, no **custo** e na **conformidade legal** dos dados.

No Brasil, existem duas regiões disponíveis:

- **Brazil South (São Paulo):** é a região principal do Azure no Brasil. A maioria dos serviços estão disponíveis aqui e é a escolha padrão para quem precisa manter os dados hospedados no país.
- **Brazil Southeast (Rio de Janeiro):** é a região destinada a **Disaster Recovery (Recuperação de Desastres)**. Ela serve como um "plano B" — caso a região de São Paulo sofra alguma falha grave, os dados e serviços replicados podem ser recuperados a partir dessa região.

Um ponto importante é o conceito de **Data Residency (Residência de Dados)**. Ao utilizar a região Brazil South, os dados ficam armazenados **fisicamente dentro do Brasil**. Isso é fundamental para empresas que precisam seguir a **LGPD (Lei Geral de Proteção de Dados)** e outras regulamentações que exigem que os dados dos usuários brasileiros permaneçam em território nacional.

> Para quem está começando, uma boa forma de entender regiões é pensar em **filiais de uma empresa**: o Azure tem "filiais" em vários países, e você escolhe em qual delas quer guardar seus recursos. Se precisa que os dados fiquem no Brasil, escolhe a filial de São Paulo (Brazil South).

---

## Grupos de Recursos (Resource Groups)

Os **Grupos de Recursos** são como pastas que **agrupam e organizam** os recursos do Azure que compartilham o mesmo ciclo de vida, as mesmas políticas ou o mesmo projeto. Por exemplo, uma aplicação web pode ter seu App Service, seu banco de dados e sua rede virtual dentro de um único grupo de recursos.

Algumas características importantes:

- Todo recurso no Azure **precisa** pertencer a um grupo de recursos
- Um recurso só pode estar em **um grupo** por vez
- Os grupos ajudam a aplicar **políticas de governança** de forma centralizada — se uma regra é aplicada ao grupo, todos os recursos dentro dele são afetados
- É possível **excluir** um grupo inteiro e todos os recursos dentro dele serão removidos juntos (cuidado!)

Outro recurso muito útil são as **Marcações (Tags)**. Tags são rótulos no formato `chave: valor` que podem ser aplicados tanto nos **recursos individuais** quanto no **grupo de recursos** como um todo.

Exemplos de tags:

| Chave | Valor |
|-------|-------|
| `ambiente` | produção |
| `projeto` | app-web |
| `responsavel` | victor |
| `centro-de-custo` | TI-001 |

> As tags ajudam principalmente na **organização** e no **controle de custos**. É possível filtrar a fatura do Azure por tags e saber exatamente quanto cada projeto ou equipe está gastando. Em ambientes com muitos recursos, tags bem definidas fazem toda a diferença.

---

## Rede Virtual (VNet)

A **Rede Virtual (Virtual Network / VNet)** é o componente que permite a comunicação entre os recursos do Azure. É como a "rede interna" onde as máquinas virtuais, bancos de dados e outros serviços se conectam e conversam entre si.

Durante o laboratório, ao acessar uma VNet pelo portal do Azure, foi possível visualizar informações importantes como:

- **Implantação (Deployment):** mostra o histórico de implantações realizadas na rede, incluindo quais recursos foram provisionados
- **Status:** indica se a rede está ativa e funcionando corretamente
- **Duração:** tempo que a implantação levou para ser concluída

Essas informações ficam disponíveis diretamente no portal e são úteis para acompanhar o que está acontecendo na rede, identificar possíveis falhas e entender o progresso das implantações.

> Voltando à analogia do prédio usada no Lab 1: se o Azure Bastion é a portaria, a **VNet** seria o condomínio inteiro — é ela que define o espaço onde os "apartamentos" (VMs, bancos de dados, etc.) ficam e como eles se comunicam entre si.

---

Esse laboratório ajudou a entender que a arquitetura do Azure vai além dos recursos em si. Saber **onde** os recursos estão (regiões), **como organizá-los** (grupos e tags) e **como eles se comunicam** (VNets) são decisões fundamentais que impactam na segurança, no custo e na conformidade de qualquer projeto na nuvem.
