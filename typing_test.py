from samples import text_samples
from random import choice


class TypingTest:
    def __init__(self):
        self.text_samples = text_samples
        self.selected_text = None

    def get_typing_text(self):
        """Returns a random sample of text for user to type."""
        self.selected_text = choice(self.text_samples)
        return self.selected_text

    def check_test(self, user_sample: str, time: int):
        """Accepts the user's entered text, a time in seconds and returns a raw WPM score and adjusted WPM score based
        on user's errors."""
        minutes = time / 60
        # splits the sample text and the user's text into lists using single spaces
        sample_words = self.selected_text.split(" ")
        user_words = user_sample.split(" ")
        # calculates the user's raw wpm by counting the number of single-space separated words
        raw_wpm = round(len(user_words)/minutes)
        # calculates the number of correctly typed words by checking the words in the user's sample against the sample
        # text
        correct_count = 0
        for word in user_words:
            if word in sample_words:
                sample_words.remove(word)
                correct_count += 1
        adjusted_wpm = round(correct_count/minutes)
        return raw_wpm, adjusted_wpm

