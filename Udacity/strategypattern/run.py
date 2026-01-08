from ImportEngine import DocxImporter
from ImportEngine import CSVImporter
from ImportEngine import Importer

#print(DocxImporter.parse('./data/cats.docx'))
#print(CSVImporter.parse('./data/cats.csv'))

print(Importer.parse('./data/cats.csv'))
print(Importer.parse('./data/cats.docx'))
print(Importer.parse('./data/cats.pdf'))