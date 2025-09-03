from .url_analyzer import URLAnalyzer

class SatyaLensBot:
    def __init__(self, config):
        self.url_analyzer = URLAnalyzer(config)

    def extract_urls(self, text):
        import re
        url_pattern = r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+"
        return re.findall(url_pattern, text)

    def make_user_friendly_response(self, analysis):
        if analysis['is_safe']:
            status = "✅ This link appears to be safe."
        elif analysis['risk_score'] >= 7.0:
            status = "🚨 Dangerous link detected! Do NOT click."
        else:
            status = "⚠️ This link looks suspicious. Proceed with caution."
        details = f"Risk score: {analysis['risk_score']}/10\nThreats: {', '.join(analysis['threats']) if analysis['threats'] else 'None'}"
        return f"{status}\n{details}"

    def process_message(self, user_id, platform, message, username=None):
        urls = self.extract_urls(message)
        if urls:
            responses = []
            for url in urls:
                analysis_result = self.url_analyzer.analyze_url(url)
                responses.append(self.make_user_friendly_response(analysis_result))
            return "\n\n".join(responses)
        else:
            # Handle non-URL messages (greetings, safety tips, etc.)
            return "Hi! Send me any suspicious link and I'll analyze it for you."
