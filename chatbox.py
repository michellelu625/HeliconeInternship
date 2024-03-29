#import openai to interact with the OpenAI API
import openai


api_key="f669e3dcecea4bda4abc83c3207936f3"

user_input = input



# Set up OpenAI API
openai.api_key = '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'

# 'get_weather_info' function takes a location perameter - represents the location for the weather info requested
def get_weather_info(location):
    # API request to fetch weather data for the given city
    f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}"
    # This is a placeholder to demonstrate the structure and format of the expected weather information string
    weather_info = f"The weather in {location} is sunny with a temperature of 25°C."
    # Allows the calling code to access and utilize the weather information
    return weather_info

# 'generate_response' function is responsible for generating a response based on the given prompt (the parameter)
def generate_response(prompt):
    # '.Completion' refers to the Completion class within the openai module
        # Represents a completion task - allows you to generate text completions based on provided prompts
            # Basically if there's an incomplete, it will generate a completed one
    response = openai.Completion.create(
        # Specifies the engine used for generating the completition (provided by OpenAI)
        engine='text-davinci-003',
        # Connects the user's input (stored in the prompt variable) to the create method
        # Provides the necessary information for generating the completion based on the user's prompt
        prompt=prompt,
        # Sets max # of tokens to 50 (tokens = individual units of text)
        max_tokens=50,
        # .7 is a higher temperature --> introduces more randomness and diversity in the generated output
        # Temperature = amt of randomness
        temperature=0.7,
        # Single completion rather than multiple variations/versions
        n=1,
        # No stopping condition is set (can continue until max tokens are reached)
        stop=None
    )
    # 'response.choices[0]' accesses the first choice/option in the generated completions from the 'response' object
        # 'response' object is the response received from the OpenAI API after making a completion request
    # text.strip() method makes sure the output is clean and doesn't have extra spaces
    return response.choices[0].text.strip()


# Defines function 'process_user_input'
    # Processes the user's input and generates a response/output based on the input
def process_user_input(user_input):
    # Converts the user_input to lowercase and removes leading/trailing whitespace
        # Ensures that input is processed consistently
    user_input = user_input.lower().strip()
    # Checks if the user has entered the word "exit" (if it does, it will return 'Goodbye!')
    if user_input == 'exit':
        return 'Goodbye!'
    # If the user input isn't exit:
    else:
        response = generate_response(user_input)
        return response

# Display welcome message
print("Welcome to Michelle's OpenAI Chat Box!")
# Provides instructions for user
print("Ask me anything or type 'exit' to quit.")

# Starts an infinite  loop - code will keep running until there is a break or an exit condition
while True:
    # Indicates that the user should enter their input after the symbol
    user_input = input("> ")
    # Calls the process_user_input function and passes the user_input as an argument
    response = process_user_input(user_input)
    # Outputs response onto terminal
    print(response)