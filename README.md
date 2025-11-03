# Base Scraping TecMundo

Projeto Python para coleta automatizada de notícias do site TecMundo, utilizando Selenium, ambiente virtual automático e exportação dos dados para CSV.

## Funcionalidades

- Criação e gerenciamento automático de ambiente virtual (`venv`)
- Instalação automática das dependências necessárias
- Scraping de notícias do TecMundo (exemplo: seção "Voxel" ou "Segurança")
- Paginação automática: clica no botão "Mais notícias recentes" para coletar todas as notícias disponíveis
- Exportação dos dados coletados para arquivo CSV
- Exemplo de visualização dos dados em JSON formatado

## Estrutura do Projeto

```
base_scraping/
│
├── main.py
├── README.md
├── news_output/
│   └── tecmundo_news.csv
└── src/
	 ├── Edge_setup.py
	 ├── Manager_venv.py
	 └── edge_web/
		  └── msedgedriver
```

## Como usar

1. Clone o repositório:
	```bash
	git clone <url-do-repo>
	cd base_scraping
	```

2. Execute o script principal:
	```bash
	python3 main.py
	```
	O ambiente virtual será criado automaticamente e as dependências instaladas na primeira execução.

3. O resultado será salvo em `news_output/tecmundo_news.csv`.

## Principais arquivos

- `main.py`: Script principal, responsável pelo scraping e exportação dos dados.
- `src/Manager_venv.py`: Gerencia o ambiente virtual e dependências.
- `src/Edge_setup.py`: Configura o WebDriver do Edge para uso com Selenium.
- `news_output/tecmundo_news.csv`: Arquivo gerado com as notícias coletadas.

## Dependências

- requests
- beautifulsoup4
- pandas
- selenium
- webdriver-manager
- lxml

Essas dependências são instaladas automaticamente pelo projeto.

## Observações

- É necessário ter o navegador Microsoft Edge instalado.
- Será necessário um navegador Microsoft Edge compatível com o driver (Versão 142.0.3595.53)
- Este driver do Edge (`msedgedriver`) presente na pasta `src/edge_web/` é compatível com MacOS, caso utilize outro sistema operacional, baixe o driver correspondente em: [Webdriver - Developer Microsoft](https://developer.microsoft.com/pt-br/microsoft-edge/tools/webdriver?form=MA13LH)
- O scraping pode ser adaptado para outras seções do TecMundo alterando a URL no `main.py`.

## Exemplo de saída no formato JSON

Depois da execução do script, cada notícia coletada é representada por um dicionário JSON como o exemplo abaixo:

```json
{
  "title": "Exemplo de notícia",
  "link": "https://www.tecmundo.com.br/...",
  "img": "https://img.tecmundo.com.br/..."
}
```

em seguida, todos esses dicionários são armazenados em uma lista que é convertida para CSV.
