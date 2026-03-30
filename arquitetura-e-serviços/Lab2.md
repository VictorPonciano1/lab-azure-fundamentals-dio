# LABORATÓRIO - COMPUTAÇÃO E REDE

## Máquinas Virtuais (VMs)

As máquinas virtuais no Azure podem ser criadas com atribuições e configurações pré-definidas, o que facilita bastante na hora de subir um ambiente rapidinho. Basicamente, a gente escolhe o que a VM vai ter antes mesmo dela ser criada.

### Tipos de configurações e atributos ao criar uma VM

Na hora de criar uma máquina virtual, existem várias coisas que a gente pode configurar:

- **Imagem do SO**: dá pra escolher entre Windows Server, Ubuntu, Debian, Red Hat, entre outros. É tipo escolher qual sistema operacional a VM vai rodar.
- **Tamanho (Size)**: define a quantidade de vCPUs e memória RAM. Por exemplo:
  - **Série B** - uso geral econômico, bom pra testes e ambientes de dev.
  - **Série D** - uso geral, equilibra CPU e memória, serve pra maioria das cargas de trabalho.
  - **Série E** - otimizada pra memória, ideal pra bancos de dados.
  - **Série F** - otimizada pra computação, quando precisa de mais processamento.
  - **Série N** - tem GPU, usada pra machine learning e renderização.
- **Disco**: dá pra escolher entre HDD Standard, SSD Standard e SSD Premium. Quanto melhor o disco, mais rápido (e mais caro também rs).
- **Rede virtual (VNet)**: a gente configura em qual rede a VM vai ficar, a sub-rede, IP público, etc.
- **Região**: onde a VM vai ficar fisicamente (ex: Brazil South, East US).
- **Grupo de recursos**: é como se fosse uma "pasta" pra organizar os recursos no Azure.

---

## Conjunto de Dimensionamento de Máquinas Virtuais (VMSS)

O Conjunto de Dimensionamento (Virtual Machine Scale Sets) é um recurso que permite criar e gerenciar um grupo de VMs com balanceamento de carga. A parte mais legal �� que ele faz o **escalonamento automático** — ou seja, se a demanda aumentar, ele cria mais VMs sozinho, e se diminuir, ele remove as que não precisa mais.

- Todas as VMs do conjunto são criadas a partir da mesma imagem e configuração base.
- É muito usado pra aplicações que precisam de **alta disponibilidade** e que podem ter picos de acesso.
- Dá pra definir regras de escalonamento, tipo: "se o uso de CPU passar de 75%, cria mais 2 VMs".
- Ele distribui o tráfego entre as VMs automaticamente através do balanceador de carga.

Resumindo: em vez de ficar criando VM por VM na mão, o Scale Set faz isso de forma automática e inteligente.

---

## Área de Trabalho Virtual do Azure (Azure Virtual Desktop)

A Área de Trabalho Virtual do Azure é basicamente um serviço de virtualização de desktop que roda na nuvem. Com ele, a gente consegue acessar um desktop Windows completo de qualquer lugar, pelo navegador ou por um aplicativo.

- Permite que vários usuários usem o **Windows 11/10 multissessão**, ou seja, várias pessoas compartilham a mesma VM (isso reduz custos).
- É bem útil pra empresas que querem que os funcionários trabalhem remotamente sem precisar de um computador potente — tudo roda no Azure.
- Dá pra publicar aplicativos individuais ou um desktop completo.
- A segurança é gerenciada pelo Azure, então os dados ficam na nuvem e não no computador do usuário.

---

## Azure Functions

O Azure Functions é um serviço de computação **serverless** — ou seja, a gente não precisa se preocupar com servidor nenhum. Basicamente, você escreve uma função (um pedaço de código) e o Azure cuida de toda a infraestrutura por baixo.

### Overview geral de uma Function:

- **O que é**: é um serviço que permite executar pequenos blocos de código (funções) sem precisar gerenciar servidores.
- **Como funciona**: a função é acionada por um **gatilho (trigger)** — pode ser uma requisição HTTP, uma mensagem numa fila, um timer, uma alteração no banco de dados, etc.
- **Linguagens suportadas**: C#, Java, JavaScript, Python, PowerShell, entre outras.
- **Cobrança**: você só paga pelo tempo que a função ficou executando. Se ninguém chamou a função, não paga nada. É o famoso modelo **pay-per-execution**.
- **Casos de uso comuns**:
  - Processar arquivos que foram enviados pra um storage.
  - Responder a webhooks e requisições de API.
  - Executar tarefas agendadas (tipo um cron job).
  - Processar mensagens de filas.

O legal do Azure Functions é que ele escala automaticamente. Se de repente chegarem mil requisições ao mesmo tempo, o Azure cria instâncias suficientes pra dar conta, e depois desce tudo de volta. A gente não precisa configurar nada disso.
