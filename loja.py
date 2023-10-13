# Definicao da classe loja, a classe central do programa, que ira gerir todas as acoes de manipulacao de inventario e 
# funcoes para que o usuario possa modificar a loja

    def iniciar_compra(self,cliente:Pessoa):
        if self.Compra_aberta == None:
            print("Erro: Ja existes uma compra aberta")
            return None
        self.Compra_aberta = Compra(cliente)
    
    def buscar_compra(self,codigo):
        for produto in self.produtos:
            if produto.codigo == codigo:
                return produto
        return None
    
    def cancelar_compra(self):
        self.Compra_aberta = None
        
    def finalizar_compra(self):
        self.Compras.append(self.Compra_aberta)
        for item in self.Compra_aberta.itens:
            for i in range(len(self.produtos)):
                if self.produtos[i].codigo == item.produto.codigo:
                    self.produtos[i].registrar_venda(item.produto.quantidade_estoque)
        self.Compra_aberta = None   
  