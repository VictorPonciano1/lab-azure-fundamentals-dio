# LABORATÓRIO 7: DESAFIO DE CÓDIGO - EXPLORANDO ARQUITETURA E SERVIÇOS AZURE COM LÓGICA DE PROGRAMAÇÃO

# Captura a entrada do usuário
resposta = input()

# Função responsável por receber um componente e retornar sua respectiva descrição.
def identificar_recurso(recurso):

    # Estrutura if/elif/else
    if recurso == "Azure Role-Based Access Control":
        return "Possibilita um gerenciamento de acesso refinado dos recursos"
        
    elif recurso == "Microsoft Entra ID":
        return "Serviço de gerenciamento de identidades e acessos"
        
    elif recurso == "Multi-Factor Authentication":
        return "Proporciona uma camada adicional de segurança"
        
    elif recurso == "Azure Key Vault":
        return "Permite armazenar e acessar segredos de maneira segura"
        
    elif recurso == "Azure Security Center":
        return "Oferece visibilidade e controle sobre a segurança dos recursos"
        
    else:
        # O else funciona como o "default"
        return "Digite uma opção válida e de forma correta."

print(identificar_recurso(resposta))

