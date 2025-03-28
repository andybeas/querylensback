# # # # """
# # # # FastAPI main file
# # # # """

# # # # import os
# # # # import uvicorn
# # # # from fastapi import FastAPI
# # # # from pydantic import BaseModel
# # # # from fastapi.middleware.cors import CORSMiddleware


# # # # app = FastAPI(
# # # #     title="Assistant",
# # # #     description="A simple assistant to help you with your daily tasks",
# # # #     version="0.0.1",
# # # # )

# # # # origins = [
# # # #     "http://localhost:3000",
# # # #     "localhost:3000",
# # # #     "http://localhost:8000",
# # # #     "localhost:8000",
# # # #     "http://localhost:8080",
# # # #     "localhost:8080",
# # # #     "http://localhost:5173",
# # # #     "localhost:5173",
# # # #     "*"
# # # # ]

# # # # app.add_middleware(
# # # #     CORSMiddleware,
# # # #     allow_origins=origins,
# # # #     allow_credentials=True,
# # # #     allow_methods=["*"],
# # # #     allow_headers=["*"],

# # # # )

# # # # from sqlchain import SequentialChain
# # # # assistant = SequentialChain()

# # # # class Item(BaseModel):
# # # #     query : str


# # # # @app.get("/")
# # # # def read_root():
# # # #     return {"Hello": "Welcome to Assistant"}



# # # # @app.get("/get_dataset_lov")
# # # # def get_dataset_lov():
# # # #     return {"names": ["accs", "aps"]}


# # # # @app.post("/get_answer")
# # # # def get_answer(item: Item):
# # # #     return {"answer": assistant.get_agent_answer(item.query)}



# # # # # uvicorn main:app --reload --port 8000 


# # # """
# # # FastAPI main file
# # # """

# # # import os
# # # import uvicorn
# # # from fastapi import FastAPI
# # # from pydantic import BaseModel
# # # from fastapi.middleware.cors import CORSMiddleware
# # # from sqlchain import SequentialChain

# # # app = FastAPI(
# # #     title="Assistant",
# # #     description="A simple assistant to help you with your daily tasks",
# # #     version="0.0.1",
# # # )

# # # origins = [
# # #     "http://localhost:3000",
# # #     "localhost:3000",
# # #     "http://localhost:8000",
# # #     "localhost:8000",
# # #     "http://localhost:8080",
# # #     "localhost:8080",
# # #     "http://localhost:5173",
# # #     "localhost:5173",
# # #     "*"
# # # ]

# # # app.add_middleware(
# # #     CORSMiddleware,
# # #     allow_origins=origins,
# # #     allow_credentials=True,
# # #     allow_methods=["*"],
# # #     allow_headers=["*"],
# # # )

# # # # Initialize the SequentialChain class from sqlchain.py
# # # assistant = SequentialChain()

# # # class Item(BaseModel):
# # #     query: str

# # # @app.get("/")
# # # def read_root():
# # #     return {"Hello": "Welcome to Assistant"}

# # # @app.get("/get_dataset_lov")
# # # def get_dataset_lov():
# # #     return {"names": ["accs", "aps"]}

# # # @app.post("/get_answer")
# # # def get_answer(item: Item):
# # #     # Get the AI's response using the SequentialChain instance
# # #     ai_answer = assistant.get_agent_answer(item.query)
    
# # #     # Validate the AI's answer using the predefined answers dataset
# # #     is_valid = assistant.validate_answer(ai_answer, item.query)
    
# # #     # Return both the AI's answer and the validation result
# # #     return {
# # #         "ai_answer": ai_answer,
# # #         "valid_answer": is_valid
# # #     }

# # # # To run the server, use the command:
# # # # uvicorn main:app --reload --port 8000



# # """
# # FastAPI main file
# # """

# # import os
# # import uvicorn
# # from fastapi import FastAPI
# # from pydantic import BaseModel
# # from fastapi.middleware.cors import CORSMiddleware
# # from sqlchain import SequentialChain

# # app = FastAPI(
# #     title="Assistant",
# #     description="A simple assistant to help you with your daily tasks",
# #     version="0.0.1",
# # )

# # origins = [
# #     "http://localhost:3000",
# #     "localhost:3000",
# #     "http://localhost:8000",
# #     "localhost:8000",
# #     "http://localhost:8080",
# #     "localhost:8080",
# #     "http://localhost:5173",
# #     "localhost:5173",
# #     "*"
# # ]

# # app.add_middleware(
# #     CORSMiddleware,
# #     allow_origins=origins,
# #     allow_credentials=True,
# #     allow_methods=["*"],
# #     allow_headers=["*"],
# # )

# # # Initialize the SequentialChain class from sqlchain.py
# # assistant = SequentialChain()

# # class Item(BaseModel):
# #     query: str

# # @app.get("/")
# # def read_root():
# #     return {"Hello": "Welcome to Assistant"}

# # @app.get("/get_dataset_lov")
# # def get_dataset_lov():
# #     return {"names": ["accs", "aps"]}

# # @app.post("/get_answer")
# # def get_answer(item: Item):
# #     # Get the AI's response using the SequentialChain instance
# #     ai_answer = assistant.get_agent_answer(item.query)
    
# #     # Validate the answer against the predefined correct answers
# #     is_valid = assistant.validate_answer(ai_answer, item.query)

# #     return {
# #         "ai_answer": ai_answer,
# #         "valid_answer": is_valid  # This will return whether the answer is valid or invalid
# #     }

# # # To run the server, use the command:
# # # uvicorn main:app --reload --port 8000



# """
# FastAPI main file
# """

# import os
# import uvicorn
# from fastapi import FastAPI
# from pydantic import BaseModel
# from fastapi.middleware.cors import CORSMiddleware
# from sqlchain import SequentialChain

# app = FastAPI(
#     title="Assistant",
#     description="A simple assistant to help you with your daily tasks",
#     version="0.0.1",
# )

# origins = [
#     "http://localhost:3000",
#     "localhost:3000",
#     "http://localhost:8000",
#     "localhost:8000",
#     "http://localhost:8080",
#     "localhost:8080",
#     "http://localhost:5173",
#     "localhost:5173",
#     "*"
# ]

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# # Initialize the SequentialChain class from sqlchain.py
# assistant = SequentialChain()

# class Item(BaseModel):
#     query: str

# @app.get("/")
# def read_root():
#     return {"Hello": "Welcome to Assistant"}

# @app.get("/get_dataset_lov")
# def get_dataset_lov():
#     return {"names": ["accs", "aps"]}

# @app.post("/get_answer")
# def get_answer(item: Item):
#     # Get the AI's response using the SequentialChain instance
#     ai_answer = assistant.get_agent_answer(item.query)
    
#     # Validate the answer against the predefined correct answers
#     validation_result = assistant.validate_answer(ai_answer, item.query)

#     # Return the AI's answer along with the validation result and reason
#     return {
#         "answer": ai_answer,
#         "valid_answer": validation_result["is_valid"],  # true or false
#         "reason": validation_result["reason"]  # The reason for validation
#     }

# # To run the server, use the command:
# # uvicorn main:app --reload --port 8000


"""
FastAPI main file
"""

import os
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from sqlchain import SequentialChain

app = FastAPI(
    title="Assistant",
    description="A simple assistant to help you with your daily tasks",
    version="0.0.1",
)

origins = [
    "http://localhost:3000",
    "localhost:3000",
    "http://localhost:8000",
    "localhost:8000",
    "http://localhost:8080",
    "localhost:8080",
    "http://localhost:5173",
    "localhost:5173",
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize the SequentialChain class from sqlchain.py
assistant = SequentialChain()

class Item(BaseModel):
    query: str

@app.get("/")
def read_root():
    return {"Hello": "Welcome to Assistant"}

@app.get("/get_dataset_lov")
def get_dataset_lov():
    return {"names": ["accs", "aps"]}

@app.post("/get_answer")
def get_answer(item: Item):
    # Get the AI's response using the SequentialChain instance
    ai_answer = assistant.get_agent_answer(item.query)
    
    # Validate the answer against the predefined correct answers
    validation_result = assistant.validate_answer(ai_answer, item.query)

    # Return the AI's answer along with the validation result and reason
    return {
        "answer": ai_answer,
        "valid_answer": validation_result["is_valid"],  # true or false
        "reason": validation_result["reason"]  # The reason for validation
    }

# To run the server, use the command:
# uvicorn main:app --reload --port 8000
