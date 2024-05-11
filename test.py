from lxml import etree
from db.add_creator import add_creator

html_content = ""
with open("tmp.html", "r") as f:
    html_content = f.read()

root = etree.HTML(html_content)
i = 1

infos = []

while True:
    path = "/html/body/div[2]/div/div[2]/main/div/div/div/div/div[5]/div/div/div/div/div[2]/div/div/div/div/div/div[2]/table/tr[%d]" %(i*2)
    creator = root.xpath(path)
    if not creator:
        break
    creator_name = creator[0].xpath("td[1]/div/span/div/div[2]/div[1]/div/span")[0].text
    category = ""
    for element in creator[0].xpath("td[1]/div/span/div/div[2]/div[2]/div/span"):
        if len(category) > 0:
            category += "|"
        category += element.xpath("div/span/div/div/div")[0].text

    fans = creator[0].xpath("td[2]/div/span/div")[0].text
    if "K" in fans:
        fans = fans.replace("K","")
        fans = float(fans) * 1000
        fans = int(fans)
    views = creator[0].xpath("td[3]/div/span/div")[0].text
    if "K" in views:
        views = views.replace("K", "")
        views = float(views) * 1000
        views = int(views)

    gmp = creator[0].xpath("td[4]/div/span/div/span/div[1]/div/span")[0].text + " " + creator[0].xpath("td[4]/div/span/div/span/div[2]/div/span")[0].text
    print(creator_name, category, fans, views, gmp)
    infos.append((creator_name, category, fans, views, gmp))
    i = i+1

add_creator(infos)
