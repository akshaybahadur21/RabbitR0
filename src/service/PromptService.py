from src.prompt.BasePrompt import base_prompt


class PromptService:
    @staticmethod
    def get_prompt_map():
        """
        Get the prompt map
        :return:
        """
        prompt_map = {base_prompt.id: base_prompt}
        return prompt_map

    @staticmethod
    def massage_prompt(prompt, speech):
        """
        Massage the prompt
        :param prompt:
        :param speech:
        :return:
        """
        new_prompt = prompt.copy()
        replacements = {
            "[INPUT]": speech
        }
        for placeholder, value in replacements.items():
            new_prompt.text = new_prompt.text.replace(placeholder, value)
        return new_prompt
