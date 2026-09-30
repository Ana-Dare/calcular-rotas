import sys
import subprocess

def main():
    print("Iniciando a Dashboard Interativa no Streamlit...")
    
    # Chama o módulo do Streamlit usando o executável Python do venv ativo
    subprocess.run([sys.executable, "-m", "streamlit", "run", "app.py"])

if __name__ == "__main__":
    main()