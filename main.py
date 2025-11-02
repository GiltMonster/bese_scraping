from src.Manager_venv import Manager_venv
from src.Edge_setup import Edge_setup


def main():
    """Função principal: gerencia o ambiente virtual, executa scraping da CNN Brasil e salva em CSV."""
    Manager_venv.check_and_install_dependencies()
    
    Edge_setup.get_edge_driver()


if __name__ == "__main__":
    main()