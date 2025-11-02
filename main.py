from src.Manager_venv import Manager_venv
from src.Edge_setup import Edge_setup
import time
import json
import os

def main():
    """Função principal: gerencia o ambiente virtual, executa scraping do TecMundo e salva em CSV."""
    Manager_venv.check_and_install_dependencies()
    
    drive = Edge_setup.get_edge_driver()
    url_tecmundo = "https://www.tecmundo.com.br/voxel"
    drive.get(url_tecmundo)
    print("Título da página:", drive.title)
    time.sleep(3)

    from selenium.webdriver.common.by import By
    from selenium.common.exceptions import NoSuchElementException, TimeoutException, ElementClickInterceptedException
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC

    news_dict_list = []
    processed_links = set()

    while True:
        try:
            section_element = drive.find_element(By.CLASS_NAME, "styles_container__Rpb9K")
            div_article_elements = section_element.find_elements(By.CLASS_NAME, "grid")

            for article in div_article_elements:
                a_elements = article.find_elements(By.TAG_NAME, "a")
                for a in a_elements:
                    link = a.get_attribute("href")
                    if link in processed_links:
                        continue
                    processed_links.add(link)
                    try:
                        title = a.find_element(By.TAG_NAME, "h3").text
                    except NoSuchElementException:
                        title = ""
                    try:
                        img = a.find_element(By.TAG_NAME, "img").get_attribute("src")
                    except NoSuchElementException:
                        img = ""

                    news_item = {
                        "title": title,
                        "link": link,
                        "img": img
                    }
                    news_dict_list.append(news_item)

            try:
                btn_next = WebDriverWait(drive, 10).until(
                    EC.presence_of_element_located((By.XPATH, "//a[@aria-label='Clique para ir para Mais notícias recentes']"))
                )
                drive.execute_script("arguments[0].scrollIntoView(true);", btn_next)
                WebDriverWait(drive, 10).until(
                    EC.element_to_be_clickable((By.XPATH, "//a[@aria-label='Clique para ir para Mais notícias recentes']"))
                )
                btn_next.click()
                # Aguarda a página recarregar e novos links aparecerem
                time.sleep(5)
                WebDriverWait(drive, 10).until(
                    EC.staleness_of(btn_next)
                )
                # Aguarda o botão aparecer novamente (se houver mais páginas)
                WebDriverWait(drive, 10).until(
                    EC.presence_of_element_located((By.XPATH, "//a[@aria-label='Clique para ir para Mais notícias recentes']"))
                )
            except (NoSuchElementException, TimeoutException, ElementClickInterceptedException):
                print("Botão 'Mais notícias recentes' não encontrado ou não clicável. Fim da coleta.")
                break

        except Exception as e:
            print(f"Erro ao buscar elementos: {e}")
            break

        if len(news_dict_list) > 20:
            break

    print("Resultados da coleta:")
    print("|" + "-" * 80 + "|")
    print(f" 🟢 Total de notícias coletadas: {len(news_dict_list)}")
    print("|" + "-" * 80 + "|")
    print(" 🆕 Exemplo de notícia coletada:")
    print(json.dumps(news_dict_list[0], indent=2, ensure_ascii=False))
    print("|" + "-" * 80 + "|")
    print(" 🏁 Salvando dados em CSV...")
    convert_JSON_to_CSV(news_dict_list)
    drive.quit()

def convert_JSON_to_CSV(news_list, filename="tecmundo_news.csv"):
    """Converte uma lista de dicionários em um arquivo CSV."""
    import pandas as pd
    os.makedirs("news_output", exist_ok=True)
    df = pd.DataFrame(news_list)
    df.to_csv(f"news_output/{filename}", index=False, encoding='utf-8-sig')
    print(f" ✅ Dados salvos em 'news_output/{filename}' com sucesso!")

    


if __name__ == "__main__":
    main()