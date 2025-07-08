from agents import user_input_agent

if __name__ == "__main__":
    user_input = input("Describe what you're looking for:\n> ")
    state = {
        "messages": [{"role": "user", "content": user_input}]
    }

    result = user_input_agent.run(state)
    print("\nParsed user query:")
    print(result["parsed_query"])
