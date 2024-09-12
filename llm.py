import google.generativeai as genai

genai.configure(api_key='GEMINI-KEY')
llm = genai.GenerativeModel('gemini-1.5-flash')

def read_response_from_file(file_path='response.txt'):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        print(f"File {file_path} not found.")
        return None

def generate_response_from_file(query, file_path='response.txt'):
    context = read_response_from_file(file_path)
    
    if context is None:
        return "No data available to generate a response."

    prompt = f"Context: {context}\nQuestion: {query}\nAnswer:"
    
    response = llm.generate_content(prompt)
    
    return response.text

if __name__ == "__main__":
    query = input("Enter your question: ").strip()

    answer = generate_response_from_file(query)

    print("\nGenerated Answer:")
    print(answer)
