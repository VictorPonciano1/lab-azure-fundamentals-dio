# LABORATÓRIO - GERENCIAMENTO E IMPLANTAÇÃO

Neste laboratório foram exploradas as diferentes formas de **criar e gerenciar recursos** no Azure. Além do portal com interface gráfica, existem ferramentas de linha de comando e linguagens declarativas que podem ser mais eficientes dependendo da demanda e do cenário.

---

## Portal do Azure

O **Portal do Azure** é a forma mais visual e intuitiva de criar e gerenciar recursos. Toda a interação acontece pela interface gráfica — clicando em botões, preenchendo formulários e navegando por menus.

A grande vantagem é que **não é necessário saber linha de comando** para utilizá-lo. O portal já faz tudo por trás: quando você clica em "Criar" uma VM, por exemplo, ele executa os comandos automaticamente.

Para quem está começando, o portal é o melhor ponto de partida, pois permite visualizar tudo de forma clara e aprender como os recursos se relacionam.

> Porém, conforme a demanda cresce — como criar dezenas de recursos de uma vez — usar apenas o portal pode se tornar lento e repetitivo. É aí que entram as ferramentas de linha de comando.

---

## Cloud Shell

O **Cloud Shell** é um terminal de linha de comando que roda **diretamente no navegador**, dentro do portal do Azure. Ele permite criar e gerenciar recursos usando comandos, sem precisar instalar nada no computador.

Algumas características importantes:

- É necessário ter uma **Storage Account (Conta de Armazenamento)** associada à sua conta para poder usar o Cloud Shell — ela armazena os arquivos e configurações dos comandos
- Oferece duas opções de terminal:
  - **PowerShell:** linguagem de comandos da Microsoft, mais comum em ambientes Windows
  - **Bash:** terminal padrão do Linux, mais utilizado por desenvolvedores

Com o Cloud Shell, cada recurso pode ser gerenciado **individualmente** por linha de comando. Por exemplo, é possível usar a CLI para alterar configurações de uma VNet que já existe, sem precisar navegar por toda a interface do portal.

> Pensando de forma simples: o portal é como montar um móvel seguindo um manual com figuras, enquanto o Cloud Shell é como montar o mesmo móvel usando uma lista de instruções escritas — o resultado é o mesmo, mas a forma de chegar lá é diferente.

---

## Escolhendo a Ferramenta Certa

A **demanda** e o cenário podem influenciar diretamente na ferramenta utilizada para governança e implantação:

| Cenário | Ferramenta Recomendada |
|---------|----------------------|
| Criar um recurso pontual para teste | **Portal do Azure** — rápido e visual |
| Gerenciar um recurso específico que já existe | **Cloud Shell (CLI)** — direto e objetivo |
| Criar vários recursos repetidamente | **Linha de comando / Scripts** — automatiza o processo |
| Implantar ambientes inteiros de forma padronizada | **Linguagem declarativa (Bicep / ARM Templates)** — infraestrutura como código |

---

## Bicep — Linguagem Declarativa do Azure

O **Bicep** é uma linguagem declarativa usada no Azure para definir e implantar recursos como código. Em vez de clicar no portal ou digitar comandos um por um, você escreve um arquivo descrevendo **o que quer criar** e o Azure se encarrega de **como criar**.

A diferença entre uma abordagem **imperativa** e **declarativa** é:

- **Imperativa (CLI/PowerShell):** você diz **passo a passo** o que fazer → "crie uma rede, depois crie uma VM, depois associe a VM à rede"
- **Declarativa (Bicep):** você descreve **o estado final desejado** → "quero uma VM conectada a uma rede" — e o Azure resolve os passos

Vantagens do Bicep:

- Código mais **limpo e legível** comparado aos ARM Templates (JSON)
- Facilita a **reutilização** — um mesmo arquivo pode criar ambientes iguais em diferentes regiões
- Permite **versionamento** — o arquivo pode ser salvo no Git e acompanhado como qualquer outro código
- Garante **consistência** — o ambiente criado será sempre igual, sem variações manuais

> O Bicep é como uma **planta de engenharia**: você desenha como quer que o prédio fique e entrega para a construtora (Azure) executar. Não importa quantas vezes você entregue a mesma planta, o resultado será sempre o mesmo prédio.

---

Esse laboratório ajudou a entender que existem **várias formas de gerenciar e implantar recursos** no Azure, e que a escolha da ferramenta certa depende do cenário. Para tarefas simples e pontuais, o portal resolve. Para automação e padronização em escala, ferramentas como o Cloud Shell e o Bicep são muito mais eficientes.
