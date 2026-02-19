# COMPUTAÇÃO EM NUVEM - LABORATÓRIO

## ANOTAÇÕES - RESUMO: LOCALIZANDO SERVIÇOS POR CATEGORIA

Durante o laboratório foi possível perceber que nem todos os serviços do Azure ficam disponíveis automaticamente para todos os usuários. Alguns recursos podem não aparecer ou não permitir criação dependendo de fatores como o **custo do serviço**, o **tipo de assinatura utilizada** (conta gratuita, estudante ou corporativa) e também a **região escolhida** para implantação. Isso acontece porque determinados serviços possuem limitações comerciais ou ainda não estão disponíveis em todos os datacenters do Azure.

Outro ponto importante observado foi o conceito de **Bastion (Bastião)**. O Azure Bastion é um serviço que permite acessar máquinas virtuais de forma mais segura, diretamente pelo navegador, sem a necessidade de expor portas públicas na internet.

De forma simples, o Bastion funciona como uma camada extra de proteção entre o usuário e as máquinas virtuais. Em vez de conectar diretamente na VM usando IP público, o acesso acontece primeiro por esse ambiente seguro, reduzindo riscos de ataques externos.

Em outras áreas de TI, esse mesmo conceito é conhecido como **Jump Server** ou **Jump Host**.

> **Jump Server:** é um servidor intermediário utilizado para acessar outros servidores internos de maneira controlada e segura. O usuário se conecta primeiro a esse servidor e, somente depois, acessa os demais recursos da rede privada.

Para quem está começando, uma boa analogia é imaginar o Bastion como a **portaria de um prédio**: você não entra direto nos apartamentos; primeiro passa pela portaria, onde o acesso é validado e monitorado. Isso ajuda a aumentar a segurança e facilita o controle de quem acessa cada recurso.

Esse laboratório ajudou a entender que, além de criar recursos na nuvem, é fundamental pensar em **segurança, controle de acesso e organização**, que são princípios básicos do uso profissional do Azure.
