import random

# ------------------ WEATHER TOOL ------------------
def mock_weather_api(location: str) -> str:
    try:
        conditions = ["Sunny", "Rainy", "Cloudy", "Windy", "Stormy"]
        temp = random.randint(20, 38)
        cond = random.choice(conditions)
        return f"Weather in {location.title()}: {cond}, {temp}°C"
    except:
        return "Weather API error."

# ------------------ DICTIONARY TOOL ------------------
mock_dictionary = {
    "computer": "An electronic device used for computation.",
    "network": "A group of connected devices that communicate.",
    "protocol": "A set of rules governing data communication.",
    "ai": "Artificial Intelligence, machine-simulated intelligence."
}

def dictionary_lookup(word: str) -> str:
    try:
        return mock_dictionary.get(word.lower(), "Word not found in dictionary.")
    except:
        return "Dictionary lookup error."

# ------------------ CURRENCY CONVERTER TOOL ------------------
def currency_converter(query: str) -> str:
    try:
        parts = query.lower().split()
        if len(parts) != 4 or parts[2] != "to":
            return "Format: '100 USD to INR'"

        amount = float(parts[0])
        from_curr = parts[1]
        to_curr = parts[3]

        rates = {
            ("usd", "inr"): 83,
            ("inr", "usd"): 1 / 83
        }

        key = (from_curr, to_curr)
        if key not in rates:
            return "Conversion not supported."

        converted = amount * rates[key]
        return f"{amount} {from_curr.upper()} = {converted:.2f} {to_curr.upper()}"
    except:
        return "Currency converter error."
