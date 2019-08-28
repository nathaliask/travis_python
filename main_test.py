from source import main

def test_dizer_ola():
	assert main.dizer_ola("Nathalia") == "Olá, Nathalia"

def test_dizer_ola_numeral():
	assert main.dizer_ola("Nathalia123") == "Olá, Nathalia123"

def test_dizer_ola_especial():
	assert main.dizer_ola("Nathalia↓") == "Olá, Nathalia↓"

def test_somar():
	assert main.somar(10, 10) == 20

def test_somar_neg():
	assert main.somar(10, -10) == 0

def test_somar_neg_neg():
	assert main.somar(-10, -10) == -20