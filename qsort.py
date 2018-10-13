def qsort_concept(concepts):
    if not concepts:
        return []
    else:
        pivot = concepts[0]['value']
        less = [concept for concept in concepts if concept['value'] < pivot]
        more = [concept for concept in concepts[1:] if concept['value'] >= pivot]
        sorted_concepts = qsort_concept(less) + [pivot] + qsort_concept(more)
        return sorted_concepts