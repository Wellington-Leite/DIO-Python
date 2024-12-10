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
