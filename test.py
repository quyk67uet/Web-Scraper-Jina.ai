import requests
import google.generativeai as genai

genai.configure(api_key='GEMINI-KEY')
llm = genai.GenerativeModel('gemini-1.5-flash')

def fetch_url_data(url):
    try:
        full_url = f"https://r.jina.ai/{url}"
        response = requests.get(full_url)
        if response.status_code == 200:
            return response.text
        else:
            return f"Error fetching data from {url}: Status code {response.status_code}"
    except Exception as e:
        return f"Error fetching data from {url}: {str(e)}"

def compare_products_using_llm(product1_data, product2_data, question):
    prompt = f"Product 1 Data: {product1_data}\n\nProduct 2 Data: {product2_data}\n\nQuestion: {question}\nAnswer:"

    response = llm.generate_content(prompt)
    return response.text

if __name__ == "__main__":
    url1 = input("Enter the first product URL: ").strip()
    url2 = input("Enter the second product URL: ").strip()

    product1_data = fetch_url_data(url1)
    with open("response1.txt", "w", encoding="utf-8") as file:
        file.write(product1_data)

    product2_data = fetch_url_data(url2)
    with open("response2.txt", "w", encoding="utf-8") as file:
        file.write(product2_data)

    while True:
        question = input("\nEnter your question: ").strip()
        
        if question.lower() in ['exit', 'quit']:
            print("Thank you for using the chatbot. Goodbye!")
            break

        answer = compare_products_using_llm(product1_data, product2_data, question)

        print("\nGenerated Answer:")
        print(answer)
