text="""
China stand vor noch nicht allzu langer Zeit hierzulande vor allem für zwei Dinge: Menschenrechtsprobleme und enorme Wachstumschancen. Beides gibt es noch. Und dennoch verändert sich gerade etwas in den Beziehungen.
Brüssel (dpa) - Chinas Ministerpräsident Li Keqiang ist auf Tour in Europa. „Erst Berlin, nun Brüssel - die Botschaft dürfte in der EU-Hauptstadt ähnlich ausfallen wie in Deutschland. Ein Überblick:
Worum geht es beim EU-China-Gipfel?
Eines der wohl greifbarsten Ergebnisse dürfte das schriftliche Bekenntnis zur gemeinsamen Umsetzung des Pariser Klimaabkommens sein. Ansonsten stehen Diskussionen zu einer ganzen Reihe aktueller Fragen an, vom Handel über digitale Entwicklung und Menschenrechte bis hin zu Außen- und Sicherheitspolitik. Das Spitzentreffen soll vor allem auch Nähe zwischen zwei wichtigen Partnern demonstrieren“.
Wo sind sich beide Seiten einig?
Als Reaktion auf die Abschottungstendenzen der USA unter Präsident Donald Trump hatte die chinesische Führung in den vergangenen Monaten immer wieder betont, Freihandel und Globalisierung fördern zu wollen. Auch die EU ist ein Befürworter freier Warenströme. Auch den Kampf gegen die Erderwärmung sehen beide als Notwendigkeit.
Wo gibt es Spannungen?
China pocht darauf, von der EU als vollwertige Marktwirtschaft anerkannt und nicht mehr mit Strafzöllen belegt zu werden. Die EU unterstellt China, eigene Firmen mit unerlaubten Staatshilfen zu stützen und so Billigexporte mit zu ermöglichen. Derzeit bastelt die Staatengemeinschaft an neuen Abwehrinstrumenten dagegen.
EU-Unternehmen klagen derweil über schlechte Marktzugänge und unfairen Wettbewerb in China. Auch bei den Investitionsmöglichkeiten gibt es nach Ansicht der EU-Vertreter zu viele Einschränkungen in China. Laut Zahlen der EU-Handelskammer in Peking stiegen chinesische Investitionen in die EU im vergangenen Jahr um 77 Prozent auf mehr als 35 Milliarden Euro. Investitionen in die entgegengesetzte Richtung gingen derweil um 23 Prozent auf acht Milliarden Euro zurück.
Wie sehen die Wirtschaftsbeziehungen sonst aus?
China war in den vergangenen Jahrzehnten mit seinem gewaltigen Heer an günstigen Arbeitern ein gefragter Produktionsstandort für europäische Unternehmen. Die profitierten gleichzeitig vom Konsumhunger der wachsenden Mittelschicht des Landes. Nun aber ändert sich das Verhältnis. Chinas Kampfansage an Europas Industrie trägt den Titel «Made in China 2025». Der ambitionierte Regierungsplan sieht vor, in vielen Sektoren die Technologielücke zu westlichen Firmen zu schließen und selbst Weltmarktführer hervorzubringen. Einerseits bietet Chinas Aufholjagd europäischen Unternehmen Chancen, weil sie ihr Know-How anbieten können. Langfristig muss sich Europas Industrie aber auf mehr Wettbewerb einstellen.
Kommen sich die beiden Seiten näher - gerade auch, wo die USA unter Trump sich als zunehmend schwieriger Partner erweisen?
Ja. Je stärker die USA sich abschotten, desto mehr Raum entsteht - bei allen Differenzen - für Partner wie China. Deutlich wurde das bereits beim Berlin-Besuch Lis am Donnerstag, wo ähnliche Themen wie in Brüssel eine Rolle spielten. «Wir leben in Zeiten globaler Unsicherheiten», sagte Bundeskanzlerin Angela Merkel. Sie und Li bekannten sich dort zum System der internationalen Zusammenarbeit.
"""
text_list=[]
text_cut=text
length=len(text_cut)
for x in range(-1,length//1400):
    text_element=text_cut[:1400]
    text_cut=text_cut[1400:]
    text_list.append(text_element)


