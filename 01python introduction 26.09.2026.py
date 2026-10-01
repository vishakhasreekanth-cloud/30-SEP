import string


# 1. DATA LOADING & MANAGEMENT

# Initial dataset containing ticket records
tickets = [
    {
        "ticket_id": 101,
        "customer": "Alice",
        "rating": 5,
        "feedback": "Great service!! The support staff fixed my issue super quickly."
    },
    {
        "ticket_id": 102,
        "customer": "Bob",
        "rating": 2,
        "feedback": "Very slow resolution... overall BAD exp, unsatisfied with response time."
    },
    {
        "ticket_id": 103,
        "customer": "Charlie",
        "rating": 4,
        "feedback": "Good help overall, but the app crashed once during testing."
    }
]

def add_ticket(ticket_list, ticket_id, customer, rating, feedback):
    """Adds a new structured ticket entry to the dataset."""
    ticket_list.append({
        "ticket_id": ticket_id,
        "customer": customer,
        "rating": rating,
        "feedback": feedback
    })

# Adding a new entry as required by taxonomy
add_ticket(tickets, 104, "Diana", 1, "Terrible service! Plz fix slang and bugs asap.")

# 2. DATA CLEANING

# Slang/keyword replacement dictionary
SLANG_MAP = {
    "plz": "please",
    "exp": "experience",
    "asap": "as soon as possible"
}

def clean_text(text):
    """
    Performs text cleaning:
    - Lowercasing
    - Punctuation removal
    - Space normalization
    - Slang/keyword correction
    """
    # Lowercasing
    text = text.lower()
    
    # Punctuation removal
    text = text.translate(str.maketrans('', '', string.punctuation))
    
    # Space normalization & slang correction
    words = text.split()
    corrected_words = [SLANG_MAP.get(word, word) for word in words]
    
    return " ".join(corrected_words)


# Apply data cleaning across all tickets
for ticket in tickets:
    ticket["cleaned_feedback"] = clean_text(ticket["feedback"])


def calculate_summary_statistics(ticket_list):
    """Calculates basic statistical measures, longest feedback, and unique words."""
    if not ticket_list:
        return {}

    ratings = [t["rating"] for t in ticket_list]
    
    # Average rating, min, max, total count
    avg_rating = sum(ratings) / len(ratings)
    min_rating = min(ratings)
    max_rating = max(ratings)
    total_count = len(ratings)

    # Longest feedback (by character length)
    longest_ticket = max(ticket_list, key=lambda x: len(x["cleaned_feedback"]))

    # Extract unique words across all feedback
    all_words = []
    for t in ticket_list:
        all_words.extend(t["cleaned_feedback"].split())
    
    unique_words = sorted(list(set(all_words)))

    return {
        "avg_rating": round(avg_rating, 2),
        "min_rating": min_rating,
        "max_rating": max_rating,
        "total_tickets": total_count,
        "longest_feedback": longest_ticket["cleaned_feedback"],
        "longest_feedback_id": longest_ticket["ticket_id"],
        "unique_words": unique_words
    }

def get_tickets_sorted_by_rating(ticket_list, reverse=True):
    """Sorts tickets based on customer rating."""
    return sorted(ticket_list, key=lambda x: x["rating"], reverse=reverse)

def filter_tickets_by_rating(ticket_list, min_threshold=1, max_threshold=5):
    """Filters tickets within a specific rating range."""
    return [t for t in ticket_list if min_threshold <= t["rating"] <= max_threshold]


def print_structured_display(ticket_list):
    """Displays formatted table output of processed tickets."""
    print("=" * 80)
    print(f"{'ID':<6} | {'Customer':<10} | {'Rating':<8} | {'Cleaned Feedback'}")
    print("-" * 80)
    for t in ticket_list:
        print(f"{t['ticket_id']:<6} | {t['customer']:<10} | {t['rating']:<8} | {t['cleaned_feedback']}")
    print("=" * 80)

def generate_one_page_summary(stats, sorted_tickets):
    """Generates clear summary and insights report."""
    print("\n" + "#" * 80)
    print("                         EXECUTIVE SUMMARY & INSIGHTS                       ")
    print("#" * 80)
    print(f"Total Tickets Analyzed : {stats['total_tickets']}")
    print(f"Average Satisfaction   : {stats['avg_rating']} / 5.0")
    print(f"Rating Range           : Min = {stats['min_rating']}, Max = {stats['max_rating']}")
    print(f"Longest Feedback (ID {stats['longest_feedback_id']}): \"{stats['longest_feedback']}\"")
    print(f"Unique Words Extracted : {len(stats['unique_words'])} words")
    print("-" * 80)
    print("Key Unique Words Sample:")
    print(", ".join(stats['unique_words'][:15]) + "...")
    print("-" * 80)
    print("Key Findings & Insights:")
    print("1. Rating distribution shows varying satisfaction, averaging a neutral-to-positive level.")
    print("2. Common keywords in feedback highlight issues related to speed, service quality, and app stability.")
    print("#" * 80 + "\n")

# Execution Pipeline
if _name_ == "_main_":
    # Calculate stats
    stats = calculate_summary_statistics(tickets)

    # Sort tickets (High to Low)
    sorted_tickets = get_tickets_sorted_by_rating(tickets, reverse=True)

    # Output Presentation
    print("\n--- STRUCTURED TICKET OUTPUT (SORTED BY RATING) ---")
    print_structured_display(sorted_tickets)

    # Reporting & Insights
    generate_one_page_summary(stats, sorted_tickets)