lasse  Pilha :
    def  __init__ ( auto ):
        eu . itens  = []

    def  push ( auto , item ):
        """Adiciona um item ao topo da pilha."""
        self . itens . anexar ( item )

    def  pop ( auto ):
        """Remove e retorna o item do topo da pilha."""
        se  não for  eu mesmo . esta_vazia ():
            retornar  self . itens . pop ()
        return  None   # Retorna None se a pilha estiver vazia

    def  espiar ( self ):
        """Retorna o item do topo da pilha sem removê-lo."""
        se  não for  eu mesmo . esta_vazia ():
            retornar  itens próprios [ - 1 ]​
        return  None   # Retorna None se a pilha estiver vazia

    def  esta_vazia ( self ):
        """Verifique se a pilha está vazia."""
        retornar  len ( self . itens ) ==  0

    def  tamanho ( self ):
        """Retorna o número de elementos na pilha."""
        retornar  len ( self . itens )

    def  __str__ ( auto ):
        """Representação da pilha como string."""
        return  f"Pilha: { self . itens } "


# Exemplo de uso
pilha  =  Pilha ()
pilha . empurre ( 10 )
pilha . empurre ( 20 )
pilha . empurre ( 30 )

imprimir ( pilha )          # Pilha: [10, 20, 30]
print ( pilha . peek ())   # 30 (Topo da pilha)
print ( pilha . pop ())    # Remove e retorna 30
print ( pilha )          # Pilha: [10, 20]
