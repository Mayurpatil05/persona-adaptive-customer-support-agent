def should_escalate(query):

    critical_keywords = [
        "lawyer",
        "legal action",
        "sue",
        "complaint to regulator",
        "this is unacceptable",
        "cancel everything immediately"
    ]

    for word in critical_keywords:
        if word in query.lower():
            return True

    return False