import os
import streamlit as st
from groq import Groq
from dotenv import load_dotenv
from pathlib import Path

# Carrega variáveis de ambiente do arquivo .env
load_dotenv()

# --- LÓGICA DE LEITURA DO PROMPT ---
# Encontra o diretório onde este script está rodando
BASE_DIR = Path(__file__).parent.resolve()
PROMPT_FILE = BASE_DIR / "prompts" / "system_prompt.txt"

# Lê o prompt do arquivo externo
with open(PROMPT_FILE, "r", encoding="utf-8") as file:
    CUSTOM_PROMPT = file.read()

# Configuração da página
st.set_page_config(
    page_title="PAI Code Reviewer",
    page_icon="🔍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Sidebar
with st.sidebar:
    st.title("🔍 PAI Code Reviewer")
    st.markdown("Assistente de revisão de código Python com foco em boas práticas, segurança e performance.")
    
    groq_api_key = st.text_input(
        "API Key Groq",
        value=os.getenv("GROQ_API_KEY", ""),
        type="password",
        help="Obtenha em https://console.groq.com/keys"
    )
    
    st.markdown("---")
    st.info("💡 Dica: Cole seu código Python na área principal e clique em 'Analisar Código'")

# Título principal
st.title("🔍 PAI Code Reviewer")
st.markdown("### Analisador de Código Python Profissional")
st.caption("Avaliação de segurança, performance, PEP 8 e boas práticas")

# Área para colar o código
code_input = st.text_area(
    "Cole seu código Python aqui:",
    height=300,
    placeholder="# Cole seu código Python aqui para análise...\ndef exemplo():\n    pass",
    label_visibility="collapsed"
)

# Botão de análise
if st.button("🔍 Analisar Código", type="primary", use_container_width=True):
    if not code_input.strip():
        st.warning("Por favor, cole algum código Python para análise.")
        st.stop()
    
    if not groq_api_key:
        st.error("Por favor, insira sua API Key da Groq na barra lateral.")
        st.stop()
    
    # Cria cliente Groq
    client = Groq(api_key=groq_api_key)
    
    # Prepara a mensagem
    messages = [
        {"role": "system", "content": CUSTOM_PROMPT},
        {"role": "user", "content": f"Revise este código Python:\n\n```python\n{code_input}\n```"}
    ]
    
    # Exibe o código sendo analisado
    with st.spinner("🔍 Analisando código..."):
        try:
            response = client.chat.completions.create(
                messages=messages,
                model="openai/gpt-oss-120b",  # Modelo mais capaz para análise crítica
                temperature=0.3,  # Temperatura baixa para respostas mais precisas
                max_tokens=2048,
            )
            
            review = response.choices[0].message.content
            
            # Exibe a análise
            st.markdown("### 📋 Resultado da Análise")
            st.markdown("---")
            st.markdown(review)
            
            # Botão para copiar/baixar a análise
            st.download_button(
                label="📥 Baixar Análise em Markdown",
                data=review,
                file_name="code_review.md",
                mime="text/markdown"
            )
            
        except Exception as e:
            st.error(f"Erro na análise: {e}")

# Rodapé
st.markdown("---")
st.markdown("<div style='text-align: center; color: gray;'>", unsafe_allow_html=True)
st.markdown("PAI Code Reviewer - Análise profissional de código Python")
st.markdown("</div>", unsafe_allow_html=True)
