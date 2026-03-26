# LABORATÓRIO - GOVERNANÇA E CONFORMIDADE

## Portal de Confiança de Serviços

O Portal de Confiança de Serviços (Service Trust Portal) é um recurso da Microsoft que centraliza informações importantes sobre segurança, privacidade e conformidade dos serviços em nuvem. É fundamental saber que ele existe, para que serve e que tipo de informações ele oferece.

Dentro do portal, é possível encontrar padrões, certificações, regulamentos, relatórios de auditoria e diversos outros documentos que auxiliam diretamente na governança de ambientes em nuvem. Ele funciona como uma base de consulta confiável para profissionais que precisam garantir que seus ambientes estejam em conformidade com normas e boas práticas do mercado.

### Certificações, Regulamentos e Padrões

O Azure disponibiliza uma ampla variedade de certificações, regulamentos e padrões que atendem diferentes setores e necessidades. Entre os principais disponíveis, estão:

- ISO/IEC 27001 – Padrão internacional de gestão de segurança da informação.
- SOC 1, SOC 2 e SOC 3 – Relatórios de controle organizacional voltados a segurança, disponibilidade e confidencialidade.
- GDPR (General Data Protection Regulation) – Regulamento europeu de proteção de dados pessoais.
- LGPD (Lei Geral de Proteção de Dados) – Regulamento brasileiro de proteção de dados pessoais.
- HIPAA – Regulamento voltado à proteção de dados na área da saúde (Estados Unidos).
- FedRAMP – Padrão de segurança para serviços em nuvem utilizados pelo governo dos EUA.
- NIST – Conjunto de padrões e diretrizes de segurança cibernética.
- É importante destacar que existem regulamentos e recursos próprios relacionados a países específicos, ou seja, dependendo da região de atuação da empresa, podem ser aplicáveis normas locais que o Azure também contempla.

## Tags (Marcas)

As tags no Azure são pares de nome e valor que podem ser atribuídos a recursos e grupos de recursos para fins de organização, controle de custos e gerenciamento.

Por exemplo, é possível criar tags como departamento: financeiro ou ambiente: produção, facilitando a identificação e o agrupamento lógico dos recursos.

Um ponto importante é entender como as tags afetam os grupos de recursos: as tags aplicadas a um grupo de recursos não são herdadas automaticamente pelos recursos que estão dentro dele. Isso significa que, se for necessário que todos os recursos de um grupo possuam determinada tag, ela precisa ser aplicada individualmente a cada recurso ou por meio de políticas (policies) que forcem essa atribuição.

## Microsoft Purview
O Microsoft Purview é uma solução unificada de governança de dados, conformidade e gerenciamento de riscos. Ele engloba um conjunto abrangente de ferramentas que ajudam as organizações a proteger e gerenciar seus dados em diferentes ambientes.

Entre os principais recursos que o Purview oferece, estão:

- Mapa de Dados – Permite descobrir, classificar e mapear dados em toda a organização, identificando onde estão armazenados e quem tem acesso.
- Catálogo de Dados – Facilita a busca e o entendimento dos dados disponíveis, funcionando como um inventário organizado.
- Gerenciamento de Conformidade – Auxilia no acompanhamento de normas e regulamentos, garantindo que a organização esteja em conformidade.
- Proteção de Informações – Classifica e protege dados sensíveis com rótulos de sensibilidade.
- Prevenção contra Perda de Dados (DLP) – Monitora e impede o compartilhamento indevido de informações confidenciais.
- Gerenciamento de Riscos Internos – Identifica atividades suspeitas e possíveis ameaças internas à organização.
- Auditoria e Descoberta Eletrônica (eDiscovery) – Permite pesquisar, coletar e auditar dados para fins legais ou investigativos.
- De forma resumida, o Microsoft Purview é uma ferramenta essencial para qualquer organização que precisa ter visibilidade, controle e proteção sobre seus dados, independentemente de onde eles estejam armazenados.

## Bloqueios de Recurso

Os bloqueios de recurso no Azure são mecanismos de proteção que impedem alterações acidentais ou exclusões indevidas de recursos importantes. Existem dois tipos de bloqueio:

- Somente Leitura (ReadOnly) – Permite visualizar o recurso, mas impede qualquer tipo de modificação. Nenhum usuário consegue alterar ou excluir o recurso enquanto esse bloqueio estiver ativo.
- Exclusão (Delete) – Permite visualizar e modificar o recurso normalmente, porém impede que ele seja excluído.
- Um aspecto fundamental dos bloqueios é que eles podem ser herdados. Quando um bloqueio é aplicado a um grupo de recursos, todos os recursos dentro desse grupo herdam automaticamente o mesmo bloqueio. Da mesma forma, bloqueios aplicados no nível da assinatura são herdados por todos os grupos de recursos e recursos abaixo dela. Essa herança garante uma camada extra de proteção em cascata, evitando ações indesejadas em toda a hierarquia.

## Políticas (Policies)

As Azure Policies são regras criadas para garantir que os recursos dentro de um ambiente Azure estejam em conformidade com os padrões e requisitos definidos pela organização. Elas funcionam como um mecanismo de governança automatizado, verificando continuamente se os recursos atendem às condições estabelecidas.

De forma geral, as políticas funcionam assim:

- Definição da política - É criada uma regra que define o que é permitido ou não (por exemplo, "todos os recursos devem ser criados apenas na região Brasil Sul").
- Atribuição da política – A regra é aplicada a um escopo específico, como uma assinatura, um grupo de recursos ou um recurso individual.
- Avaliação – O Azure verifica automaticamente se os recursos existentes e os novos estão em conformidade com a política.
Ação – Dependendo da configuração, a política pode apenas auditar (informar que algo está fora de conformidade) ou impor (enforce) a regra, impedindo a criação de recursos que não atendam aos critérios.
- A opção de enforce policy (impor política) é especialmente importante, pois quando ativada, ela bloqueia ativamente qualquer ação que viole a regra definida. Por exemplo, se uma política impõe que máquinas virtuais só podem ser criadas em determinadas regiões, qualquer tentativa de criar uma VM fora dessas regiões será negada automaticamente.

As políticas são ferramentas fundamentais para manter a padronização, segurança e controle de custos em ambientes corporativos de nuvem.
