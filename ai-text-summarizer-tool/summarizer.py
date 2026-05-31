from transformers import pipeline

class TextSummarizer:
    def __init__(self, model_name="facebook/bart-large-cnn"):
        self.summarizer = pipeline("summarization", model=model_name)

    def summarize(self, text: str, max_length: int = 130, min_length: int = 30) -> str:
        result = self.summarizer(text, max_length=max_length, min_length=min_length, do_sample=False)
        return result[0]['summary_text']