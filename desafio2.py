class ContaBancaria:
    def __init__(self, saldo=0.0, limite_saque=500.0, max_saques_dia=3):
        self.saldo = saldo
        self.limite_saque = limite_saque
        self.num_saques_dia = 0
        self.max_saques_dia = max_saques_dia
    
    def sacar(self, valor):
        if self.num_saques_dia >= self.max_saques_dia:
            print("Limite de saques diários atingido.")
            return False
        if valor > self.limite_saque:
            print(f"O valor máximo para saque é R$ {self.limite_saque}.")
            return False
        if valor > self.saldo:
            print("Saldo insuficiente.")
            return False
        
        self.saldo -= valor
        self.num_saques_dia += 1
        print(f"Saque de R$ {valor:.2f} realizado com sucesso.")
        return True
    
    def depositar(self, valor):
        if valor <= 0:
            print("O valor do depósito deve ser positivo.")
            return False
        
        self.saldo += valor
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
        return True
    
    def extrato(self):
        print("========== EXTRATO ==========")
        print(f"Saldo atual: R$ {self.saldo:.2f}")
        print(f"Saques realizados hoje: {self.num_saques_dia}/{self.max_saques_dia}")
        print("=============================")
