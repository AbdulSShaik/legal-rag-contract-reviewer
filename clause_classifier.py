from transformers import pipeline

labels = [
    "Confidentiality", "Governing Law", "Indemnification", "Termination", 
    "Non-Compete", "Dispute Resolution", "Liability", "Arbitration"
]

classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

def classify_clause(clause):
    result = classifier(clause, candidate_labels=labels)
    return result['labels'][0], result['scores'][0]