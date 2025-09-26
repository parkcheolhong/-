#!/usr/bin/env python3
"""
통역 프로그램 with GPT AI 기능
Translation Program with GPT AI Functionality

This program provides:
1. Text translation using OpenAI GPT models
2. Code analysis and review functionality
3. Multi-language support
"""

import os
import sys
import argparse
from typing import Optional, Dict, Any
from dotenv import load_dotenv
import openai
from config import Config
from utils import (
    validate_language_code, get_language_name, determine_file_language,
    format_translation_result, format_analysis_result, read_file_safely,
    validate_api_key, print_supported_languages, print_supported_programming_languages
)

class AITranslator:
    """AI-powered translator using OpenAI GPT models"""
    
    def __init__(self, api_key: Optional[str] = None):
        """Initialize the translator with OpenAI API key"""
        load_dotenv()
        
        self.api_key = api_key or Config.OPENAI_API_KEY
        if not self.api_key:
            raise ValueError("OpenAI API key is required. Set OPENAI_API_KEY environment variable or pass it directly.")
        
        self.client = openai.OpenAI(api_key=self.api_key)
        self.languages = Config.SUPPORTED_LANGUAGES
    
    def translate_text(self, text: str, target_lang: str = 'ko', source_lang: str = 'auto') -> Dict[str, Any]:
        """
        Translate text using GPT AI
        
        Args:
            text: Text to translate
            target_lang: Target language code
            source_lang: Source language code (auto for auto-detection)
            
        Returns:
            Dictionary with translation result and metadata
        """
        try:
            target_language = self.languages.get(target_lang, target_lang)
            
            if source_lang == 'auto':
                prompt = f"""
                Please translate the following text to {target_language}.
                If the text is already in {target_language}, please indicate that no translation is needed.
                
                Text to translate:
                "{text}"
                
                Please provide:
                1. The detected source language
                2. The translation (or indicate if no translation needed)
                3. Any cultural or contextual notes if relevant
                """
            else:
                source_language = self.languages.get(source_lang, source_lang)
                prompt = f"""
                Please translate the following text from {source_language} to {target_language}.
                
                Text to translate:
                "{text}"
                
                Please provide:
                1. The translation
                2. Any cultural or contextual notes if relevant
                """
            
            response = self.client.chat.completions.create(
                model=Config.DEFAULT_MODEL,
                messages=[
                    {"role": "system", "content": "You are a professional translator with expertise in multiple languages and cultural contexts."},
                    {"role": "user", "content": prompt}
                ],
                temperature=Config.TEMPERATURE
            )
            
            translation = response.choices[0].message.content
            
            return {
                'success': True,
                'original_text': text,
                'translated_text': translation,
                'source_lang': source_lang,
                'target_lang': target_lang,
                'model_used': Config.DEFAULT_MODEL
            }
            
        except Exception as e:
            return {
                'success': False,
                'error': str(e),
                'original_text': text
            }
    
    def analyze_code(self, code: str, language: str = 'auto') -> Dict[str, Any]:
        """
        Analyze code and provide review feedback
        
        Args:
            code: Source code to analyze
            language: Programming language (auto for auto-detection)
            
        Returns:
            Dictionary with code analysis results
        """
        try:
            prompt = f"""
            Please analyze the following code and provide a comprehensive review:
            
            Code to analyze:
            ```
            {code}
            ```
            
            Please provide:
            1. Detected programming language (if auto-detection requested)
            2. Code quality assessment
            3. Potential issues or bugs
            4. Suggestions for improvement
            5. Best practices recommendations
            6. Security considerations (if applicable)
            7. Performance considerations
            
            Please format your response in a clear, structured manner.
            """
            
            response = self.client.chat.completions.create(
                model=Config.DEFAULT_MODEL,
                messages=[
                    {"role": "system", "content": "You are an expert code reviewer with deep knowledge of multiple programming languages, best practices, and security considerations."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.2
            )
            
            analysis = response.choices[0].message.content
            
            return {
                'success': True,
                'original_code': code,
                'analysis': analysis,
                'language': language,
                'model_used': Config.DEFAULT_MODEL
            }
            
        except Exception as e:
            return {
                'success': False,
                'error': str(e),
                'original_code': code
            }

def main():
    """Main function to handle command line interface"""
    parser = argparse.ArgumentParser(
        description='AI-powered translator and code analyzer',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Translate text to Korean
  python translator.py translate "Hello world" --target ko
  
  # Translate with specific source language
  python translator.py translate "안녕하세요" --source ko --target en
  
  # Analyze code from file
  python translator.py analyze --file example.py
  
  # Analyze code from stdin
  echo "def hello(): print('world')" | python translator.py analyze
  
  # List supported languages
  python translator.py languages
  
  # List supported programming languages
  python translator.py prog-languages
        """
    )
    
    subparsers = parser.add_subparsers(dest='command', help='Available commands')
    
    # Translation command
    translate_parser = subparsers.add_parser('translate', help='Translate text')
    translate_parser.add_argument('text', help='Text to translate')
    translate_parser.add_argument('--source', '-s', default=Config.DEFAULT_SOURCE_LANG, help=f'Source language code (default: {Config.DEFAULT_SOURCE_LANG})')
    translate_parser.add_argument('--target', '-t', default=Config.DEFAULT_TARGET_LANG, help=f'Target language code (default: {Config.DEFAULT_TARGET_LANG})')
    
    # Code analysis command
    analyze_parser = subparsers.add_parser('analyze', help='Analyze code')
    analyze_parser.add_argument('--file', '-f', help='Code file to analyze')
    analyze_parser.add_argument('--language', '-l', default='auto', help='Programming language (default: auto)')
    
    # Languages command
    subparsers.add_parser('languages', help='List supported languages')
    
    # Programming languages command  
    subparsers.add_parser('prog-languages', help='List supported programming languages')
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        return
    
    # Handle non-API commands first
    if args.command == 'languages':
        print_supported_languages()
        return
    
    if args.command == 'prog-languages':
        print_supported_programming_languages()
        return
    
    # Validate API key for commands that need it
    if not validate_api_key():
        sys.exit(1)
    
    try:
        translator = AITranslator()
        
        if args.command == 'translate':
            # Validate language codes
            if not validate_language_code(args.source) and args.source != 'auto':
                print(f"Error: Unsupported source language '{args.source}'", file=sys.stderr)
                print("Use 'python translator.py languages' to see supported languages", file=sys.stderr)
                sys.exit(1)
            
            if not validate_language_code(args.target):
                print(f"Error: Unsupported target language '{args.target}'", file=sys.stderr)
                print("Use 'python translator.py languages' to see supported languages", file=sys.stderr)
                sys.exit(1)
            
            result = translator.translate_text(args.text, args.target, args.source)
            print(format_translation_result(result))
            
            if not result['success']:
                sys.exit(1)
        
        elif args.command == 'analyze':
            if args.file:
                code = read_file_safely(args.file)
                if code is None:
                    sys.exit(1)
                
                # Auto-detect language from file extension if not specified
                if args.language == 'auto':
                    args.language = determine_file_language(args.file)
            else:
                # Read from stdin
                try:
                    code = sys.stdin.read()
                except KeyboardInterrupt:
                    print("\nOperation cancelled by user", file=sys.stderr)
                    sys.exit(1)
            
            if not code.strip():
                print("No code provided for analysis", file=sys.stderr)
                sys.exit(1)
            
            result = translator.analyze_code(code, args.language)
            print(format_analysis_result(result))
            
            if not result['success']:
                sys.exit(1)
    
    except ValueError as e:
        print(f"Configuration error: {e}", file=sys.stderr)
        sys.exit(1)
    except KeyboardInterrupt:
        print("\nOperation cancelled by user", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
    main()