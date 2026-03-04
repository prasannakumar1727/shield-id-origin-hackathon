def calculate_trust_score(face, deepfake, live, doc):

    # Convert deepfake probability to authenticity score
    deepfake_score = 1 - deepfake

    trust_score = (
        0.4 * face +
        0.25 * deepfake_score +
        0.2 * live +
        0.15 * doc
    ) * 100

    flags = []

    if deepfake > 0.5:
        flags.append("Synthetic Face Detected")

    if live < 0.5:
        flags.append("Low Liveness Signal")

    if doc < 0.5:
        flags.append("ID Forgery Risk")

    if trust_score > 75:
        flags.append("Identity Verified")

    return round(trust_score, 2), flags
