# LABORATÓRIO 5: DESAFIO DE CÓDIGO - EXPLORANDO ARQUITETURA E SERVIÇOS AZURE COM LÓGICA DE PROGRAMAÇÃO

# Captura a entrada do usuário
resposta = input()

# Função responsável por receber um componente e retornar sua respectiva descrição.
def identificar_componente(componente):

    # Estrutura if/elif/else
    if componente == "Regiões do Azure":
        return "Localizações geográficas onde os serviços são disponibilizados"
        
    elif componente == "Zonas de Disponibilidade":
        return "Garante alta disponibilidade ao isolar falhas"
        
    elif componente == "Datacenters":
        return "Instalações físicas que abrigam servidores e outros recursos"
        
    elif componente == "Assinaturas":
        return "Unidades de faturamento que agrupam recursos e serviços do Azure"
        
    elif componente == "Grupos de Gerenciamento":
        return "Estruturas hierárquicas que gerenciam múltiplas assinaturas"
        
    else:
        # O else funciona como o "default"
        return "Digite uma opção válida e de forma correta."

print(identificar_componente(resposta))
