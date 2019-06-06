import asyncio
from lxml import html, etree

POST_DIV_SELECTOR = '//div[@class="post__text post__text-html js-mediator-article"]'

async def replace_text(selector):
    original_text = selector.text
    if original_text:
        words = original_text.split(' ')
        new_words = []
        for word in words:
            if not ('<' in word or '>' in word) and len(word) == 6:
                new_words.append(word + '™')
            new_words.append(word)
        selector.text = " ".join(new_words)
    if selector.getchildren():
        for child_selector in selector.getchildren():
            replace_text(child_selector)

async def handle_response(text: str) -> str:
    html_selection = html.fromstring(text)
    main_page_selections = html_selection.xpath(POST_DIV_SELECTOR)
    [await replace_text(sel) for sel in main_page_selections]


    return html.tostring(html_selection, pretty_print=True, encoding='unicode')
