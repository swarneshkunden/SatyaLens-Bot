import requests
from urllib.parse import urlparse, parse_qs

class URLAnalyzer:
    def __init__(self, config):
        self.config = config
        # Initialize API keys or other settings from config here if needed

    def analyze_url(self, url):
        # Parse the URL components
        parsed = urlparse(url)
        protocol = parsed.scheme.upper()
        domain = parsed.netloc
        path = parsed.path
        query_params = parse_qs(parsed.query)

        # Try sending a GET request to check HTTP status and get content
        try:
            response = requests.get(url, timeout=5)
            status_code = response.status_code
            html_content = response.text

            # Extract title and meta description (basic extraction)
            title = self._extract_tag_content(html_content, '<title>', '</title>')
            meta_desc = self._extract_tag_content(html_content, 'name="description" content="', '"')

        except requests.RequestException:
            status_code = None
            title = None
            meta_desc = None

        # Determine threats and risk (simple heuristics)
        threats = []
        risk_score = 3.0
        is_safe = True

        # Example heuristic: suspicious if domain ends with .ru or contains 'bit.ly'
        if domain.endswith('.ru') or 'bit.ly' in url:
            threats.append("Suspicious domain or URL shortener detected")
            risk_score = 8.0
            is_safe = False

        if status_code and status_code >= 400:
            threats.append(f"HTTP error status: {status_code}")
            risk_score = max(risk_score, 6.0)
            is_safe = False

        # Prepare and return analysis results
        return {
            "is_safe": is_safe,
            "risk_score": risk_score,
            "threats": threats,
            "protocol": protocol,
            "domain": domain,
            "path": path,
            "query_params": query_params,
            "http_status": status_code,
            "page_title": title,
            "meta_description": meta_desc
        }

    def _extract_tag_content(self, html, start_tag, end_tag):
        start_index = html.find(start_tag)
        if start_index == -1:
            return None
        start_index += len(start_tag)
        end_index = html.find(end_tag, start_index)
        if end_index == -1:
            return None
        return html[start_index:end_index].strip()
