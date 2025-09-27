"""
Configuration settings for the AI translator
"""

import os
from typing import Dict, List

class Config:
    """Configuration class for AI translator settings"""
    
    # OpenAI settings
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
    DEFAULT_MODEL = 'gpt-3.5-turbo'
    TEMPERATURE = 0.3
    
    # Language settings
    DEFAULT_SOURCE_LANG = os.getenv('DEFAULT_SOURCE_LANG', 'auto')
    DEFAULT_TARGET_LANG = os.getenv('DEFAULT_TARGET_LANG', 'ko')
    
    # Supported languages
    SUPPORTED_LANGUAGES: Dict[str, str] = {
        'ko': 'Korean',
        'en': 'English',
        'ja': 'Japanese',
        'zh': 'Chinese (Simplified)',
        'zh-tw': 'Chinese (Traditional)',
        'es': 'Spanish',
        'fr': 'French',
        'de': 'German',
        'ru': 'Russian',
        'it': 'Italian',
        'pt': 'Portuguese',
        'ar': 'Arabic',
        'hi': 'Hindi',
        'auto': 'Auto-detect'
    }
    
    # Programming languages for code analysis
    PROGRAMMING_LANGUAGES: List[str] = [
        'python', 'javascript', 'typescript', 'java', 'c', 'cpp', 'csharp',
        'go', 'rust', 'php', 'ruby', 'kotlin', 'swift', 'scala', 'r',
        'sql', 'html', 'css', 'bash', 'powershell', 'auto'
    ]
    
    # File extensions mapping
    FILE_EXTENSIONS: Dict[str, str] = {
        '.py': 'python',
        '.js': 'javascript',
        '.ts': 'typescript',
        '.java': 'java',
        '.c': 'c',
        '.cpp': 'cpp',
        '.cxx': 'cpp',
        '.cc': 'cpp',
        '.cs': 'csharp',
        '.go': 'go',
        '.rs': 'rust',
        '.php': 'php',
        '.rb': 'ruby',
        '.kt': 'kotlin',
        '.swift': 'swift',
        '.scala': 'scala',
        '.r': 'r',
        '.sql': 'sql',
        '.html': 'html',
        '.htm': 'html',
        '.css': 'css',
        '.sh': 'bash',
        '.bash': 'bash',
        '.ps1': 'powershell'
    }
    
    @classmethod
    def get_language_from_file(cls, filename: str) -> str:
        """Get programming language from file extension"""
        for ext, lang in cls.FILE_EXTENSIONS.items():
            if filename.lower().endswith(ext):
                return lang
        return 'auto'