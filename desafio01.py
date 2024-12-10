# 1 / 2 - Verificação de Integridade de Arquivos com Hashes

def verificar_hashes(lista_hashes):
  
     for hash_comparacao in lista_hashes:
        try:
            # Divide cada entrada em hash_calculado e hash_esperado
            hash_calculado, hash_esperado = hash_comparacao.split(",")
            
            # Remove espaços extras antes de comparar
            hash_calculado = hash_calculado.strip()
            hash_esperado = hash_esperado.strip()
            
            # Verifica a igualdade
            if hash_calculado == hash_esperado:
                print("Correto")
            else:
                print("Inválido")
        except ValueError:
            print(f"Formato inválido: {hash_comparacao}")
        
hashes_usuario = input()

lista_hashes = hashes_usuario.split(";")

verificar_hashes(lista_hashes)


# 2 / 2 - Simulação de Enumeração de Serviços em um Servidor
# Dicionário que mapeia números de portas aos serviços correspondentes
port_services = {
    21: "FTP",      # Serviço de transferência de arquivos
    22: "SSH",      # Secure Shell (acesso remoto seguro)
    23: "Telnet",   # Protocolo de acesso remoto inseguro
    25: "SMTP",     # Serviço de envio de emails
    53: "DNS",      # Serviço de tradução de nomes de domínio
    80: "HTTP",     # Protocolo de transferência de hipertexto (web)
    110: "POP3",    # Serviço de recebimento de emails
    143: "IMAP",    # Serviço de recebimento de emails com suporte a pastas
    443: "HTTPS",   # Protocolo seguro de transferência de hipertexto
    3306: "MySQL",  # Banco de dados MySQL
    3389: "RDP",    # Remote Desktop Protocol (Acesso remoto ao Windows)
    5432: "PostgreSQL", # Banco de dados PostgreSQL
    6379: "Redis"   # Banco de dados Redis
}

# Função que realiza a enumeração de serviços
def enumerate_services(ports):
    # Inicializamos uma lista para armazenar os serviços correspondentes
    services = []
    
 # Itera sobre cada porta fornecida na lista de portas
    for port in ports:
        # Verifica se a porta existe no dicionário de serviços
        if port in port_services:
            # Se existir, adicione o serviço correspondente à lista de serviços
            services.append(port_services[port])
        else:
            # Se a porta não estiver mapeada, adicione "Desconhecido"
            services.append("Desconhecido")
    
    return services

# Função principal que lida com a entrada do usuário e exibe o resultado:
def main():
    ports_input = input()
    
    # TODO: Converta a string de entrada para uma lista de inteiros (números de portas)
    # Utilize a função strip() para remove espaços em branco, e o split() para separar por vírgula
    
    ports = list(map(int, ports_input.strip().split(",")))
    
    # Chama a função de enumeração para obter a lista de serviços correspondentes
    services = enumerate_services(ports)
    
    
    print(services)


if __name__ == "__main__":
    main()
