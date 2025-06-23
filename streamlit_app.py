"""
AgrovisãoTech - Aplicação Principal para Streamlit Cloud
Ponto de entrada para demonstração online
"""

# Importar e executar o app principal
import sys
import os

# Adicionar diretório mobile ao path
sys.path.append(os.path.join(os.path.dirname(__file__), 'mobile'))

# Importar e executar o app melhorado
from app_enhanced import main

if __name__ == "__main__":
    main()