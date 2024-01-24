class UrnaEletronica:
    def __init__(self):
        self.eleitores_registrados = {
            1001: "Adelardo Antonio", 1002: "Beatriz Bezerra", 1003: "Cristiano Castro",
            1004: "Diana Diniz", 1005: "Eliana Esperanca", 1006: "Francisco Fabiano",
            1007: "Giulia Gran", 1008: "Helena Hipno", 1009: "Indira Inter",
            1010: "Jacinto Jeremias", 1011: "Kaio Kleber", 1012: "Leandro Leite"
        }

        self.votos_presidente = {
            "11": "Armando Silva", "12": "Bernardo Sousa", "13": "Cristiano Lima", "B": "Branco", "N": "Nulo"
        }
        self.votos_senadores = {
            "101": "Augusto Rosa", "102": "Bruno Costa", "103": "Carlos Pereira",
            "104": "Diego Frota", "105": "Edson Martins", "B": "Branco", "N": "Nulo"
        }
        self.senha_tse = "12345"

        # Inicializa contadores para votos branco e nulo separadamente
        self.votos_branco_presidente = 0
        self.votos_nulo_presidente = 0
        self.votos_branco_senadores = 0
        self.votos_nulo_senadores = 0

        # Inicializa contadores para votos totais
        self.total_votos_presidente = 0
        self.total_votos_senadores = 0

        # Inicializa contadores para cada candidato
        for codigo in self.votos_presidente:
            setattr(self, f"presidente_{codigo}", 0)

        for codigo in self.votos_senadores:
            setattr(self, f"senador_{codigo}", 0)

        # Lista para rastrear os eleitores que já votaram
        self.eleitores_que_votaram = []

    def autenticar_tse(self):
        tentativas = 3  # Número de tentativas permitidas
        while tentativas > 0:
            senha = input("Digite a senha do TSE: ")
            if senha == self.senha_tse:
                return True
            else:
                print("Senha incorreta. Tente novamente.")
                tentativas -= 1

        print("Número máximo de tentativas excedido. Encerrando o programa.")
        return False

    def registrar_eleitor(self, titulo_eleitor):
        titulo_eleitor = int(titulo_eleitor)

        # Verifica se o eleitor já votou
        if titulo_eleitor in self.eleitores_que_votaram:
            print("Este eleitor já votou. Não é permitido votar novamente.")
            return False

        if titulo_eleitor in self.eleitores_registrados:
            eleitor_nome = self.eleitores_registrados[titulo_eleitor]

            print(f"\nDados do Eleitor:")
            print(f"Título: {titulo_eleitor}")
            print(f"Nome: {eleitor_nome}")

            confirmacao = input("Os dados estão corretos? (s/n): ").lower()

            if confirmacao != "s":
                print("Registro cancelado.")
                return False

            print("Eleitor já registrado.")
            self.votar(eleitor_nome)  # Direciona para a opção de votar
            self.eleitores_que_votaram.append(titulo_eleitor)  # Adiciona o eleitor à lista de eleitores que já votaram
            return True

        if titulo_eleitor not in self.eleitores_registrados:
            print("Eleitor não encontrado.")
            return False

    def votar(self, eleitor_nome):
        print("\nOpções de Votação:")
        while True:
            print("Para presidente:")
            for codigo, candidato in self.votos_presidente.items():
                print(f"Código {codigo} - {candidato}")

            presidente_codigo = input("\nDigite o código do candidato a presidente: ")

            if presidente_codigo in self.votos_presidente:
                presidente = self.votos_presidente[presidente_codigo]

                # Atualiza contadores de votos branco e nulo para presidente
                if presidente_codigo == "B":
                    self.votos_branco_presidente += 1
                elif presidente_codigo == "N":
                    self.votos_nulo_presidente += 1
                else:
                    # Atualiza contadores de votos para cada candidato a presidente
                    setattr(self, f"presidente_{presidente_codigo}", getattr(self, f"presidente_{presidente_codigo}") + 1)

                self.total_votos_presidente += 1
                break
            else:
                print("Código de voto para presidente inválido. Por favor, escolha uma opção válida.")

        while True:
            print("Para senador (1ª opção):")
            for codigo, candidato in self.votos_senadores.items():
                print(f"Código {codigo} - {candidato}")

            senador1_codigo = input("Digite o código do candidato a primeiro senador: ")

            if senador1_codigo in self.votos_senadores:
                senador1 = self.votos_senadores[senador1_codigo]

                # Atualiza contadores de votos branco e nulo para senador
                if senador1_codigo == "B":
                    self.votos_branco_senadores += 1
                elif senador1_codigo == "N":
                    self.votos_nulo_senadores += 1
                else:
                    # Atualiza contadores de votos para cada candidato a senador
                    setattr(self, f"senador_{senador1_codigo}", getattr(self, f"senador_{senador1_codigo}") + 1)

                self.total_votos_senadores += 1
                break
            else:
                print("Código de voto para o primeiro senador inválido. Por favor, escolha uma opção válida.")

        while True:
            print("Para senador (2ª opção):")
            for codigo, candidato in self.votos_senadores.items():
                print(f"Código {codigo} - {candidato}")

            senador2_codigo = input("Digite o código do candidato a segundo senador: ")

            if senador2_codigo in self.votos_senadores:
                senador2 = self.votos_senadores[senador2_codigo]

                # Atualiza contadores de votos branco e nulo para senador
                if senador2_codigo == "B":
                    self.votos_branco_senadores += 1
                elif senador2_codigo == "N":
                    self.votos_nulo_senadores += 1
                else:
                    # Atualiza contadores de votos para cada candidato a senador
                    setattr(self, f"senador_{senador2_codigo}", getattr(self, f"senador_{senador2_codigo}") + 1)

                self.total_votos_senadores += 1
                break
            else:
                print("Código de voto para o segundo senador inválido. Por favor, escolha uma opção válida.")

        print(f"\nEleitor {eleitor_nome} votou:")
        print(f"Presidente: {presidente}")
        print(f"Senador 1: {senador1}")
        print(f"Senador 2: {senador2}")

    def gerar_estatisticas(self):
        print("\nEstatísticas da Eleição:")
        print("Presidente:")
        print(f"Quantidade total de votos: {self.total_votos_presidente}")
        for codigo, candidato in self.votos_presidente.items():
            # Exclui branco e nulo para senador da contagem de votos para presidente
            if codigo not in ["B", "N"]:
                votos = getattr(self, f"presidente_{codigo}")
                percentagem = (votos / self.total_votos_presidente) * 100 if self.total_votos_presidente != 0 else 0
                print(f"{candidato}: {votos} votos ({percentagem:.2f}%)")

        # Mostra votos branco e nulo separadamente para presidente
        print("\nVotos em Branco e Nulo:")
        print(f"Branco: {self.votos_branco_presidente} votos")
        print(f"Nulo: {self.votos_nulo_presidente} votos")

        print("\nSenadores:")
        print(f"Quantidade total de votos: {self.total_votos_senadores}")
        for codigo, candidato in self.votos_senadores.items():
            # Exclui branco e nulo para presidente da contagem de votos para senador
            if codigo not in ["B", "N"]:
                votos = getattr(self, f"senador_{codigo}")
                percentagem = (votos / self.total_votos_senadores) * 100 if self.total_votos_senadores != 0 else 0
                print(f"{candidato}: {votos} votos ({percentagem:.2f}%)")

        # Mostra votos branco e nulo separadamente para senador
        print("\nVotos em Branco e Nulo:")
        print(f"Branco: {self.votos_branco_senadores} votos")
        print(f"Nulo: {self.votos_nulo_senadores} votos")


if __name__ == "__main__":
    urna = UrnaEletronica()

    if urna.autenticar_tse():
        while True:
            print("\nOpções:")
            print("1. Registrar Eleitor e Votar")
            print("2. Encerrar Votação e Gerar Estatísticas")

            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                titulo_eleitor = input("Digite o número do título de eleitor: ")
                urna.registrar_eleitor(titulo_eleitor)

            elif opcao == "2":
                senha_tse_digitada = input("Digite a senha do TSE: ")
                if senha_tse_digitada == urna.senha_tse:
                    urna.gerar_estatisticas()
                    break
                else:
                    print("Senha do TSE incorreta. Retornando ao menu principal.")

            else:
                print("Opção inválida. Tente novamente.")
    else:
        print("Autenticação falhou. Encerrando o programa.")
