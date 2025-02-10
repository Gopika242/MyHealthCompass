import random
from django.core.cache import cache
import requests
from django.conf import settings

# Static list of fitness quotes
fitness_quotes = [
    "The only bad workout is the one that didn’t happen.",
    "Fitness is not about being better than someone else, it's about being better than you used to be.",
    "Take care of your body, it’s the only place you have to live.",
    "The body achieves what the mind believes.",
    "You don’t have to be great to start, but you have to start to be great.",
    "A healthy outside starts from the inside.",
    "Exercise is a celebration of what your body can do, not a punishment for what you ate.",
    "Success starts with self-discipline.",
    "Health is not valued until sickness comes.",
    "The pain you feel today will be the strength you feel tomorrow.",
    "Sore today, strong tomorrow.",
    "Fitness is like a relationship. You can’t cheat and expect it to work.",
    "Your health is an investment, not an expense.",
    "A good laugh and a long sleep are the best cures in the doctor’s book.",
    "You don't have to be extreme, just consistent.",
    "It never gets easier, you just get stronger.",
    "The best way to predict your future is to create it.",
    "Don’t count the days, make the days count.",
    "The difference between who you are and who you want to be is what you do.",
    "Exercise to be fit, not skinny. Eat to nourish your body, and always ignore the haters.",
    "The body achieves what the mind believes. 💪",
    "Fitness is not about being better than someone else, it’s about being better than you used to be.",
    "Push yourself because no one else is going to do it for you.",
    "The pain you feel today will be the strength you feel tomorrow.",
    "Success starts with self-discipline.",
    "It is health that is real wealth and not pieces of gold and silver.",
    "Your body deserves the best.",
    "The greatest wealth is health.",
    "A healthy outside starts from the inside.",
    "The doctor of the future will no longer treat the human frame with drugs, but rather will cure and prevent disease with nutrition.",
    "If you don’t make time for your wellness, you will be forced to make time for your illness.",
    "He who has health has hope; and he who has hope has everything.",
    "Health is a state of complete harmony of the body, mind, and spirit.",
    "To keep the body in good health is a duty... otherwise we shall not be able to keep our mind strong and clear.",
    "Take care to get all the facts, and take a moment to truly listen to your body.",
    "A good conscience is a continual Christmas.",
    "Happiness is the highest form of health.",
    "Your health is an investment, not an expense.",
    "A fit, healthy body—that is the best fashion statement.",
    "The human body is the best work of art.",
    "An ounce of prevention is worth a pound of cure.",
    "The groundwork for all happiness is good health.",
    "The first wealth is health.",
    "Take care of your body. It’s the only place you have to live.",
    "If you want to live a long life, focus on health, not just on living longer.",
    "Eating well is a form of self-respect."
]

def fetch_fitness_quote():
    # Try to get the quote from cache
    quote = cache.get("daily_quote")
    
    if not quote:
        try:
            # Select a random fitness quote from the list
            quote = random.choice(fitness_quotes)
            # Cache the quote for 24 hours
            cache.set("daily_quote", quote, 86400)
        except Exception as e:
            quote = f"Error fetching quote: {str(e)}"
    
    return quote



def get_recipe(query):
    # Construct API URL with query
    api_url = f'https://api.api-ninjas.com/v1/recipe?query={query}'
    
    headers = {
        'X-Api-Key': settings.API_NINJAS_KEY
    }
    
    response = requests.get(api_url, headers=headers)
    
    # Check if the response is successful
    if response.status_code == 200:
        return response.json()  # Return the JSON response
    else:
        return None  # Return None in case of an error or failure


# import requests
# from django.core.cache import cache

# ZENQUOTES_API_URL = "https://zenquotes.io/api/quotes"

# # Define a list of keywords to filter fitness-related quotes
# FITNESS_KEYWORDS = ['fitness', 'health', 'fit', 'exercise', 'workout', 'training', 'gym', 'strength', 'muscle','healthy']

# def fetch_fitness_quote():
#     # Try to get the quote from cache
#     quote = cache.get("daily_quote")
    
#     if not quote:
#         try:
#             # Fetch random quotes from ZenQuotes API
#             response = requests.get(ZENQUOTES_API_URL)
#             if response.status_code == 200:
#                 quotes_data = response.json()

#                 # Filter for quotes that contain any of the fitness-related keywords
#                 for q in quotes_data:
#                     if any(keyword in q["q"].lower() for keyword in FITNESS_KEYWORDS):  # Check for any fitness keyword
#                         quote = q["q"]
#                         # Cache the quote for 24 hours
#                         cache.set("daily_quote", quote, 86400)
#                         break
#                 else:
#                     # Default message if no fitness-related quote is found
#                     quote = "Stay motivated! Keep pushing forward! 💪"
#             else:
#                 quote = f"Error fetching quote. Status: {response.status_code}"
#         except Exception as e:
#             quote = f"Error fetching quote: {str(e)}"
    
#     return quote







# import requests
# from django.core.cache import cache

# API_URL="https://api.api-ninjas.com/v1/quotes?category=fitness"
# API_KEY ="o3t54D+t/feLQyikOG8/dg==YGcjnU5cIIoEHtyM"

# def get_daily_quote():
#     quote=cache.get("daily_fitness_quote")
#     if not quote:
#         headers={"X-Api-Key":API_KEY}
#         response=requests.get(API_URL,headers=headers)
#         if response.status_code==200:
#             data=response.json()
#             if data:
#                 quote=f'{data[0]["quote"]}-{data[0]["author"]}'
#                 cache.set("daily_fitness_quote",quote,86400)
#             else:
#                 quote="Stay motivated!Keep pushing forward! 💪"

#         else:
#             quote = "Error fetching quote."
#     return quote                

# import requests

# # Define the ZenQuotes API URL for fitness quotes
# ZENQUOTES_API_URL = "https://zenquotes.io/api/quotes?category=fitness"

# def fetch_fitness_quote():
#     try:
#         response = requests.get(ZENQUOTES_API_URL)
#         if response.status_code == 200:
#             quotes_data = response.json()
#             if quotes_data:
#                 return quotes_data[0]["q"]  # Return the quote
#             else:
#                 return "Stay motivated! Keep pushing forward! 💪"
#         else:
#             return f"Error fetching quote. Status: {response.status_code}"
#     except Exception as e:
#         return f"Error fetching quote: {str(e)}"
