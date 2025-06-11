# 🔐 Testes Automatizados de Login - Herokuapp

![QA](https://img.shields.io/badge/Testes-Automação-blue)
![Ferramenta](https://img.shields.io/badge/Selenium-Python-green)
![Tipo de Teste](https://img.shields.io/badge/Testes-Funcional-lightgrey)
![Python application](https://github.com/celiapaivab/qa-login-selenium-internet/actions/workflows/python-app.yml/badge.svg?branch=main)


---

Este projeto realiza testes automatizados com **Selenium** e **Pytest**  no formulário de login do site [the-internet.herokuapp.com/login](https://the-internet.herokuapp.com/login).  
O foco é validar mensagens de sucesso e erro, além do funcionamento do botão de logout.

---

## ✅ Tecnologias utilizadas

- Python
- Pytest
- Selenium WebDriver
- GitHub Actions

---

## 📋 Testes Implementados

- ✅ Login com credenciais válidas
- ✅ Login com credenciais inválidas
- ✅ Login com campos vazios
- ✅ Logout com verificação de mensagem e retorno ao formulário

---

## 🚀 Como executar localmente

1. Clone o repositório:

```bash
git clone https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git
cd SEU_REPOSITORIO
```

2. Crie e ative um ambiente virtual:

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate   # Windows
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

4. Execute os testes:

```bash
pytest tests/
```
