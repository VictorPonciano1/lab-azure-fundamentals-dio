# LABORATÓRIO - MONITORAMENTO

Neste laboratório foram exploradas as principais ferramentas de monitoramento do Azure: o **Azure Monitor**, o **Service Health** e o **Advisor**. Essas ferramentas trabalham juntas para garantir que os recursos estejam funcionando corretamente, que problemas sejam identificados rapidamente e que o ambiente esteja sempre otimizado.

---

## Azure Monitor

O **Azure Monitor** é a ferramenta central de monitoramento do Azure. Ele traz uma **visão completa de tudo que está acontecendo** nos recursos — desde máquinas virtuais até contas de armazenamento.

Dentro do Monitor, é possível acessar diversos recursos:

- **Application Insights:** monitora o desempenho e o comportamento de aplicações web em tempo real, identificando erros, lentidão e gargalos
- **Métricas:** exibe dados como uso de CPU, memória, disco e rede dos recursos
- **Alertas:** permite criar notificações automáticas quando algo sai do normal (ex: CPU de uma VM ultrapassando 90%)
- **Análise de VMs e Contas de Storage:** permite acompanhar o status e o desempenho desses recursos de forma centralizada

Além disso, dentro do Monitor também é possível fazer a **validação dos serviços**, verificando se tudo está operando como esperado.

> Pensando de forma simples, o Azure Monitor é como um **painel de controle de um carro**: ele mostra a velocidade, o combustível, a temperatura do motor e acende luzes de alerta quando algo precisa de atenção.

---

## Service Health

O **Service Health** é a ferramenta que mostra a **saúde dos serviços do Azure** que você está utilizando. Enquanto o Monitor foca nos seus recursos, o Service Health foca nos **serviços da Microsoft** por trás deles.

Ele oferece uma série de validações que ajudam a entender:

- Se algum serviço do Azure está **disponível ou indisponível** no momento
- Se os seus recursos estão sendo **afetados** por algum problema na infraestrutura da Microsoft
- Se existem **manutenções planejadas** que podem impactar o uso dos serviços no futuro

Isso é muito útil porque nem toda falha é culpa da sua configuração — às vezes o próprio Azure está passando por um problema ou por uma manutenção programada, e o Service Health avisa isso com antecedência.

> Se o Azure Monitor é o painel do carro, o **Service Health** seria o aplicativo de trânsito: ele avisa se a estrada (infraestrutura do Azure) está livre, congestionada ou em obras.

---

## Advisor (Assistente do Azure)

O **Advisor** é o assistente inteligente do Azure que analisa os recursos e fornece **recomendações práticas** para melhorar o ambiente. Ele organiza as sugestões em cinco categorias principais:

| Categoria | O que avalia |
|-----------|-------------|
| **Custo** | Identifica recursos subutilizados ou formas de economizar (ex: redimensionar uma VM que está grande demais) |
| **Segurança** | Aponta vulnerabilidades e sugere melhorias de proteção (integrado ao Microsoft Defender para Nuvem) |
| **Confiabilidade** | Recomenda práticas para aumentar a disponibilidade dos recursos (ex: adicionar redundância) |
| **Excelência Operacional** | Sugere melhorias na organização e nos processos (ex: aplicar tags, configurar alertas) |
| **Performance** | Identifica gargalos e sugere otimizações para melhorar a velocidade e o desempenho |

> O Advisor funciona como um **consultor gratuito** que fica analisando seu ambiente 24h por dia e dizendo: "olha, você pode economizar aqui", "esse recurso está sem proteção" ou "essa VM está lenta, considere trocar o tamanho". Vale a pena consultar ele com frequência.

---

Esse laboratório ajudou a entender que monitorar o ambiente no Azure não é opcional — é essencial. O **Monitor** mostra o que está acontecendo, o **Service Health** avisa sobre problemas externos e manutenções, e o **Advisor** dá recomendações para melhorar continuamente. Juntos, eles garantem mais **controle, segurança e eficiência** no uso da nuvem.
