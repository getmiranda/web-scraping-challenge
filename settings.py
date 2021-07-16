
STORES = {
    'Chedraui': {
        'card': '//li[@class="js-plp-product-click product-item"]',
        'upc': '//div[@class="sku-code-pdp"]',
        'split': '\n',
        'tag': 'chedraui',
        'url': 'https://www.chedraui.com.mx/',
        'search': '//input[@id="searchBox"]'
    },
    'Superama': {
        'card': '//li[@class="upcWrapper item isotope-item"]',
        'upc': '//p[@class="upc-descripcion"]',
        'split': ' ',
        'tag': 'superama',
        'url': 'https://www.superama.com.mx/',
        'search': '//input[@id="serachTextV3"]'
    },
    'Walmart Súper': {
        'card': '//div[@data-automation-id="product-0"]',
        'upc': '//p[@class="text_text__1DYNl text_secondary__16wKP"]',
        'split': ':',
        'tag': 'walmart',
        'url': 'https://super.walmart.com.mx/',
        'search': '//input[@data-automation-id="searchBar"]',
        'not_found': '//section[@class="page-layout_contentContainer__3lTei showAside"]'
    }
}
