def hiring_signal(careers_url):
    if isinstance(careers_url, str) and "careers" in careers_url.lower():
        return "Yes"
    return "No"

def funding_tier(amount):
    if amount >= 50000000:
        return "High"
    if amount >= 10000000:
        return "Medium"
    return "Low"
