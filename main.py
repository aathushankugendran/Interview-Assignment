# Import necessary modules
from langchain_openai import ChatOpenAI
from langchain_core.prompts.chat import ChatPromptTemplate
from langchain.output_parsers import CommaSeparatedListOutputParser
from selenium import webdriver

# Set your OpenAI API key
openai_api_key = "sk-proj-XarUuTXA8wZbNVAJiq70T3BlbkFJKQZ0wgtSrIYSgeaX8qy5"

# Initialize Chrome WebDriver
webdriver_path = "/Users/aathushankugendran/Desktop/chromedriver-mac-x64"
options = webdriver.ChromeOptions()
options.binary_location = webdriver_path
driver = webdriver.Chrome(options=options)

# Initialize the chat model (e.g., using OpenAI) with your API key
chat_model = ChatOpenAI(model="gpt-3.5-turbo-0125", openai_api_key=openai_api_key)

# Create a prompt template for the conversation
template = "You are booking tickets for the movie {movie} in {location} for {time}."
human_template = "I want to book tickets for the movie 'Dune' in Toronto for tonight at 10 PM."

chat_prompt = ChatPromptTemplate.from_messages([
    ("system", template),
    ("human", human_template),
])

# Initialize the output parser (if needed)
output_parser = CommaSeparatedListOutputParser()

# Chain together the prompt, chat model, and output parser (if needed)
chain = chat_prompt | chat_model | output_parser

# Invoke the chain to generate a response
response = chain.invoke({"movie": "Dune: Part Two", "location": "Markham", "time": "tonight at 10 PM"})

# Use Selenium to perform actions based on the generated response
driver.get("https://www.cineplex.com/")
search_bar = driver.find_element_by_id("searchBarInput")
search_bar.send_keys(response)
search_button = driver.find_element_by_id("searchBarSubmit")
search_button.click()
# Close the WebDriver
driver.quit()
