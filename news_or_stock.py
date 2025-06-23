import requests
from dotenv import load_dotenv
import os
import json
from tabulate import tabulate
load_dotenv()
def get_business_headlines(log_func, gui_output_func=None):
    api_key = os.getenv("NEWS_API_KEY")
    module_name = "news_or_stock.py"
    endpoint_name = "NewsAPI (Top U.S. Business Headlines)"
    if not api_key:
        print("Error: NEWS_API_KEY not found in .env file.")
        log_func(module_name, endpoint_name, "FAILURE", "API key not found")
        return False
    url = f"https://newsapi.org/v2/top-headlines?country=us&category=business&pageSize=5&apiKey={api_key}"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses
        data = response.json()
        if data.get("status") == "error":
            error_code = data.get('code', 'unknown_code')
            error_message = data.get('message', 'No error message provided by NewsAPI')
            print(f"NewsAPI Error: {error_code} - {error_message}")
            log_func(module_name, endpoint_name, "FAILURE", f"NewsAPI Error: {error_code} - {error_message}")
            return False
        log_func(module_name, url, "SUCCESS")
        headers = ["#", "Title", "Source", "Published Date", "URL"]
        table_data = []
        if data.get('articles'):
            for i, article in enumerate(data['articles'][:3]):
                title = article.get('title', 'N/A')
                source_name = article.get('source', {}).get('name', 'N/A')
                url_link = article.get('url', 'N/A')
                published_at = article.get('publishedAt', 'N/A')
                published_date = published_at.split('T')[0] if 'T' in published_at else published_at
                table_data.append([i + 1, title, source_name, published_date, url_link])
        else:
                table_data.append(["No articles found", "N/A", "N/A", "N/A", "N/A"])
                print("\n--- Top U.S. Business Headlines ---")
        print(tabulate(table_data, headers=headers, tablefmt="grid"))
        print("-----------------------------")
        return True
    except requests.exceptions.RequestException as e:
        print(f"Network error fetching business headlines: {e}")
        log_func(module_name, url, "FAILURE", f"RequestException: {e}")
        return False
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON response from NewsAPI: {e}")
        log_func(module_name, url, "FAILURE", f"JSONDecodeError: {e}")
        return False
    except KeyError as e:
        print(f"Error parsing news data: Missing expected key '{e}' in JSON response")
        log_func(module_name, url, "FAILURE", f"KeyError: {e}")
        return False
    
    if __name__ == "__main__":
        # Example usage
        print("Running news_or_stock.py directly for testing purposes.")
        def dummy_log(*args, **kwargs):
            print(f"Dummy log: {args}")
        get_business_headlines(dummy_log)

