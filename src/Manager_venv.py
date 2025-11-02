import os
import sys
import subprocess
import venv

class Manager_venv:
    """Gerenciador de ambiente virtual e dependências"""
    
    def __init__(self, venv_name="venv"):
        self.venv_name = venv_name
        self.venv_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), venv_name)
        self.venv_python = self._get_venv_python_path()
    
    def _get_venv_python_path(self):
        """Retorna o caminho para o executável Python do ambiente virtual"""
        if sys.platform == "win32":
            return os.path.join(self.venv_dir, "Scripts", "python.exe")
        else:
            return os.path.join(self.venv_dir, "bin", "python3")
    
    def setup_dependencies(self):
        # Se o script não estiver rodando dentro do venv, cria um novo ambiente virtual e reexecuta o script
        if sys.prefix != self.venv_dir:
            if not os.path.exists(self.venv_dir):
                print("Criando ambiente virtual...")
                venv.create(self.venv_dir, with_pip=True)

            print(f"Reiniciando dentro do ambiente virtual: {self.venv_python}")
            subprocess.run([self.venv_python] + sys.argv)  # Reexecuta o script dentro do venv
            sys.exit(0)  # Encerra a execução do processo atual

        # Verifica se as dependências estão instaladas
        try:
            import requests
            import bs4
            import pandas
            import selenium
            import webdriver_manager
            import lxml

        except ImportError:
            print("Dependências necessárias não encontradas: request beautifulsoup4 pandas selenium webdriver-manager lxml")
            user_input = input("Deseja instalar as dependências agora? (s/n): ").strip().lower()

            if user_input == 's':
                print("Instalando dependências no ambiente virtual...")
                subprocess.check_call([self.venv_python, "-m", "pip", "install", "requests", "beautifulsoup4", "pandas", "selenium", "webdriver-manager", "lxml"])
                print("Dependências instaladas com sucesso! Continuando...")

                # Recarregar módulos importados após instalação
                import importlib
                importlib.invalidate_caches()

            else:
                print("Não foi possível continuar devido à falta das dependências necessárias.")
                sys.exit(1)

    @staticmethod
    def check_and_install_dependencies():
        """Função de conveniência que mantém a interface original"""

        manager = Manager_venv()
        manager.setup_dependencies()
