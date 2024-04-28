from src.base.prompt import Prompt

vision_prompt = Prompt(
    id="vision_prompt_001",
    text="""
    You are an AI assistant and you have received an image as input.
    You need to generate the image description from the input image.
    
    Return a response in valid JSON string format with `long_description` that contains the detailed description of the image, `short_description` that contains a brief description of the image, `confidence_score` as a metric expressing how certain you are of your choice (this must be between 0.0, not confident, to 1.0, extremely confident).
         """,
    retry="""Can you return this response in valid JSON string format with `long_description` that contains the detailed description of the image, `short_description` that contains a brief description of the image, `confidence_score` as a metric expressing how certain you are of your choice (this must be between 0.0, not confident, to 1.0, extremely confident)"""
)
