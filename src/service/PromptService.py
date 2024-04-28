from src.prompt.BasePrompt import base_prompt


class PromptService:
    @staticmethod
    def get_prompt_map():
        prompt_map = {base_prompt.id: base_prompt}
        return prompt_map

    @staticmethod
    def massage_prompt(prompt, speech):
        new_prompt = prompt.copy()
        replacements = {
            "[INPUT]": speech
        }
        for placeholder, value in replacements.items():
            new_prompt.text = new_prompt.text.replace(placeholder, value)
        return new_prompt
