#!/usr/bin/env python3
"""
MarkItDown Integration for ARP v24
===================================
Convert documents to Markdown for LLM analysis

Usage:
    python3 markitdown_pipeline.py --input document.pdf --output summary.md
    python3 markitdown_pipeline.py --youtube "https://youtube.com/watch?v=..." --output transcript.md
"""

import os
import sys
from pathlib import Path

# Activate markitdown environment
MARKITDOWN_ENV = Path(__file__).parent / "markitdown_env"
MARKITDOWN_PYTHON = MARKITDOWN_ENV / "bin" / "python3"

def ensure_markitdown():
    """Ensure MarkItDown is available"""
    if not MARKITDOWN_ENV.exists():
        print(f"Error: markitdown_env not found at {MARKITDOWN_ENV}")
        print("Run: uv venv markitdown_env && source markitdown_env/bin/activate && uv pip install 'markitdown[all]'")
        sys.exit(1)
    return str(MARKITDOWN_PYTHON)

def convert_document(input_path: str, output_path: str = None) -> str:
    """
    Convert document to Markdown.
    
    Supports: PDF, DOCX, PPTX, XLSX, Images, Audio, HTML, YouTube, etc.
    """
    python = ensure_markitdown()
    
    script = f"""
from markitdown import MarkItDown

md = MarkItDown()
result = md.convert("{input_path}")
print(result.text_content)
"""
    
    # Run in markitdown environment
    import subprocess
    result = subprocess.run(
        [str(MARKITDOWN_PYTHON), "-c", script],
        capture_output=True,
        text=True
    )
    
    if result.returncode != 0:
        print(f"Error: {result.stderr}")
        return None
    
    output = result.stdout
    
    # Save if output path specified
    if output_path:
        with open(output_path, 'w') as f:
            f.write(output)
        print(f"Saved to: {output_path}")
    
    return output

def convert_youtube(url: str, output_path: str = None) -> str:
    """Convert YouTube video to Markdown transcript"""
    return convert_document(url, output_path)

def convert_multiple(input_dir: str, output_dir: str = None) -> list:
    """
    Convert all documents in a directory.
    
    Args:
        input_dir: Directory containing documents
        output_dir: Output directory (optional)
        
    Returns:
        List of converted content
    """
    results = []
    input_path = Path(input_dir)
    
    for file in input_path.rglob('*'):
        if file.suffix.lower() in ['.pdf', '.docx', '.pptx', '.xlsx', '.html']:
            print(f"Converting: {file}")
            out = output_dir / f"{file.stem}.md" if output_dir else None
            content = convert_document(str(file), str(out) if out else None)
            results.append({'file': str(file), 'content': content})
    
    return results

def main():
    """CLI interface"""
    import argparse
    
    parser = argparse.ArgumentParser(description='MarkItDown for ARP v24')
    parser.add_argument('--input', '-i', help='Input file or URL')
    parser.add_argument('--output', '-o', help='Output markdown file')
    parser.add_argument('--youtube', '-y', help='YouTube URL')
    parser.add_argument('--batch', '-b', help='Batch convert directory')
    
    args = parser.parse_args()
    
    if args.youtube:
        print(f"Converting YouTube: {args.youtube}")
        content = convert_youtube(args.youtube, args.output)
    elif args.input:
        print(f"Converting: {args.input}")
        content = convert_document(args.input, args.output)
    elif args.batch:
        print(f"Batch converting: {args.batch}")
        results = convert_multiple(args.batch, args.output)
        print(f"Converted {len(results)} files")
    else:
        parser.print_help()

if __name__ == '__main__':
    main()