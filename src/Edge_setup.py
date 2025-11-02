
class Edge_setup:

    def get_edge_driver():
        from selenium import webdriver
        from selenium.webdriver import EdgeOptions
        from selenium.webdriver.edge.service import Service
        import requests

        # Verifica conexão com a internet
        try:
            requests.get("https://www.google.com", timeout=5)
        except requests.ConnectionError:
            print("Sem conexão com a internet. Verifique sua rede.")
            return

        options = EdgeOptions()
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')

        service = Service("src/edge_web/msedgedriver")

        driver = webdriver.Edge(service=service, options=options)
        # Edge_setup.testing_edge_driver(driver)
        
        return driver
    
    @staticmethod
    def testing_edge_driver(driver):
        try:
            print("Iniciando Edge WebDriver...")
            print("Testando acesso ao Google.com ...")
            driver.get("https://www.google.com")
            print("Título da página:", driver.title)
            print("Edge WebDriver configurado com sucesso!")
        except Exception as e:
            print(f"Erro ao iniciar o Edge WebDriver: {e}")
        finally:
            if driver:
                driver.quit()