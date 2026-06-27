"""Testes unitários dos validadores de CPF e e-mail.

Mantemos a suíte propositalmente pequena: 1 caso válido + 1 caso inválido
para cada validador. O suficiente para o aluno acompanhar o ciclo TDD
sem se afogar em código de teste.

Os capítulos 5 (TDD) e 10 (atividade prática) sugerem novos testes
para cobrir casos de borda — adicione-os à medida que evoluir o projeto.
"""

from src.validators import validar_cpf, validar_email


def test_aceita_cpf_valido():
    assert validar_cpf("111.444.777-35") is True


def test_rejeita_cpf_com_digito_verificador_errado():
    assert validar_cpf("111.444.777-30") is False


def test_aceita_email_valido():
    assert validar_email("aluno@ufopa.edu.br") is True


def test_rejeita_email_sem_arroba():
    assert validar_email("semarroba.com") is False


def test_aceita_cpf_valido():
    assert validar_cpf("111.444.777-35") is True


def test_rejeita_cpf_com_tamanho_invalido():
    assert validar_cpf("123") is False


def validar_cpf(cpf: str) -> bool:
    apenas_digitos = cpf.replace(".", "").replace("-", "")
    if len(apenas_digitos) != 11:
        return False
    return True


def test_rejeita_cpf_com_todos_digitos_iguais():
    assert validar_cpf("11111111111") is False


def validar_cpf(cpf: str) -> bool:
    apenas_digitos = cpf.replace(".", "").replace("-", "")
    if len(apenas_digitos) != 11:
        return False
    if len(set(apenas_digitos)) == 1:
        return False
    return True


def test_rejeita_cpf_com_digito_verificador_errado():
    assert validar_cpf("111.444.777-30") is False


def validar_cpf(cpf: str) -> bool:
    apenas_digitos = cpf.replace(".", "").replace("-", "")
    if len(apenas_digitos) != 11 or not apenas_digitos.isdigit():
        return False
    if len(set(apenas_digitos)) == 1:
        return False

    # primeiro dígito verificador
    soma = sum(int(apenas_digitos[i]) * (10 - i) for i in range(9))
    primeiro = (soma * 10) % 11
    if primeiro == 10:
        primeiro = 0

    # segundo dígito verificador
    soma = sum(int(apenas_digitos[i]) * (11 - i) for i in range(10))
    segundo = (soma * 10) % 11
    if segundo == 10:
        segundo = 0

    return apenas_digitos[9] == str(primeiro) and apenas_digitos[10] == str(segundo)


"""# tests/test_validators.py
def test_aceita_cnpj_valido():
    assert validar_cnpj("11.222.333/0001-81") is True"""
