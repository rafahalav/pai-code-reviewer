#!/bin/bash

# PAI Code Reviewer - Script de inicialização
# Desenvolvido por Rafael Halav

echo "🔍 PAI Code Reviewer - Iniciando..."
echo "====================================="

# 1. Inicializa o hook do micromamba para permitir 'activate' dentro de scripts
eval "$(micromamba shell hook --shell bash)"

# 2. Verifica se o ambiente virtual existe, se não, cria
if ! micromamba env list | grep -q "paiec1"; then
    echo "📦 Criando ambiente virtual paiec1..."
    micromamba create --name paiec1 python=3.13 -y
else
    echo "✅ Ambiente paiec1 já existe."
fi

# 3. Ativa o ambiente
echo "🔄 Ativando ambiente virtual..."
micromamba activate paiec1

# 4. Instala/atualiza dependências
echo "📥 Instalando/Atualizando dependências..."
pip install -r requirements.txt --quiet

# 5. Verifica se o arquivo .env existe
if [ ! -f ".env" ]; then
    echo "⚠️  Aviso: Arquivo .env não encontrado!"
    echo "   Crie um arquivo .env com sua API Key da Groq:"
    echo "   GROQ_API_KEY=sua_chave_aqui"
    echo ""
    echo "   Obtendo chave em: https://console.groq.com/keys"
    echo "   (O app vai iniciar, mas você poderá colar a chave na interface)"
fi

# 6. Inicia o Streamlit
echo ""
echo "🚀 Iniciando PAI Code Reviewer..."
echo "   Acesse: http://localhost:8501"
echo "   Pressione Ctrl+C para parar."
echo ""

streamlit run reviewer.py
