import autogen
# import openai

# openai.api_key = 'your open api key'

# Load the configuration list from a JSON file
config_list = autogen.config_list_from_json(
    "OAI_CONFIG_LIST",
    file_location=".",
    filter_dict={
        "model": "gpt-4"
    }
)

# Define the configuration for the LLM
llm_config = {
    "request_timeout": 600,
    "seed": 42,
    "config_list": config_list,
    "temperature": 0,
}

# Create an AssistantAgent
assistant = autogen.AssistantAgent(
    name="assistant",
    llm_config=llm_config,
    system_message="Reply TERMINATE if the task has been solved at full satisfaction."
)

# Create a UserProxyAgent
user_proxy = autogen.UserProxyAgent(
    name="user_proxy",
    human_input_mode="ALWAYS",
    max_consecutive_auto_reply=10,
    is_termination_msg=lambda x: x.get(
        "content", "").rstrip().endswith("TERMINATE"),
    code_execution_config={"work_dir": "web"},
    llm_config=llm_config,
    system_message="Reply TERMINATE if the task has been solved at full satisfaction. Otherwise, reply CONTINUE, or the reason why the task is not solved yet." # noqa
)

# Assign a task to the user_proxy
user_proxy.initiate_chat(
    assistant,
    message="""Build a classic space invader game in python""",
)
