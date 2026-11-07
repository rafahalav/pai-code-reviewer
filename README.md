# 🔍 PAI Code Reviewer - Analisador de Código Python

Ferramenta de revisão de código Python assistida por IA, focada em identificar bugs, vulnerabilidades de segurança, problemas de performance (Big O) e conformidade com PEP 8.

## 🎯 Sobre o Projeto

Enquanto o **PAI AI Coder** gera código, o **PAI Code Reviewer** avalia e melhora código existente. Esta ferramenta demonstra habilidades essenciais para **Treinamento e Avaliação de IA (RLHF)**:

- **Análise Crítica:** Capacidade de identificar problemas em código gerado por IA ou humanos.
- **Avaliação de Qualidade:** Julgamento de segurança, performance e manutenibilidade.
- **Feedback Construtivo:** Explicações didáticas sobre problemas e soluções.
- **Conformidade com Padrões:** Verificação rigorosa de PEP 8 e boas práticas da indústria.

## ✨ Destaques Técnicos (Foco em AI Training)

- **System Prompting Especializado:** Prompt estruturado em 4 seções obrigatórias (Diagnóstico, Performance, PEP 8, Código Revisado).
- **Classificação de Gravidade:** Problemas categorizados claramente como CRÍTICO, MÉDIO ou BAIXO.
- **Análise Big O:** Avaliação de complexidade algorítmica com sugestões práticas de otimização.
- **Segurança em Primeiro Lugar:** Detecção proativa de *hardcoded secrets*, riscos de injeção e operações inseguras.
- **Separação de Responsabilidades:** Prompts isolados em arquivo externo (`prompts/system_prompt.txt`) para fácil manutenção e teste de diferentes personas.

## 🛠️ Stack Tecnológica

- **Python 3.13**
- **Streamlit:** Interface web interativa e responsiva.
- **Groq API:** Inferência de LLM de alta velocidade (modelo `openai/gpt-oss-120b`).
- **Prompt Engineering Avançado:** Técnicas de *few-shot* e formatação estruturada.
- **python-dotenv:** Gerenciamento seguro de variáveis de ambiente e chaves de API.

---

## 🚀 Instalação e Uso Rápido

### Pré-requisitos
- Python 3.8+
- [Micromamba](https://mamba.readthedocs.io/en/latest/installation/micromamba-installation.html) instalado.
- Conta na [Groq](https://console.groq.com/) com uma API Key ativa.

### Inicialização Automatizada (Recomendado)

**1. Clone o repositório:**
```bash
git clone https://github.com/rafahalav/pai-code-reviewer.git
cd pai-code-reviewer
```

**2. Configure a API Key:**
Crie um arquivo `.env` na raiz do projeto e adicione sua chave:
```env
GROQ_API_KEY=sua_chave_gsk_aqui
```

**3. Execute o script de inicialização:**
```bash
chmod +x start.sh  # Apenas na primeira vez
./start.sh
```

> **O que o `start.sh` faz automaticamente?**
> - ✅ Inicializa o hook do shell do Micromamba.
> - ✅ Cria e ativa o ambiente virtual `paiec1` (se não existir).
> - ✅ Instala todas as dependências do `requirements.txt`.
> - ✅ Verifica a existência do arquivo `.env`.
> - ✅ Inicia o Streamlit em `http://localhost:8501`.

*(Alternativa Manual: Consulte o final deste documento para os passos manuais de instalação).*

---

## 💬 Exemplo Real de Análise

Veja como o **PAI Code Reviewer** avalia um código com problemas comuns de segurança e performance.

### Código de Entrada (Propositadamente ruim):
```python
def calc(x,y):
    return x+y

senha = "123456"
print(senha)

for i in range(100):
    for j in range(100):
        print(i*j)
```

### Análise Gerada pela IA:

#### 🔍 DIAGNÓSTICO
| Problema | Descrição | Gravidade |
| :--- | :--- | :--- |
| **Hard-coded password** | A senha "123456" está escrita no código e exibida com `print`. | **CRÍTICO** – expõe credenciais. |
| **Senha impressa** | Exibir a senha em stdout facilita a captura por logs. | **CRÍTICO** |
| **Loop O(n²) com I/O** | 10.000 iterações com `print` geram gargalo de desempenho. | **MÉDIO** |
| **Ausência de docstrings** | Reduz a legibilidade e a capacidade de ferramentas estáticas. | **MÉDIO** |
| **Nomes genéricos** | `x`, `y` e `senha` (deveria ser `password` em inglês). | **BAIXO** |

#### ⚡ PERFORMANCE (Big O)
O laço duplo tem complexidade **O(n²)**. Cada iteração executa `print()`, uma operação de I/O custosa. 
**Otimização sugerida:** Acumular resultados em uma lista ou `StringIO` e imprimir de uma vez, ou usar compreensão de lista (`list comprehension`) para reduzir a sobrecarga do interpretador.

#### 📚 PEP 8 & BOAS PRÁTICAS
| Item | Conformidade | Comentário |
| :--- | :--- | :--- |
| **Nomes de variáveis** | ❌ | PEP 8 recomenda nomes claros e em inglês (`password`). |
| **Espaçamento** | ❌ | Falta de duas linhas em branco entre definições top-level. |
| **Tipagem** | ❌ | Ausente. Deveria ser `def calc(x: int, y: int) -> int:`. |
| **Estrutura de execução** | ❌ | O código roda no import. Deve usar `if __name__ == "__main__":`. |

#### ✅ CÓDIGO REVISADO
A IA gera uma versão profissional, aplicando:
- `os.getenv()` para segurança da senha.
- Módulo `logging` no lugar de `print` para dados sensíveis.
- `Type hints` e `docstrings` completas (padrão Google/NumPy).
- List comprehension para a tabela de multiplicação, reduzindo chamadas de I/O de 10.000 para apenas `limit`.

*(O relatório completo em Markdown pode ser baixado diretamente pela interface do app através do botão "Baixar Análise").*

---

## 🎓 Casos de Uso

- **Revisão de Código:** Antes de commits em produção ou Code Reviews em equipe.
- **Aprendizado:** Estudantes entendendo boas práticas e padrões Python.
- **Avaliação de IA:** Testar e comparar a qualidade de código gerado por diferentes LLMs.
- **Auditoria de Segurança:** Identificação rápida de vulnerabilidades comuns (OWASP Top 10 para Python).

## 📊 Por que isso importa para AI Training?

Empresas como **Scale AI**, **Outlier** e **DataAnnotation** buscam profissionais que saibam:
1. **Avaliar** saídas de modelos de IA (não apenas gerá-las).
2. **Identificar** problemas sutis de qualidade, segurança e performance.
3. **Fornecer feedback** estruturado, formatado e construtivo.
4. **Seguir guidelines** complexas de formatação (como as 4 seções deste app).

O PAI Code Reviewer demonstra todas essas habilidades na prática.

## 🔗 Projetos Relacionados

- **PAI AI Coder:** Assistente de geração de código Python - [github.com/rafahalav/pai-ai-coder](https://github.com/rafahalav/pai-ai-coder)
- **CIPHER IA:** Assistente local com Qwen2 1.5B - [github.com/rafahalav/cipher-ia](https://github.com/rafahalav/cipher-ia) *(se aplicável)*

## 👨‍💻 Autor

**Rafael Halav**  
Technology Professional | Telecommunications | IT | Python | AI | Data  
🔗 [LinkedIn](https://www.linkedin.com/in/rafael-halav) | ✉️ [Contato](mailto:rafa.halav83@gmail.com)

*Desenvolvido com foco em aprendizado contínuo e aplicação prática de Inteligência Artificial.*

---
**License:** MIT  
**Status:** Active Development

---

<details>
<summary><strong>📦 Instalação Manual (Alternativa ao start.sh)</strong></summary>

Se preferir não usar o script automatizado:

```bash
# 1. Criar e ativar ambiente
micromamba create --name paiec1 python=3.13 -y
micromamba activate paiec1

# 2. Instalar dependências
pip install -r requirements.txt

# 3. Executar
streamlit run reviewer.py
```
</details>
