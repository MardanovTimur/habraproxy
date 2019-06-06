from lxml import html, etree

test = '''
<div class="post__body post__body_crop ">
    <div class="post__text post__text-html js-mediator-article">
        Горький опыт сериалов, которые хорошо начинаются и разочаровывающе заканчиваются, удерживал меня от написания восторженного обзора на сериал «Чернобыль» до этой недели. И сейчас, когда вышла последняя, пятая серия, к сожалению, я вынужден сказать, что это отличный сериал, это прекрасный повод узнать больше о чернобыльской катастрофе, его обязательно стоит посмотреть, если вы еще не, но, если первые три серии, на мой взгляд, поднимаются до уровня моего самого любимого фильма «Аполлон-13», то две последние, опять же, по моему мнению, оказываются заметно похуже.
        <br> Mf
        <br>
        <img src="https://habrastorage.org/webt/wj/mi/kg/wjmikgdatl-gjzmxhvaz1p7s5mm.jpeg"><br>
        <i>Кадр из сериала</i>
        <br>
        <br>
        <i>Под катом спойлеры, как бы странно это не звучало для базирующегося на реальной истории сериала.</i><br>
    </div>

    <a class="btn btn_x-large btn_outline_blue post__habracut-btn" href="https://habr.com/ru/post/454670/#habracut">Читать дальше →</a>
</div>
'''

selection = html.fromstring(test)
text = selection.xpath('//div[@class="post__text post__text-html js-mediator-article"]')
root = text[0].getparent()
text[0].text = 'asdasd'
print(dir(text[0]))
for c in text[0].getchildren():
    print(c, c.text)

#  root.replace(text[0], etree.HTML(html.tostring(text[0], pretty_print=True, encoding='unicode')))
print(html.tostring(text[0], encoding='unicode', pretty_print=True))

