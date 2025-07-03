# Testes Automatizados de Login - Herokuapp

![QA](https://img.shields.io/badge/Testes-Automação-blue)
![Ferramenta](https://img.shields.io/badge/Selenium-Python-green)
![Tipo de Teste](https://img.shields.io/badge/Testes-Funcional-lightgrey)
![Python application](https://github.com/celiapaivab/qa-login-selenium-internet/actions/workflows/python-app.yml/badge.svg?branch=main)

---

## 📌 Sobre o Projeto

Este projeto realiza testes automatizados com **Selenium** e **Pytest**  no formulário de login do site [the-internet.herokuapp.com/login](https://the-internet.herokuapp.com/login).  
O foco é validar mensagens de sucesso e erro, além do funcionamento do botão de logout.

---

## 🎯 Objetivo do Projeto

- Automatizar os testes de login e logout no site de testes the-internet.herokuapp.com  
- Validar mensagens de sucesso e erro exibidas pelo sistema  
- Garantir que o fluxo de logout retorna corretamente ao formulário de login  

---

## 🔧 Tecnologias e Ferramentas

- Python
- Pytest
- Selenium WebDriver
- GitHub Actions

---

## ▶️ Como Executar

1. Clone o repositório:

```bash
git clone https://github.com/celiapaivab/qa-login-selenium-internet.git
cd qa-login-selenium-internet
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

---

## 🧾 Resultado

- Testes de login com credenciais válidas e inválidas executados com sucesso.  
- Validação de mensagens apropriadas para tentativas com campos vazios.  
- Teste de logout garantindo retorno ao formulário de login com a mensagem correta.  
- Pipeline configurado no GitHub Actions executando os testes automaticamente em cada push.

---

## 📚 Aprendizados

- Implementação prática de testes automatizados com Selenium e Pytest.  
- Como estruturar testes para diferentes cenários de login e logout.  
- Integração de testes automatizados com pipeline CI/CD no GitHub Actions.  
- Melhoria na organização do código com boas práticas para testes funcionais.

---

## 💡 Melhorias Futuras

- Adicionar testes para casos de recuperação de senha.  
- Implementar testes para múltiplos navegadores (cross-browser).  
- Criar relatórios detalhados em HTML para resultados de teste.  
- Integrar testes com ferramentas de monitoramento de bugs.

---

## 📂 Arquivos do Projeto

- `tests/` – Scripts de teste automatizados para login/logout  
- `pages/` – Page Object Model para o formulário de login e logout  
- `requirements.txt` – Dependências do projeto  
- `.github/workflows/python-app.yml` – Configuração do pipeline no GitHub Actions  

---

## 🇺🇸 Project Summary

This project implements automated tests using **Selenium** and **Pytest** for the login form on [the-internet.herokuapp.com/login](https://the-internet.herokuapp.com/login). The tests cover successful and unsuccessful login attempts, empty field validations, and logout functionality.  

The project also includes a continuous integration pipeline with GitHub Actions to run tests automatically on code pushes, ensuring the reliability of the login system.
