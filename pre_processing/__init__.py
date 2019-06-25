import json

from pre_processing.processor import Processor
from pre_processing.text_pre_processor import init, dictionary, stringify

# Carregando corpus não tratado
from sentiment_analysis.sentimental import sentiment
from text_classifier.classifier import classify

with open('../data/output.json') as processo:
    data = json.load(processo)

ementas = []
acordaos = []

# respeitar
for i in data:
    ementa = []
    for j in i["elementos"]["Ementa"]:
        ementa.append(j)
    ementas.append(' '.join(ementa))

for i in data:
    for j in i["elementos"]["Acórdão"]:
        acordaos.append(j)

# ementasProcess = init(ementas)
ementasProcess = Processor(ementas)
acordaosProcess = Processor(acordaos)

ementasProcess.process().stringify()

acordaos_boos = sentiment(acordaosProcess.corpus)
classify(ementasProcess.corpus, acordaos_boos)

