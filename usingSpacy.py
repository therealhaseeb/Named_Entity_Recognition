import spacy


FINANCIAL_ENTITY_TYPES = [
    "MONEY",  # Currency symbols, e.g. "$"
    "PERCENT",  # Percentages, e.g. "50%"
    "QUANTITY",  # Quantities, e.g. "10 million"
    "CARDINAL",  # Numerals, e.g. "100"
]

nlp = spacy.load('en_core_web_sm')

# Sample text document
doc_text = """
NEW YORK, April 10 (Reuters) - Most Wall Street banks are likely to report lower quarterly earnings and face a dour outlook for the rest of the year, with last month's regional banking crisis and a slowing economy expected to hurt profitability.
Earnings per share for the six biggest U.S. banks are expected to be down about 10% from a year earlier, analyst estimates from Refinitiv I/B/E/S show. Banks start reporting results on April 14.
The bank is expected to report a 30% rise in EPS, buoyed by an almost 36% increase in net interest income, according the Refinitiv I/B/E/S estimates and Reuters calculations.
However, tighter financial conditions and a slowing economy mean banks face the prospect of tepid loan growth and souring credit, forcing them to add to provisions against potential losses.
"We expect a challenging earnings season for the banks," said David Chiaverini, banking analyst at Wedbush Securities, in a note.
He said bank managements will become more defensive, implementing liquidity measures that could lead to downward revisions for net interest income.
Profits are also likely to be hit by another dry spell for deals and capital markets activity, and some analysts are predicting a slowdown in trading revenue as well. These trends would especially hit investment banking powerhouses like Goldman Sachs Group Inc (GS.N) and Morgan Stanley (MS.N).
Trading income, a silver lining in the previous quarters, could suffer from lower equities trading in the first quarter versus a year earlier, partially offset by strength in fixed-income, currencies and commodities (FICC), analysts said.
Goldman's earnings per share could fall by a fifth, hurt by investment banking woes, after a bigger-than-expected 69% drop in fourth-quarter profit, hurt by wealth management revenue and consumer business losses.
"""

# Process the document with spaCy
doc = nlp(doc_text)

# Extract financial entities with context
financial_entities = []
for ent in doc.ents:
    if ent.label_ in FINANCIAL_ENTITY_TYPES:
        sentence = ent.sent.text.strip()
        entity = ent.text.strip()
        type =ent.label_
        financial_entities.append((entity, type, sentence))

# Print the extracted entities with context
for entity, type, sentence in financial_entities:
    print(f"Entity: {entity} ({type}), Context: {sentence}")

