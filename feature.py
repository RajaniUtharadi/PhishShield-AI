import re

def extract_features(url):

    features = []

    # URL length
    features.append(len(url))

    # Count dots
    features.append(url.count('.'))

    # Count hyphens
    features.append(url.count('-'))

    # @ symbol
    features.append(url.count('@'))

    # HTTPS check
    features.append(1 if "https" in url else 0)

    # IP address detection
    features.append(
        1 if re.search(r'\d+\.\d+\.\d+\.\d+', url) else 0
    )

    # Suspicious keywords
    suspicious_keywords = [
        'login',
        'verify',
        'secure',
        'account',
        'bank',
        'update',
        'free',
        'bonus'
    ]

    keyword_score = sum(
        word in url.lower()
        for word in suspicious_keywords
    )

    features.append(keyword_score)

    return features