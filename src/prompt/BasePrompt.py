from src.base.prompt import Prompt

base_prompt = Prompt(
    id="base_prompt_001",
    text="""
    You are an AI assistant. You will be given a voice to text input.
    You need to generate intent from the input.
    The intent will be classified into one of the following categories:
    1. greeting
    2. question
    3. statement
    4. command
    5. affirmation
    6. negation
    
    Return a response in valid JSON string format with the best category as `intent`, your `reason` behind this choice and `confidence_score` as a metric expressing how certain you are of your choice
          (this must be between 0.0, not confident, to 1.0, extremely confident)?
          
          Refrain from selecting a category that is not in the above criteria.
    
    Input: [INPUT]
         """,
    retry="""Can you return this response in valid JSON string format with the best category as `label` (label has to be either "News", "Finance", "Entertainment", "Sports", "Lifestyle" or "Tech"), your `reason` behind this choice, `confidence_score` as a metric expressing how certain you are of your choice (this must be between 0.0, not confident, to 1.0, extremely confident)"""
)
