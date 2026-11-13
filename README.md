# Atividade 4: Testes Automatizados do LocalEats

**Unidade Curricular:** Qualidade de Software  
**Projeto:** LocalEats  
**Estudante:** Izadora Calvetti Souza  
**Sistema testado:** [LocalEats](https://local-eats-unisenac.vercel.app/)

---

## 1. Identificação das Responsabilidades

| ID | Integrante | Tipo | Comportamento verificado | Arquivo e função |
| :--- | :--- | :--- | :--- | :--- |
| **TU01** | Izadora Calvetti Souza | Unitário | Pedido atinge o valor mínimo (limite de R$ 30,00) | `tests/test_regras.py::test_pedido_atinge_valor_minimo_no_limite` |
| **TU02** | Izadora Calvetti Souza | Unitário | Pedido abaixo do valor mínimo retorna False | `tests/test_regras.py::test_pedido_abaixo_do_valor_minimo` |
| **TU03** | Izadora Calvetti Souza | Unitário | Pedido com valor negativo gera exceção ValueError | `tests/test_regras.py::test_pedido_com_valor_negativo_gera_erro` |
| **TF01** | Izadora Calvetti Souza | Funcional | Carregamento e interação na interface do LocalEats | `tests/test_localeats.py::test_navegacao_e_filtro_pagina_inicial` |

---

## 2. Registro do Ciclo TDD

**TDD de Izadora Calvetti Souza**
* **Regra escolhida:** Regra 1 — Verificar valor mínimo do pedido (`pedido_atingiu_valor_minimo(valor_pedido)`).
* **Primeiro teste escrito:** `test_pedido_atinge_valor_minimo_no_limite`, verificando se um pedido de valor `30` retorna `True`.
* **Por que o teste falhou inicialmente:** A função `pedido_atingiu_valor_minimo` ainda não existia no arquivo `regras.py` (gerando `ImportError` / `NameError`).
* **Implementação mínima realizada:** Criação da função `def pedido_atingiu_valor_minimo(valor_pedido): return True` para fazer o primeiro teste passar (Green).
* **Segundo teste escrito:** `test_pedido_abaixo_do_valor_minimo`, passando o valor `29.90` e esperando `False` ( além do teste para valores negativos esperando `ValueError`).
* **Melhoria ou refatoração realizada:** Atualização da lógica para comparar `return valor_pedido >= 30.0`, adição da validação condicional `if valor_pedido < 0: raise ValueError(...)`. 

---

## 3. Explicação Individual do Teste Desenvolvido

**Responsável:** Izadora Calvetti Souza  
**Teste explicado:** `TU01` e `TU02` (`tests/test_regras.py`)

Fiz primeiramente os testes unitários. 
Como a regra de negócio estabelece que pedidos a partir de R$ 30,00 são válidos, o `TU01` testa exatamente isso (`30`), 
garantindo que o operador  inclua o limite (`>=` e não apenas `>`).
Já o `TU02` testa o valor abaixo do limite (`29.90`), fazendo com que pedidos abaixo desse valor sejam bloqueados com retorno `False`. 
O `TU03` valida o tratamento de exceções com `pytest.raises(ValueError)` para impedir entradas inválidas (valores negativos)


Uso de inteligência artificial
Ferramenta utilizada: Gemini 

Como a ferramenta foi utilizada: Para auxílio no texto do README. 

