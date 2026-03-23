# LABORATÓRIO - CRIANDO MÁQUINAS VIRTUAIS

Um dos benefícios da Nuvem se trata do **SLA (Service Level Agreement / Acordo de Nível de Serviço)**. O SLA define a garantia de disponibilidade que a Microsoft oferece para cada serviço do Azure. Quanto maior a porcentagem do SLA, menor é o tempo de inatividade permitido. Abaixo, uma tabela com os principais níveis de SLA e seus respectivos tempos de inatividade:

| SLA (%) | Tempo de inatividade por semana | Tempo de inatividade por mês | Tempo de inatividade por ano |
|---------|-------------------------------|------------------------------|------------------------------|
| 99%     | 1,68 hora                     | 7,2 horas                   | 3,65 dias                   |
| 99,9%   | 10,1 minutos                  | 43,2 minutos                | 8,76 horas                  |
| 99,95%  | 5 minutos                     | 21,6 minutos                | 4,38 horas                  |
| 99,99%  | 1,01 minuto                   | 4,32 minutos                | 52,56 minutos               |
| 99,999% | 6 segundos                    | 25,9 segundos               | 5,26 minutos                |

> **Importante:** Quanto mais "noves" o SLA possui, maior é a disponibilidade e menor é o tempo de inatividade tolerado. Porém, atingir níveis mais altos de SLA geralmente envolve arquiteturas mais complexas e custos mais elevados.

---

## Opções ao Criar uma Máquina Virtual

Quando se vai criar uma máquina virtual no Azure, é possível escolher inúmeras opções que influenciam diretamente no desempenho, na disponibilidade e no custo do recurso. Entre as principais, destacam-se:

- **Assinatura (Subscription):** define qual conta será cobrada pelos recursos utilizados pela VM.
- **Grupo de Recursos (Resource Group):** organiza os recursos relacionados dentro de um mesmo grupo lógico, facilitando o gerenciamento e a governança.
- **Nome da Máquina Virtual:** identificação única do recurso dentro do grupo de recursos.
- **Região (Region):** local físico do datacenter onde a VM será implantada. A escolha da região impacta na latência, no custo e na disponibilidade de serviços.
- **Opções de Disponibilidade (Availability Options):** define como a VM será protegida contra falhas. As principais opções são:
  - **Conjunto de Disponibilidade (Availability Set):** distribui as VMs entre domínios de falha e de atualização dentro de um mesmo datacenter.
  - **Zona de Disponibilidade (Availability Zone):** distribui as VMs entre datacenters fisicamente separados dentro de uma mesma região, oferecendo maior proteção contra falhas de datacenter.
  - **Conjunto de Dimensionamento de Máquinas Virtuais (VM Scale Set):** permite criar e gerenciar um grupo de VMs com balanceamento de carga e escalonamento automático.
- **Imagem (Image):** sistema operacional e softwares pré-instalados na VM (ex: Windows Server 2022, Ubuntu 24.04, etc.).
- **Tamanho (Size):** define a quantidade de vCPUs, memória RAM e capacidade de armazenamento temporário. Cada tamanho atende a diferentes cargas de trabalho (uso geral, computação intensiva, memória otimizada, etc.).
- **Tipo de Autenticação:** pode ser por **senha** ou por **chave pública SSH**, sendo a segunda opção mais segura e recomendada para ambientes Linux.
- **Portas de Entrada (Inbound Ports):** define quais portas serão liberadas para acesso externo à VM (ex: porta 22 para SSH, porta 3389 para RDP, porta 80 para HTTP).
- **Disco do Sistema Operacional (OS Disk):** tipo de disco utilizado para o sistema operacional, podendo ser **SSD Premium**, **SSD Standard** ou **HDD Standard**.
- **Rede Virtual (Virtual Network):** define a rede na qual a VM será conectada, permitindo a comunicação com outros recursos do Azure.
- **Sub-rede (Subnet):** segmento dentro da rede virtual onde a VM será posicionada.
- **IP Público (Public IP):** endereço IP acessível pela internet, necessário caso a VM precise ser acessada externamente.

> Ao lado de cada opção no portal do Azure, está um **ícone especial (ℹ️)** que apresenta uma breve descrição da configuração. Ao clicar nele, o usuário pode ser direcionado à **Documentação Oficial da Microsoft** referente à opção que estava visualizando. Isso é extremamente útil para quem está aprendendo, pois permite tirar dúvidas em tempo real durante a criação do recurso.

---

## Redundância nas Contas de Armazenamento

Algo de muita ajuda no desenvolvimento em nuvem é a estratégia do uso de **Redundância** nas contas de armazenamento. A redundância garante que os dados estejam protegidos contra falhas de hardware, interrupções de rede e até desastres naturais. O Azure oferece quatro modelos principais:

- **LRS (Locally Redundant Storage / Armazenamento com Redundância Local):** mantém **3 cópias** dos dados dentro de um **único datacenter** na região primária. É a opção mais barata, porém oferece menor proteção, pois se o datacenter inteiro falhar, os dados podem ser perdidos. Possui durabilidade de **11 noves** (99,999999999%).

- **ZRS (Zone-Redundant Storage / Armazenamento com Redundância de Zona):** distribui **3 cópias** dos dados entre **3 zonas de disponibilidade** diferentes dentro da mesma região. Oferece proteção contra falhas de um datacenter inteiro, já que os dados estão espalhados em locais fisicamente separados. Possui durabilidade de **12 noves** (99,9999999999%).

- **GRS (Geo-Redundant Storage / Armazenamento com Redundância Geográfica):** mantém **3 cópias no datacenter primário (LRS)** e replica mais **3 cópias** para uma **região secundária** a centenas de quilômetros de distância. Ao todo, são **6 cópias** dos dados. Oferece proteção contra desastres regionais completos. Possui durabilidade de **16 noves** (99,99999999999999%).

- **GZRS (Geo-Zone-Redundant Storage / Armazenamento com Redundância de Zona Geográfica):** combina o melhor do ZRS e do GRS. Distribui **3 cópias entre zonas de disponibilidade na região primária (ZRS)** e replica mais **3 cópias para uma região secundária (LRS)**. É a opção mais resiliente, protegendo contra falhas de datacenter, zona e região. Possui durabilidade de **16 noves** (99,99999999999999%).

| Modelo | Cópias | Escopo Primário | Região Secundária | Durabilidade |
|--------|--------|-----------------|-------------------|-------------|
| **LRS** | 3 | Único datacenter | ❌ Não | 11 noves |
| **ZRS** | 3 | 3 zonas de disponibilidade | ❌ Não | 12 noves |
| **GRS** | 6 | Único datacenter + região secundária | ✅ Sim | 16 noves |
| **GZRS** | 6 | 3 zonas + região secundária | ✅ Sim | 16 noves |

> Para quem está começando, uma boa forma de pensar na redundância é como fazer **backup em diferentes locais**: o LRS seria guardar todas as cópias na mesma gaveta; o ZRS seria distribuir em gavetas diferentes do mesmo escritório; o GRS seria manter cópias em outro escritório da cidade; e o GZRS seria distribuir nas gavetas do escritório atual e ainda manter cópias em outro escritório distante.

Esse laboratório ajudou a entender que a criação de uma máquina virtual no Azure vai muito além de simplesmente "ligar um servidor". É fundamental considerar a **disponibilidade, a redundância dos dados, a segurança e o custo** de cada configuração escolhida, pois essas decisões impactam diretamente na confiabilidade e no desempenho das aplicações hospedadas na nuvem.
