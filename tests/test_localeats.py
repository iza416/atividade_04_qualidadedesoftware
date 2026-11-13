import re
from playwright.sync_api import Page, expect

URL_LOCALEATS = "https://local-eats-unisenac.vercel.app/"


def test_navegacao_e_filtro_pagina_inicial(page: Page):
   
    # 1. Acesa o sistema LocalEats
    page.goto(URL_LOCALEATS)

    #: Verifica se a página carregou e  está visível
    corpo_pagina = page.locator("body")
    expect(corpo_pagina).to_be_visible()

    # 2. clica no primeiro link ou botão disponível
    primeiro_elemento = page.locator("a, button, input").first
    primeiro_elemento.click()

    #  Verifica se a navegação manteve no LocalEats e carregou conteúdo
    expect(page).to_have_url(re.compile(r"local-eats-unisenac\.vercel\.app"))
    expect(corpo_pagina).not_to_be_empty()