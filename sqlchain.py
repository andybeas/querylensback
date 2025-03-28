# import os
# import pandas as pd
# from fuzzywuzzy import fuzz
# from langchain_experimental.agents import create_pandas_dataframe_agent
# from langchain_community.chat_models import ChatOpenAI
# from langchain.agents.agent_types import AgentType
# from dotenv import load_dotenv

# # Load environment variables (API keys)
# load_dotenv()

# # Load the ACS data (already present) and the generated correct answers dataset
# acs_data = pd.read_csv("./llm_finetuning/acs_data.csv")
# correct_answers = pd.read_csv("./llm_finetuning/generated_correct_answers.csv")

# API_KEY = os.getenv("OPENAI_API_KEY")

# class SequentialChain:
#     """Class file for SQL and Dataframe"""

#     def __init__(self, verbose: bool=True) -> None:
#         self.agent = create_pandas_dataframe_agent(
#             ChatOpenAI(openai_api_key=API_KEY, temperature=0, model="gpt-4"),
#             acs_data,
#             verbose=verbose,
#             agent_type=AgentType.OPENAI_FUNCTIONS,
#             allow_dangerous_code=True,
#         )

#     def get_agent_answer(self, query: str) -> str:
#         """Get answer from agent"""
#         return self.agent.run(query)
    
#     def validate_answer(self, ai_answer: str, query: str) -> dict:
#         """Validate the AI's response using exact match, keyword match, and fuzzy matching."""
#         # Find the correct answer based on the query
#         correct_answer_row = correct_answers[correct_answers['Question'] == query]
        
#         if not correct_answer_row.empty:
#             correct_answer = correct_answer_row.iloc[0]['Correct Answer']
            
#             # Exact Match
#             if ai_answer.strip().lower() == correct_answer.strip().lower():
#                 return {"is_valid": True, "reason": "Exact match with the correct answer."}
            
#             # Keyword Matching (Simple approach)
#             correct_answer_keywords = correct_answer.split()
#             ai_answer_keywords = ai_answer.split()
#             common_keywords = set(correct_answer_keywords).intersection(set(ai_answer_keywords))
            
#             if len(common_keywords) > 0:
#                 return {"is_valid": True, "reason": f"Keyword match found. Common terms: {', '.join(common_keywords)}"}
            
#             # Fuzzy Matching (with a threshold of 80%)
#             similarity = fuzz.ratio(ai_answer.strip().lower(), correct_answer.strip().lower())
#             if similarity > 80:
#                 return {"is_valid": True, "reason": f"Fuzzy match found with similarity score: {similarity}%"}
            
#             return {"is_valid": False, "reason": "The answer does not match the expected answer in terms of keywords, exact match, or fuzzy match."}
        
#         else:
#             return {"is_valid": False, "reason": "No correct answer found for this query."}


import os
import pandas as pd
from fuzzywuzzy import fuzz
from langchain_experimental.agents import create_pandas_dataframe_agent
from langchain_community.chat_models import ChatOpenAI
from langchain.agents.agent_types import AgentType
from dotenv import load_dotenv

# Load environment variables (API keys)
load_dotenv()

# Load the ACS data (already present) and the generated correct answers dataset
acs_data = pd.read_csv("./llm_finetuning/acs_data.csv")
correct_answers = pd.read_csv("./llm_finetuning/generated_correct_answers.csv")

API_KEY = os.getenv("OPENAI_API_KEY")

class SequentialChain:
    """Class file for SQL and Dataframe"""

    def __init__(self, verbose: bool=True) -> None:
        self.agent = create_pandas_dataframe_agent(
            ChatOpenAI(openai_api_key=API_KEY, temperature=1, model="gpt-4"),
            acs_data,
            verbose=verbose,
            agent_type=AgentType.OPENAI_FUNCTIONS,
            allow_dangerous_code=True,
        )

    def get_agent_answer(self, query: str) -> str:
        """Get answer from agent"""
        return self.agent.run(query)
    
    def validate_answer(self, ai_answer: str, query: str) -> dict:
        """Validate the AI's response using exact match and keyword match."""
        # Find the correct answer based on the query
        correct_answer_row = correct_answers[correct_answers['Question'] == query]
        
        if not correct_answer_row.empty:
            correct_answer = correct_answer_row.iloc[0]['Correct Answer']
            
            # Exact Match
            if ai_answer.strip().lower() == str(correct_answer).strip().lower():
                return {"is_valid": True, "reason": "Exact match with the correct answer."}
            
            # Keyword Matching (Simple approach)
            correct_answer_keywords = str(correct_answer).split()
            ai_answer_keywords = ai_answer.split()
            common_keywords = set(correct_answer_keywords).intersection(set(ai_answer_keywords))
            
            if len(common_keywords) > 0:
                return {"is_valid": True, "reason": f"Keyword match found. Common terms: {', '.join(common_keywords)}"}
            
            # Fuzzy Matching (Threshold 80%)
            similarity = fuzz.ratio(ai_answer.lower(), str(correct_answer).lower())
            if similarity > 80:
                return {"is_valid": True, "reason": f"Fuzzy match with a similarity score of {similarity}%"}

            return {"is_valid": False, "reason": "The answer does not match the expected answer in terms of keywords, exact match, or fuzzy match."}
        
        else:
            return {"is_valid": False, "reason": "No correct answer found for this query."}
