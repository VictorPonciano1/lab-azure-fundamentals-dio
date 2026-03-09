# LABORATÓRIO 6: DESAFIO DE CÓDIGO - EXPLORANDO ARQUITETURA E SERVIÇOS AZURE COM LÓGICA DE PROGRAMAÇÃO

# Captura a entrada do usuário
resposta = input()

# Função responsável por receber um componente e retornar sua respectiva descrição.
def identificar_servico(servico):

    # Estrutura if/elif/else
    if servico == "Arquivos do Azure":
        return "Armazenamento de arquivos compartilhados acessíveis por meio de SMB"
        
    elif servico == "Blob do Azure":
        return "Armazenamento de arquivos grandes e não estruturados"
        
    elif servico == "Fila do Azure":
        return "Armazenamento de mensagens para comunicação entre aplicações"
        
    elif servico == "Tabelas do Azure":
        return "Armazenamento de dados estruturados não relacionais em tabelas"
        
    elif servico == "Disco do Azure":
        return "Armazenamento de alto desempenho para máquinas virtuais"
        
    else:
        # O else funciona como o "default"
        return "Digite uma opção válida e de forma correta."

print(identificar_servico(resposta))
