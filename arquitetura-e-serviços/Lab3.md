# LABORATÓRIO - ARMAZENAMENTO AZURE

## Contas de Armazenamento (Storage Accounts)

A Conta de Armazenamento é o recurso principal pra guardar qualquer tipo de dado no Azure. Ela agrupa todos os serviços de armazenamento — blobs, arquivos, filas e tabelas — tudo num lugar só.

Na hora de criar, a gente define:

- **Nome da conta**: único no mundo inteiro, só letras minúsculas e números (3 a 24 caracteres). Ele vira parte da URL de acesso (ex: `meustorage.blob.core.windows.net`).
- **Região**: onde os dados ficam fisicamente (ex: Brazil South).
- **Desempenho**: **Standard** (HDD, mais barato) ou **Premium** (SSD, mais rápido).
- **Redundância**: quantas cópias e onde (LRS, ZRS, GRS, GZRS).

---

## Serviços de Armazenamento

### Blob Storage

Serve pra guardar **qualquer tipo de arquivo** — imagens, vídeos, backups, logs. Os dados ficam organizados em **containers** (tipo pastas).

Tipos de blob: **Block Blob** (arquivos em geral), **Append Blob** (logs, só acrescenta) e **Page Blob** (discos de VMs).

As **camadas de acesso** ajudam a economizar:

| Camada | Uso | Armazenamento | Acesso |
|--------|-----|---------------|--------|
| **Hot** | Dados acessados o tempo todo | Mais caro | Barato |
| **Cool** | Pouca frequência (mín. 30 dias) | Mais barato | Mais caro |
| **Cold** | Raramente acessados (mín. 90 dias) | Ainda mais barato | Ainda mais caro |
| **Archive** | Quase nunca acessados (mín. 180 dias) | O mais barato | O mais caro + demora |

> Resumindo: quanto menos acessa, mais barato pra guardar, porém mais caro e demorado pra buscar. É tipo self-storage: quanto mais longe, mais barato o aluguel rs.

---

### File Storage

Compartilhamento de arquivos na nuvem usando protocolo **SMB** — o mesmo das pastas de rede do Windows. Dá pra montar direto no Windows, Linux ou macOS como se fosse uma pasta de rede normal. Muito usado pra migrar file servers antigos pra nuvem.

### Queue Storage

Serviço de **mensageria** com filas. Uma parte da aplicação coloca mensagens na fila e outra parte consome depois, sem travar ninguém. Cada mensagem tem até 64 KB e uma fila suporta milhões delas. Ideal pra desacoplar componentes de uma aplicação.

### Table Storage

Banco de dados **NoSQL** sem esquema fixo. Cada registro é uma entidade identificada por **PartitionKey** e **RowKey**. Bom pra logs, metadados e dados de configuração em grande volume.

---

## Migração de Dados

- **AzCopy**: ferramenta de linha de comando pra copiar dados de/para Storage Accounts. Sincronização unidirecional.
- **Storage Explorer**: aplicativo com interface gráfica — arrastar, soltar, criar containers, tudo visualmente.
- **Azure Data Box**: pra volumes gigantes (TB/PB). A Microsoft manda um dispositivo físico, você copia os dados e devolve. Mais rápido que transferir pela internet.

---

Esse laboratório mostrou que armazenamento no Azure vai além de só guardar arquivo. Saber escolher entre blob, file, queue ou table — e a camada de acesso certa — faz toda a diferença no custo e na performance.
