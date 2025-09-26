"""
Utility functions for the AI translator
"""

import os
import sys
from typing import Optional, Dict, Any
from config import Config

def validate_language_code(lang_code: str) -> bool:
    """Validate if language code is supported"""
    return lang_code in Config.SUPPORTED_LANGUAGES

def get_language_name(lang_code: str) -> str:
    """Get full language name from code"""
    return Config.SUPPORTED_LANGUAGES.get(lang_code, lang_code)

def determine_file_language(filename: str) -> str:
    """Determine programming language from filename"""
    return Config.get_language_from_file(filename)

def format_translation_result(result: Dict[str, Any]) -> str:
    """Format translation result for display"""
    if not result.get('success'):
        return f"Translation failed: {result.get('error', 'Unknown error')}"
    
    source_name = get_language_name(result['source_lang'])
    target_name = get_language_name(result['target_lang'])
    
    formatted = f"""
=== Translation Result ===
Source Language: {source_name}
Target Language: {target_name}
Model Used: {result.get('model_used', 'Unknown')}

Original Text:
{result['original_text']}

Translation:
{result['translated_text']}
"""
    return formatted.strip()

def format_analysis_result(result: Dict[str, Any]) -> str:
    """Format code analysis result for display"""
    if not result.get('success'):
        return f"Code analysis failed: {result.get('error', 'Unknown error')}"
    
    formatted = f"""
=== Code Analysis Result ===
Language: {result.get('language', 'Auto-detected')}
Model Used: {result.get('model_used', 'Unknown')}

Analysis:
{result['analysis']}
"""
    return formatted.strip()

def read_file_safely(filename: str) -> Optional[str]:
    """Safely read file content with proper error handling"""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.", file=sys.stderr)
        return None
    except UnicodeDecodeError:
        try:
            # Try with different encoding
            with open(filename, 'r', encoding='latin-1') as f:
                return f.read()
        except Exception as e:
            print(f"Error reading file '{filename}': {e}", file=sys.stderr)
            return None
    except Exception as e:
        print(f"Error reading file '{filename}': {e}", file=sys.stderr)
        return None

def validate_api_key() -> bool:
    """Validate that OpenAI API key is configured"""
    api_key = Config.OPENAI_API_KEY
    if not api_key:
        print("Error: OpenAI API key not configured.", file=sys.stderr)
        print("Please set the OPENAI_API_KEY environment variable or create a .env file.", file=sys.stderr)
        return False
    
    if api_key.startswith('sk-') and len(api_key) > 20:
        return True
    else:
        print("Warning: API key format appears to be invalid.", file=sys.stderr)
        return True  # Still allow execution in case format changes

def print_supported_languages():
    """Print list of supported languages"""
    print("Supported Languages:")
    for code, name in Config.SUPPORTED_LANGUAGES.items():
        print(f"  {code}: {name}")

def print_supported_programming_languages():
    """Print list of supported programming languages"""
    print("Supported Programming Languages for Code Analysis:")
    for lang in sorted(Config.PROGRAMMING_LANGUAGES):
        print(f"  {lang}")