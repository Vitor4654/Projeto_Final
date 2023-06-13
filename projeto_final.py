import json


def main_menu():
    print("==== Bem-vindo ao Sistema de Gestão de Turmas ====")
    print("Selecione uma opção:")
    print("1. Aluno")
    print("2. Professor")
    print("3. Coordenador")
    print("0. Sair")


def aluno_menu():
    print("\n==== Menu Aluno ====")
    print("Selecione uma opção:")
    print("1. Cadastrar novo aluno")
    print("2. Editar aluno cadastrado")
    print("3. Visualizar alunos cadastrados")
    print("4. Apagar aluno cadastrado")
    print("0. Voltar ao menu principal")


def professor_menu():
    print("\n==== Menu Professor ====")
    print("Selecione uma opção:")
    print("1. Cadastrar novo professor")
    print("2. Editar professor cadastrado")
    print("3. Ver dados de um professor cadastrado")
    print("4. Excluir um professor cadastrado")
    print("5. Visualizar turmas de um professor específico")
    print("6. Visualizar alunos da turma de um professor específico")
    print("0. Voltar ao menu principal")


def coordenador_menu():
    print("\n==== Menu Coordenador ====")
    print("Selecione uma opção:")
    print("1. Criar turma")
    print("2. Editar turma")
    print("3. Ver turma")
    print("4. Apagar turma")
    print("0. Voltar ao menu principal")


def cadastrar_aluno(alunos):
    nome = input("Digite o nome do aluno: ")
    if nome.isnumeric() or nome == "":
        print("Números ou espaços em branco são inválidos.")
    else:
        composto = nome.split()
        if len(composto) >= 2:
            matricula = str(len(alunos) + 1)
            alunos[matricula] = nome
            print(f"Aluno {nome} cadastrado com matrícula {matricula}")
            return True
        else:
            print("Nome inválido, ele deve ser nome composto.")
        return False
        

def editar_aluno(alunos):
    matricula = input("Digite a matrícula do aluno que deseja editar: ")
    if matricula.isnumeric():
        if matricula in alunos:
            nome = input("Digite o novo nome do aluno: ")
            alunos[matricula] = nome
            print(f"Aluno com matrícula {matricula} atualizado")
        else:
            print("Aluno não encontrado")
    else:
        print("Letras ou espaços em branco são inválidos.")


def visualizar_alunos(alunos):
    if alunos:
        print("\n==== Alunos Cadastrados ====")
        for matricula, nome in alunos.items():
            print(f"Matrícula: {matricula} | Nome: {nome}")
    else:
        print("Nenhum aluno cadastrado")


def apagar_aluno(alunos):
    matricula = input("Digite a matrícula do aluno que deseja apagar: ")
    if matricula.isnumeric(): 
        if matricula in alunos:
            nome = alunos[matricula]
            del alunos[matricula]
            print(f"Aluno {nome} com matrícula {matricula} apagado")
        else:
            print("Aluno não encontrado")
    else:
        print("Letras ou espaços em branco são inválidos.")


def cadastrar_professor(professores):
    nome = input("Digite o nome do professor: ")
    if nome.isnumeric() or nome == "":
        print("Números ou espaços em branco são inválidos.")
    else:
        composto = nome.split()
        if len(composto) >= 2:
            matricula = str(len(professores) + 1)
            professores[matricula] = nome
            print(f"Professor {nome} cadastrado com matrícula {matricula}")
            return True
        else:
            print("Nome inválido, ele deve ser nome composto.")
        return False


def editar_professor(professores):
    matricula = input("Digite a matrícula do professor que deseja editar: ")
    if matricula.isnumeric():
        if matricula in professores:
            nome = input("Digite o novo nome do professor: ")
            professores[matricula] = nome
            print(f"Professor com matrícula {matricula} atualizado")
        else:
            print("Professor não encontrado")
    else:
        print("Letras ou espaços em branco são inválidos.")


def ver_dados_professor(professores):
    matricula = input("Digite a matrícula do professor que deseja visualizar: ")
    if matricula in professores:
        nome = professores[matricula]
        print(f"Matrícula: {matricula} | Nome: {nome}")
    else:
        print("Professor não encontrado")


def excluir_professor(professores, turmas):
    matricula = input("Digite a matrícula do professor que deseja excluir: ")
    if matricula.isnumeric():
        if matricula in professores:
            nome = professores[matricula]
            del professores[matricula]
            turmas = {turma: prof for turma, prof in turmas.items() if prof != matricula}
            print(f"Professor {nome} com matrícula {matricula} excluído")
        else:
            print("Professor não encontrado")
    else:
        print("Letras ou espaços em branco são inválidos.")
        

def visualizar_turmas_professor(turmas, professores):
    matricula = input("Digite a matrícula do professor: ")
    if matricula in professores:
        turmas_professor = [turma for turma, prof in turmas.items() if prof == matricula]
        if turmas_professor:
            print(f"\n==== Turmas do Professor com matrícula {matricula} ====")
            for turma in turmas_professor:
                print(f"Disciplina: {turma} | Professor: {professores[matricula]}")
        else:
            print(f"O professor com matrícula {matricula} não está associado a nenhuma turma")
    else:
        print("Professor não encontrado")


def visualizar_alunos_turma(turmas, alunos, professores):
    turma = input("Digite o nome da turma (disciplina): ")
    if turma in turmas:
        matricula_professor = turmas[turma]
        alunos_turma = [alunos[matricula] for matricula in alunos if matricula in turmas.values() and turmas[turma] == matricula]
        print(f"\n==== Alunos da turma de {turma} ====")
        print(f"Professor: {professores[matricula_professor]}")
        if alunos_turma:
            for aluno in alunos_turma:
                print(f"Aluno: {aluno}")
        else:
            print("Nenhum aluno matriculado nessa turma")
    else:
        print("Turma não encontrada")


def criar_turma(turmas, professores, alunos):
    disciplina = input("Digite o nome da disciplina (turma): ")
    if disciplina in turmas:
        print("A turma já existe")
    else:
        print("Professores disponíveis:")
        for matricula, nome in professores.items():
            print(f"Matrícula: {matricula} | Nome: {nome}")
        matricula_professor = input("Digite a matrícula do professor da turma: ")
        if matricula_professor in professores:
            print("Alunos disponíveis:")
            for matricula, nome in alunos.items():
                print(f"Matrícula: {matricula} | Nome: {nome}")
            alunos_turma = input("Digite as matrículas dos alunos da turma (separados por vírgula): ").split(",")
            alunos_turma = [matricula.strip() for matricula in alunos_turma]
            alunos_turma = [matricula for matricula in alunos_turma if matricula in alunos]
            if alunos_turma:
                turmas[disciplina] = matricula_professor
                print(f"Turma de {disciplina} criada com sucesso")
            else:
                print("Nenhum aluno válido selecionado")
        else:
            print("Professor não encontrado")


def editar_turma(turmas, professores, alunos):
    disciplina = input("Digite o nome da disciplina (turma) que deseja editar: ")
    if disciplina in turmas:
        print("Professores disponíveis:")
        for matricula, nome in professores.items():
            print(f"Matrícula: {matricula} | Nome: {nome}")
        matricula_professor = input("Digite a nova matrícula do professor da turma: ")
        if matricula_professor in professores:
            print("Alunos disponíveis:")
            for matricula, nome in alunos.items():
                print(f"Matrícula: {matricula} | Nome: {nome}")
            alunos_turma = input("Digite as novas matrículas dos alunos da turma (separados por vírgula): ").split(",")
            alunos_turma = [matricula.strip() for matricula in alunos_turma]
            alunos_turma = [matricula for matricula in alunos_turma if matricula in alunos]
            if alunos_turma:
                turmas[disciplina] = matricula_professor
                print(f"Turma de {disciplina} atualizada com sucesso")
            else:
                print("Nenhum aluno válido selecionado")
        else:
            print("Professor não encontrado")
    else:
        print("Turma não encontrada")


def ver_turma(turmas, professores):
    disciplina = input("Digite o nome da disciplina (turma) que deseja visualizar: ")
    if disciplina in turmas:
        matricula_professor = turmas[disciplina]
        nome_professor = professores[matricula_professor]
        print(f"\n==== Turma de {disciplina} ====")
        print(f"Professor: {nome_professor}")
    else:
        print("Turma não encontrada")


def apagar_turma(turmas):
    disciplina = input("Digite o nome da disciplina (turma) que deseja apagar: ")
    if disciplina in turmas:
        del turmas[disciplina]
        print(f"Turma de {disciplina} apagada")
    else:
        print("Turma não encontrada")


def salvar_dados(alunos, professores, turmas):
    with open("alunos.json", "w") as file:
        json.dump(alunos, file)
    with open("professores.json", "w") as file:
        json.dump(professores, file)
    with open("turmas.json", "w") as file:
        json.dump(turmas, file)


def carregar_dados():
    try:
        with open("alunos.json", "r") as file:
            alunos = json.load(file)
    except FileNotFoundError:
        alunos = {}
    try:
        with open("professores.json", "r") as file:
            professores = json.load(file)
    except FileNotFoundError:
        professores = {}
    try:
        with open("turmas.json", "r") as file:
            turmas = json.load(file)
    except FileNotFoundError:
        turmas = {}
    return alunos, professores, turmas


def interface():
    alunos, professores, turmas = carregar_dados()

    while True:
        main_menu()
        opcao = input("Digite a opção desejada: ")
        if opcao == "1":
            while True:
                aluno_menu()
                opcao_aluno = input("Digite a opção desejada: ")
                if opcao_aluno == "1":
                    cadastrar_aluno(alunos)
                elif opcao_aluno == "2":
                    editar_aluno(alunos)
                elif opcao_aluno == "3":
                    visualizar_alunos(alunos)
                elif opcao_aluno == "4":
                    apagar_aluno(alunos)
                elif opcao_aluno == "0":
                    break
                else:
                    print("Opção inválida")
        elif opcao == "2":
            while True:
                professor_menu()
                opcao_professor = input("Digite a opção desejada: ")
                if opcao_professor == "1":
                    cadastrar_professor(professores)
                elif opcao_professor == "2":
                    editar_professor(professores)
                elif opcao_professor == "3":
                    ver_dados_professor(professores)
                elif opcao_professor == "4":
                    excluir_professor(professores, turmas)
                elif opcao_professor == "5":
                    visualizar_turmas_professor(turmas, professores)
                elif opcao_professor == "6":
                    visualizar_alunos_turma(turmas, alunos, professores)
                elif opcao_professor == "0":
                    break
                else:
                    print("Opção inválida")
        elif opcao == "3":
            while True:
                coordenador_menu()
                opcao_coordenador = input("Digite a opção desejada: ")
                if opcao_coordenador == "1":
                    criar_turma(turmas, professores, alunos)
                elif opcao_coordenador == "2":
                    editar_turma(turmas, professores, alunos)
                elif opcao_coordenador == "3":
                    ver_turma(turmas, professores)
                elif opcao_coordenador == "4":
                    apagar_turma(turmas)
                elif opcao_coordenador == "0":
                    break
                else:
                    print("Opção inválida")
        elif opcao == "0":
            salvar_dados(alunos, professores, turmas)
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida")


interface()
