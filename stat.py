import pandas as pd
import matplotlib.pyplot as plt


zakarp = { "name":"Закарпатська", "words": ["закарпат","ужгород", "мукач", "хуст"], "population": 1253791 }
ivan = { "name":"Івано-Франківська", "words": ["івано-франків", "калус", "калуш", "коломи"], "population": 1368097 }
kyiv = { "name":"Київська+м. Київ", "words": ["київ", "києв", "борисп", "білоцерків", "білій церкві", "біла церква", "бровар"], "population": 4761828 }
ternopil = { "name":"Тернопільська", "words": ["терноп", "чортків", "кременц", "кременець", "чортков"]	, "population": 4748404 }
chernivtsi = { "name":"Чернівецька", "words": ["чернівецьк", "чернівц", "сторожин", "новодністровськ"], "population": 901632 }
dnipro = { "name":"Дніпропетровська", "words": ["дніпр", "кривому", "кривий", "криворі", "кривого", "кам'янськ"], "population": 4131808 }
zhytomyr = { "name":"Житомирська", "words": ["житомир", "бердич", "коростен", "коростн"], "population": 1208212 }
kirov = { "name":" Кіровоградська", "words": ["кропивницьк", "кіровоград", "олександрі", "світловодськ"], "population": 933109 }
cherkasy = { "name":"Черкаська", "words": ["черкас", "черкащ", "умані", "уманськ", "умань", "сміла", "смілі", "смілсь", "смільч"], "population": 1192137 }
chernihiv = { "name":"Чернігівська", "words": ["чернігів", "чернігов", "ніжин", "прилук"], "population": 991294 }
odesa = { "name":"Одеська", "words": ["одеса", "одеси", "одесі", "одеськ", "ізмаїл", "чорноморськ", "одещин"], "population": 2377230 }
kharkiv = { "name":"Харківська", "words": ["харков", "харків", "лозов", "ізюм"], "population": 2658461 }
kherson = { "name":"Херсонська", "words": ["херсон", "каховк", "каховц" ], "population": 1027913 }
sumy = { "name":"Сумська", "words": ["суми", "сумах", "сумськ", "сумчан", "конотоп", "шостк"], "population": 1068247 }
rivne = { "name":"Рівненська", "words": ["рівне", "рівному", "рівненськ", "рівнян", "вараш", "варас", "дубно", "дубне"], "population": 1203463 }
donetsk = { "name":"Донецька", "words": ["донецьк", "маріуп", "макіїв", "донечч"], "population": 4131808 }
volyn = { "name":"Волинська", "words": ["волин", "луцьк", "ковел", "лучча"], "population": 1031421 }
zapor = { "name":"Запорізька", "words": ["запорізь", "запоріжж", "мелітопол", "бердянськ"], "population": 1687401 }
khmeln = { "name":"Хмельницька", "words": ["хмельницьк", "хмельничч", "кам'янець", "шепетів"], "population": 1254702 }
krym = { "name":"Крим+м. Севастополь", "words": ["крим", "севастоп", "сімфероп", "керч", "євпатор"], "population":  2354548}
luhan = { "name":"Луганська", "words": ["луганськ", "луганщ", "алчевськ", "сєвєродонецьк"], "population": 2135913 }
lviv = { "name":"Львівська", "words": ["львів", "дрогоби", "червоноград"], "population": 2512084 }
mykol = { "name":"Миколаївська", "words": ["миколаїв", "первомайськ", "южноукраїн"], "population": 1119862 }
vinn = { "name":"Вінницька", "words": ["вінниц", "віннич", "могилів", "могилев", "жмерин"], "population": 1545416 }
polt = { "name":"Полтавська", "words": ["полтав", "кременчу", "горішн"], "population": 1386978 }


oblasts = [zakarp, ivan, kyiv, ternopil, chernivtsi, dnipro, zhytomyr, 
kirov, cherkasy, chernihiv, odesa, kharkiv, kherson, sumy, rivne, donetsk, volyn, zapor,khmeln, krym, luhan, lviv, mykol, vinn, polt]

results = {}
df = pd.DataFrame(oblasts)




with open("channel.json", 'r') as file:
	all = file.read()
	for idx, row in df.iterrows():
		words = row["words"]
		total = 0
		for word in words:
			total+=all.count(word)
		df.loc[idx, "total"] = total
		df.loc[idx, "chaos_index"] = total/row["population"]
		


df = df.set_index("name")
#df = df.sort_values(by="total")
df = df.sort_values(by="chaos_index")
print(df)

df.plot(kind='bar', xlabel="Області", ylabel="Йобнутість", use_index=True, sort_columns=True, y="chaos_index")
#df.plot(kind='bar', xlabel="Області", ylabel="Йобнутість", use_index=True, sort_columns=True, y="total")
plt.show()
