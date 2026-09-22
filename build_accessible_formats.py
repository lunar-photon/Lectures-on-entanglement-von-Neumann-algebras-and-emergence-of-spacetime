#!/usr/bin/env python3
"""
Build script to generate accessible HTML and Markdown editions of the
Hong Liu 'Lectures on Entanglement, von Neumann Algebras, and Emergence of Spacetime' Reading Companion.
"""

import os
import re
import html
import json

CHAPTERS = [
    ("01_introduction.tex", "Sec. I: Introduction and Motivations"),
    ("02_von_neumann_algebras.tex", "Sec. II: Introduction to von Neumann Algebras"),
    ("03_type_I_and_II.tex", "Sec. III: Type I and II Algebras & Entanglement"),
    ("04_type_III_modular_theory.tex", "Sec. IV: Type III Algebras & Modular Theory"),
    ("05_crossed_product.tex", "Sec. V: Crossed Product by Modular Group"),
    ("06_adscft_large_N.tex", "Sec. VI: AdS/CFT Duality in Large-N Limit"),
    ("07_subregion_subalgebra_duality.tex", "Sec. VII: Subregion-Subalgebra Duality"),
    ("08_emergence_of_spacetime.tex", "Sec. VIII: Emergence of Spacetime"),
    ("09_quantum_gravity_regimes.tex", "Sec. IX: Quantum Gravity Regimes & Toy Models"),
    ("10_conclusions.tex", "Sec. X: Conclusions & Discussions")
]

def clean_tex_to_text(tex):
    """Strip LaTeX commands for plain text / search indexing."""
    t = tex
    t = re.sub(r'\\texorpdfstring\{([^}]*)\}\{([^}]*)\}', r'\2', t)
    t = re.sub(r'\\(textbf|textit|emph|text|mathrm)\{([^}]*)\}', r'\2', t)
    t = re.sub(r'\\(section|subsection|subsubsection)\*?\{([^}]*)\}', r'\2', t)
    t = re.sub(r'\$([^$]*)\$', r'\1', t)
    t = re.sub(r'\\[a-zA-Z]+', ' ', t)
    t = re.sub(r'[{}]', ' ', t)
    t = re.sub(r'\s+', ' ', t).strip()
    return t

def tex_to_html(tex_content):
    """Convert LaTeX chapter content to clean semantic HTML."""
    # Expand custom texorpdfstring
    content = re.sub(r'\\texorpdfstring\{([^}]*)\}\{([^}]*)\}', r'\1', tex_content)
    
    # Handle comments
    lines = content.split('\n')
    cleaned_lines = []
    for line in lines:
        if line.strip().startswith('%') and not line.strip().startswith('% ='):
            continue
        # Remove trailing unescaped comments
        line_no_comment = re.sub(r'(?<!\\)%.*$', '', line)
        cleaned_lines.append(line_no_comment)
    content = '\n'.join(cleaned_lines)

    # Process custom boxes: physconnect
    def replace_physconnect(match):
        opt = match.group(1) or ""
        title = "Physics Connection"
        if opt:
            opt_clean = opt.strip('[]: ')
            title += f": {opt_clean}"
        body = match.group(2)
        return f'\n<div class="callout callout-physics" role="region" aria-label="{html.escape(clean_tex_to_text(title))}"><div class="callout-header"><span class="callout-icon">⚛</span> <span class="callout-title">{title}</span></div><div class="callout-body">\n{body}\n</div></div>\n'

    content = re.sub(r'\\begin\{physconnect\}(\[[^\]]*\])?(.*?)\\end\{physconnect\}', replace_physconnect, content, flags=re.DOTALL)

    # Process yourquestion
    def replace_question(match):
        q_text = match.group(1)
        return f'\n<div class="callout callout-question" role="region" aria-label="Margin Question"><div class="callout-header"><span class="callout-icon">💡</span> <span class="callout-title">Margin Question</span></div><div class="callout-body"><em>{q_text}</em></div></div>\n'

    content = re.sub(r'\\yourquestion\{([^{}]*(?:\{[^{}]*\}[^{}]*)*)\}', replace_question, content)

    # Process worked examples in quotes
    def replace_worked_example(match):
        body = match.group(1)
        return f'\n<div class="callout callout-example" role="region" aria-label="Worked Example"><div class="callout-header"><span class="callout-icon">📝</span> <span class="callout-title">Worked Example</span></div><div class="callout-body">\n{body}\n</div></div>\n'

    content = re.sub(r'\\begin\{quote\}\s*\\textit\{Worked example[^}]*\}\.?\s*(.*?)\\end\{quote\}', replace_worked_example, content, flags=re.DOTALL)
    content = re.sub(r'\\begin\{quote\}(.*?)\\end\{quote\}', r'<blockquote>\1</blockquote>', content, flags=re.DOTALL)

    # Process headings
    content = re.sub(r'\\section\{([^}]*)\}', r'<h2 class="section-title">\1</h2>', content)
    content = re.sub(r'\\subsection\{([^}]*)\}', r'<h3 class="subsection-title">\1</h3>', content)
    content = re.sub(r'\\subsubsection\*?\{([^}]*)\}', r'<h4 class="subsubsection-title">\1</h4>', content)

    # Process lists
    def replace_enum(match):
        items = re.findall(r'\\item\s*(.*?)(?=\\item|\Z)', match.group(1), flags=re.DOTALL)
        lis = ''.join([f'<li>{it.strip()}</li>' for it in items])
        return f'<ol class="styled-list">{lis}</ol>'

    def replace_item(match):
        items = re.findall(r'\\item\s*(.*?)(?=\\item|\Z)', match.group(1), flags=re.DOTALL)
        lis = ''.join([f'<li>{it.strip()}</li>' for it in items])
        return f'<ul class="styled-list">{lis}</ul>'

    content = re.sub(r'\\begin\{enumerate\}(.*?)\\end\{enumerate\}', replace_enum, content, flags=re.DOTALL)
    content = re.sub(r'\\begin\{itemize\}(.*?)\\end\{itemize\}', replace_item, content, flags=re.DOTALL)

    # Process basic tables
    def replace_tabular(match):
        table_body = match.group(1)
        # remove \toprule, \midrule, \bottomrule
        table_body = re.sub(r'\\(toprule|midrule|bottomrule)', '', table_body)
        rows = [r.strip() for r in table_body.strip().split(r'\\') if r.strip()]
        html_rows = []
        for i, row in enumerate(rows):
            cols = [c.strip() for c in row.split('&')]
            if i == 0:
                html_rows.append('<tr>' + ''.join([f'<th>{c}</th>' for c in cols]) + '</tr>')
            else:
                html_rows.append('<tr>' + ''.join([f'<td>{c}</td>' for c in cols]) + '</tr>')
        return f'<div class="table-container"><table class="styled-table">{"".join(html_rows)}</table></div>'

    content = re.sub(r'\\begin\{tabular\}\{[^}]*\}(.*?)\\end\{tabular\}', replace_tabular, content, flags=re.DOTALL)
    content = re.sub(r'\\begin\{center\}|\\end\{center\}', '', content)

    # Process math blocks: \[ ... \] -> $$ ... $$
    content = re.sub(r'\\\[(.*?)\\\]', r'<div class="math-block">$$\1$$</div>', content, flags=re.DOTALL)

    # Process inline formatting
    content = re.sub(r'\\textbf\{([^}]*)\}', r'<strong>\1</strong>', content)
    content = re.sub(r'\\(emph|textit)\{([^}]*)\}', r'<em>\1</em>', content)
    content = re.sub(r'\\cite\{([^}]*)\}', r'<cite>[\1]</cite>', content)

    # Replace double quotes `` ''
    content = re.sub(r"``(.*?)''", r'“\1”', content)
    content = re.sub(r'--(-)?', r'—', content)

    # Clean empty paragraphs and format text paragraphs
    blocks = re.split(r'\n\s*\n', content)
    html_blocks = []
    for b in blocks:
        b_clean = b.strip()
        if not b_clean:
            continue
        if b_clean.startswith('<h') or b_clean.startswith('<div') or b_clean.startswith('<ol') or b_clean.startswith('<ul') or b_clean.startswith('<blockquote') or b_clean.startswith('<table'):
            html_blocks.append(b_clean)
        else:
            html_blocks.append(f'<p>{b_clean}</p>')

    return '\n\n'.join(html_blocks)

def tex_to_markdown(tex_content):
    """Convert LaTeX chapter content to clean Markdown."""
    content = re.sub(r'\\texorpdfstring\{([^}]*)\}\{([^}]*)\}', r'\1', tex_content)
    
    # Process custom boxes
    def replace_physconnect_md(match):
        opt = match.group(1) or ""
        title = "Physics Connection"
        if opt:
            opt_clean = opt.strip('[]: ')
            title += f": {opt_clean}"
        body = match.group(2).strip()
        lines = body.split('\n')
        quoted = '\n'.join([f"> {l}" for l in lines])
        return f"\n> [!NOTE] **{title}**\n{quoted}\n"

    content = re.sub(r'\\begin\{physconnect\}(\[[^\]]*\])?(.*?)\\end\{physconnect\}', replace_physconnect_md, content, flags=re.DOTALL)

    def replace_question_md(match):
        q_text = match.group(1).strip()
        return f"\n> [!TIP] **Margin Question:**\n> *{q_text}*\n"

    content = re.sub(r'\\yourquestion\{([^{}]*(?:\{[^{}]*\}[^{}]*)*)\}', replace_question_md, content)

    def replace_quote_md(match):
        body = match.group(1).strip()
        lines = body.split('\n')
        quoted = '\n'.join([f"> {l}" for l in lines])
        return f"\n> [!EXAMPLE] **Worked Example:**\n{quoted}\n"

    content = re.sub(r'\\begin\{quote\}\s*\\textit\{Worked example[^}]*\}\.?\s*(.*?)\\end\{quote\}', replace_quote_md, content, flags=re.DOTALL)

    # Headings
    content = re.sub(r'\\section\{([^}]*)\}', r'# \1', content)
    content = re.sub(r'\\subsection\{([^}]*)\}', r'## \1', content)
    content = re.sub(r'\\subsubsection\*?\{([^}]*)\}', r'### \1', content)

    # Lists
    def replace_enum_md(match):
        items = re.findall(r'\\item\s*(.*?)(?=\\item|\Z)', match.group(1), flags=re.DOTALL)
        return '\n' + '\n'.join([f"{i+1}. {it.strip()}" for i, it in enumerate(items)]) + '\n'

    def replace_item_md(match):
        items = re.findall(r'\\item\s*(.*?)(?=\\item|\Z)', match.group(1), flags=re.DOTALL)
        return '\n' + '\n'.join([f"- {it.strip()}" for it in items]) + '\n'

    content = re.sub(r'\\begin\{enumerate\}(.*?)\\end\{enumerate\}', replace_enum_md, content, flags=re.DOTALL)
    content = re.sub(r'\\begin\{itemize\}(.*?)\\end\{itemize\}', replace_item_md, content, flags=re.DOTALL)

    # Math blocks
    content = re.sub(r'\\\[(.*?)\\\]', r'\n$$\n\1\n$$\n', content, flags=re.DOTALL)

    # Formatting
    content = re.sub(r'\\textbf\{([^}]*)\}', r'**\1**', content)
    content = re.sub(r'\\(emph|textit)\{([^}]*)\}', r'*\1*', content)
    content = re.sub(r"``(.*?)''", r'"\1"', content)
    content = re.sub(r'--(-)?', r'—', content)
    content = re.sub(r'\\cite\{([^}]*)\}', r'[\1]', content)
    content = re.sub(r'\\begin\{center\}|\\end\{center\}', '', content)

    return content

def build_web_app():
    """Build the single-page responsive interactive HTML companion."""
    chapters_data = []
    
    for filename, title in CHAPTERS:
        filepath = os.path.join("chapters", filename)
        if not os.path.exists(filepath):
            continue
        with open(filepath, "r", encoding="utf-8") as f:
            tex_content = f.read()
            
        ch_id = os.path.splitext(filename)[0]
        html_body = tex_to_html(tex_content)
        plain_text = clean_tex_to_text(tex_content)
        
        # Extract subheadings for sidebar navigation
        subheadings = []
        for sub_match in re.finditer(r'\\subsection\{([^}]*)\}', tex_content):
            sub_title = re.sub(r'\\texorpdfstring\{([^}]*)\}\{([^}]*)\}', r'\1', sub_match.group(1))
            sub_id = re.sub(r'[^a-zA-Z0-9]+', '-', sub_title.lower()).strip('-')
            subheadings.append({"title": sub_title, "id": sub_id})
            
        chapters_data.append({
            "id": ch_id,
            "filename": filename,
            "title": title,
            "html": html_body,
            "plain_text": plain_text,
            "subheadings": subheadings
        })

    # Read introduction from main.tex
    main_intro_html = """
    <div class="companion-intro-hero">
        <div class="badge">Reading Companion & Mathematical Guide</div>
        <h1>Lectures on Entanglement, von Neumann Algebras, and Emergence of Spacetime</h1>
        <p class="subtitle">A pedagogical companion to <strong>Hong Liu (arXiv:2510.07017)</strong></p>
        <div class="meta-tags">
            <span class="tag">10 Complete Chapters</span>
            <span class="tag">Fully Accessible (Screen Reader & WCAG AAA)</span>
            <span class="tag">MathJax 3 Typesetting</span>
            <span class="tag">Interactive Search & Bookmarks</span>
        </div>
        <div class="hero-description">
            <p>This companion is meant to be read alongside Hong Liu's 119-page paper. It follows the paper's section numbers exactly, walked through with every mathematical step spelled out from scratch, derivations fully justified, and worked examples computed with concrete numbers.</p>
        </div>
        <div class="hero-actions">
            <a href="main.pdf" class="btn btn-primary" target="_blank">📄 Open Compiled PDF (102 Pages)</a>
            <button class="btn btn-secondary" onclick="scrollToChapter('01_introduction')">🚀 Start Reading Online</button>
        </div>
    </div>
    """

    html_template = f"""<!DOCTYPE html>
<html lang="en" data-theme="light">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Reading Companion: Entanglement, von Neumann Algebras & Spacetime (Hong Liu)</title>
    <meta name="description" content="Pedagogical companion to Hong Liu's Lectures on Entanglement, von Neumann Algebras, and Emergence of Spacetime (arXiv:2510.07017)">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Lora:ital,wght@0,400;0,600;1,400&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
    <!-- MathJax for rendering LaTeX math with custom macros -->
    <script>
    window.MathJax = {{
        tex: {{
            inlineMath: [['$', '$'], ['\\\\(', '\\\\)']],
            displayMath: [['$$', '$$'], ['\\\\[', '\\\\]']],
            processEscapes: true,
            macros: {{
                HH: "\\\\mathcal{{H}}",
                M: "\\\\mathcal{{M}}",
                N: "\\\\mathcal{{N}}",
                Alg: "\\\\mathcal{{A}}",
                Sscr: "\\\\mathcal{{S}}",
                BH: "B(\\\\mathcal{{H}})",
                dd: "\\\\mathrm{{d}}",
                ii: "\\\\mathrm{{i}}",
                Tr: "\\\\operatorname{{Tr}}",
                tr: "\\\\operatorname{{tr}}",
                id: "\\\\mathbf{{1}}",
                braket: ["\\\\langle #1 \\\\rangle", 1],
                ket: ["|#1\\\\rangle", 1],
                bra: ["\\\\langle #1|", 1],
                Re: "\\\\operatorname{{Re}}",
                Im: "\\\\operatorname{{Im}}"
            }}
        }},
        options: {{
            enableMenu: true
        }}
    }};
    </script>
    <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
    <style>
        :root {{
            --font-sans: 'Inter', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
            --font-serif: 'Lora', Georgia, serif;
            --font-mono: 'JetBrains Mono', monospace;
            
            --bg-primary: #ffffff;
            --bg-secondary: #f8fafc;
            --bg-surface: #f1f5f9;
            --text-primary: #0f172a;
            --text-secondary: #475569;
            --text-muted: #64748b;
            
            --border-color: #e2e8f0;
            --accent-primary: #1d4ed8;
            --accent-hover: #1e40af;
            --accent-subtle: #eff6ff;
            
            --callout-phys-bg: #f0f7ff;
            --callout-phys-border: #2563eb;
            --callout-phys-text: #1e3a8a;
            
            --callout-q-bg: #fffbeb;
            --callout-q-border: #d97706;
            --callout-q-text: #854d0e;
            
            --callout-ex-bg: #f8fafc;
            --callout-ex-border: #64748b;
            --callout-ex-text: #334155;
            
            --sidebar-width: 320px;
            --content-max-width: 860px;
            --font-size-base: 17px;
            --line-height-base: 1.75;
        }}

        [data-theme="dark"] {{
            --bg-primary: #0f172a;
            --bg-secondary: #1e293b;
            --bg-surface: #334155;
            --text-primary: #f8fafc;
            --text-secondary: #cbd5e1;
            --text-muted: #94a3b8;
            
            --border-color: #334155;
            --accent-primary: #3b82f6;
            --accent-hover: #60a5fa;
            --accent-subtle: #1e3a8a33;
            
            --callout-phys-bg: #1e293b;
            --callout-phys-border: #3b82f6;
            --callout-phys-text: #93c5fd;
            
            --callout-q-bg: #2d2618;
            --callout-q-border: #f59e0b;
            --callout-q-text: #fde68a;
            
            --callout-ex-bg: #1e293b;
            --callout-ex-border: #94a3b8;
            --callout-ex-text: #e2e8f0;
        }}

        [data-theme="sepia"] {{
            --bg-primary: #fbf0d9;
            --bg-secondary: #f4e3be;
            --bg-surface: #ebd4a4;
            --text-primary: #433422;
            --text-secondary: #5f4b32;
            --text-muted: #826c51;
            
            --border-color: #e0c896;
            --accent-primary: #9b4d1b;
            --accent-hover: #7b380f;
            --accent-subtle: #faebd7;
            
            --callout-phys-bg: #f5e9d0;
            --callout-phys-border: #8b5a2b;
            --callout-phys-text: #4a2c11;
            
            --callout-q-bg: #f9edd5;
            --callout-q-border: #c07d32;
            --callout-q-text: #593913;
            
            --callout-ex-bg: #f2e1bf;
            --callout-ex-border: #8c7355;
            --callout-ex-text: #3c2a18;
        }}

        * {{
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }}

        body {{
            font-family: var(--font-serif);
            font-size: var(--font-size-base);
            line-height: var(--line-height-base);
            color: var(--text-primary);
            background-color: var(--bg-primary);
            transition: background-color 0.2s, color 0.2s;
            overflow-x: hidden;
        }}

        /* Header Navigation */
        .top-navbar {{
            position: sticky;
            top: 0;
            z-index: 100;
            background: var(--bg-primary);
            border-bottom: 1px solid var(--border-color);
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding: 0.75rem 1.5rem;
            backdrop-filter: blur(8px);
            background: rgba(var(--bg-primary), 0.9);
        }}

        .nav-left, .nav-right {{
            display: flex;
            align-items: center;
            gap: 0.75rem;
        }}

        .brand-title {{
            font-family: var(--font-sans);
            font-weight: 700;
            font-size: 1rem;
            color: var(--text-primary);
            text-decoration: none;
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }}

        .btn {{
            font-family: var(--font-sans);
            font-size: 0.85rem;
            font-weight: 500;
            padding: 0.45rem 0.85rem;
            border-radius: 6px;
            border: 1px solid var(--border-color);
            background: var(--bg-secondary);
            color: var(--text-primary);
            cursor: pointer;
            text-decoration: none;
            display: inline-flex;
            align-items: center;
            gap: 0.4rem;
            transition: all 0.15s;
        }}

        .btn:hover {{
            background: var(--bg-surface);
            border-color: var(--accent-primary);
        }}

        .btn-primary {{
            background: var(--accent-primary);
            color: #ffffff;
            border-color: var(--accent-primary);
        }}

        .btn-primary:hover {{
            background: var(--accent-hover);
            color: #ffffff;
        }}

        /* Search Box */
        .search-container {{
            position: relative;
            width: 280px;
        }}

        .search-input {{
            width: 100%;
            font-family: var(--font-sans);
            font-size: 0.85rem;
            padding: 0.45rem 0.75rem 0.45rem 2rem;
            border-radius: 6px;
            border: 1px solid var(--border-color);
            background: var(--bg-secondary);
            color: var(--text-primary);
            outline: none;
        }}

        .search-input:focus {{
            border-color: var(--accent-primary);
            box-shadow: 0 0 0 3px var(--accent-subtle);
        }}

        .search-icon {{
            position: absolute;
            left: 0.65rem;
            top: 50%;
            transform: translateY(-50%);
            color: var(--text-muted);
            font-size: 0.85rem;
            pointer-events: none;
        }}

        /* Layout */
        .app-layout {{
            display: flex;
            min-height: calc(100vh - 56px);
        }}

        /* Sidebar */
        .sidebar {{
            width: var(--sidebar-width);
            flex-shrink: 0;
            background: var(--bg-secondary);
            border-right: 1px solid var(--border-color);
            position: sticky;
            top: 56px;
            height: calc(100vh - 56px);
            overflow-y: auto;
            padding: 1.25rem 1rem;
            display: flex;
            flex-direction: column;
            gap: 0.5rem;
        }}

        .sidebar-heading {{
            font-family: var(--font-sans);
            font-size: 0.75rem;
            text-transform: uppercase;
            letter-spacing: 0.05em;
            color: var(--text-muted);
            font-weight: 700;
            padding: 0.25rem 0.5rem;
        }}

        .nav-chapter-item {{
            font-family: var(--font-sans);
            font-size: 0.88rem;
            font-weight: 500;
            color: var(--text-secondary);
            text-decoration: none;
            padding: 0.5rem 0.65rem;
            border-radius: 6px;
            display: block;
            transition: all 0.15s;
            line-height: 1.4;
        }}

        .nav-chapter-item:hover {{
            background: var(--bg-surface);
            color: var(--text-primary);
        }}

        .nav-chapter-item.active {{
            background: var(--accent-subtle);
            color: var(--accent-primary);
            font-weight: 600;
        }}

        /* Main Content Container */
        .main-content {{
            flex: 1;
            max-width: var(--content-max-width);
            margin: 0 auto;
            padding: 2.5rem 2rem 6rem 2rem;
        }}

        /* Hero */
        .companion-intro-hero {{
            padding: 2.5rem 2rem;
            background: var(--bg-secondary);
            border-radius: 12px;
            border: 1px solid var(--border-color);
            margin-bottom: 3.5rem;
        }}

        .companion-intro-hero h1 {{
            font-family: var(--font-sans);
            font-size: 2rem;
            font-weight: 700;
            line-height: 1.25;
            margin: 0.75rem 0;
            color: var(--text-primary);
        }}

        .subtitle {{
            font-size: 1.1rem;
            color: var(--text-secondary);
            margin-bottom: 1.25rem;
        }}

        .badge {{
            display: inline-block;
            font-family: var(--font-sans);
            font-size: 0.75rem;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 0.05em;
            background: var(--accent-primary);
            color: #ffffff;
            padding: 0.2rem 0.6rem;
            border-radius: 4px;
        }}

        .meta-tags {{
            display: flex;
            flex-wrap: wrap;
            gap: 0.5rem;
            margin: 1rem 0;
        }}

        .tag {{
            font-family: var(--font-sans);
            font-size: 0.75rem;
            background: var(--bg-surface);
            color: var(--text-secondary);
            padding: 0.25rem 0.5rem;
            border-radius: 4px;
            border: 1px solid var(--border-color);
        }}

        .hero-description {{
            font-size: 0.98rem;
            color: var(--text-secondary);
            margin: 1.25rem 0;
            line-height: 1.6;
        }}

        .hero-actions {{
            display: flex;
            gap: 0.75rem;
            margin-top: 1.5rem;
        }}

        /* Article / Chapter Styling */
        .chapter-article {{
            margin-bottom: 4.5rem;
            scroll-margin-top: 80px;
        }}

        .section-title {{
            font-family: var(--font-sans);
            font-size: 1.8rem;
            font-weight: 700;
            color: var(--text-primary);
            margin-top: 2rem;
            margin-bottom: 1rem;
            padding-bottom: 0.5rem;
            border-bottom: 2px solid var(--accent-primary);
            line-height: 1.3;
        }}

        .subsection-title {{
            font-family: var(--font-sans);
            font-size: 1.35rem;
            font-weight: 600;
            color: var(--text-primary);
            margin-top: 2.2rem;
            margin-bottom: 0.8rem;
            line-height: 1.35;
        }}

        .subsubsection-title {{
            font-family: var(--font-sans);
            font-size: 1.1rem;
            font-weight: 600;
            color: var(--text-secondary);
            margin-top: 1.8rem;
            margin-bottom: 0.6rem;
        }}

        p {{
            margin-bottom: 1.2rem;
            text-align: justify;
            text-justify: inter-word;
        }}

        /* Callout Boxes */
        .callout {{
            margin: 1.5rem 0;
            border-radius: 8px;
            border-left: 4px solid transparent;
            padding: 1rem 1.25rem;
            background: var(--bg-secondary);
            box-shadow: 0 1px 3px rgba(0,0,0,0.05);
        }}

        .callout-header {{
            font-family: var(--font-sans);
            font-weight: 600;
            font-size: 0.92rem;
            display: flex;
            align-items: center;
            gap: 0.5rem;
            margin-bottom: 0.5rem;
        }}

        .callout-body {{
            font-size: 0.96rem;
            line-height: 1.65;
        }}

        .callout-physics {{
            background: var(--callout-phys-bg);
            border-color: var(--callout-phys-border);
            color: var(--callout-phys-text);
        }}

        .callout-physics .callout-title {{
            color: var(--callout-phys-border);
        }}

        .callout-question {{
            background: var(--callout-q-bg);
            border-color: var(--callout-q-border);
            color: var(--callout-q-text);
        }}

        .callout-question .callout-title {{
            color: var(--callout-q-border);
        }}

        .callout-example {{
            background: var(--callout-ex-bg);
            border-color: var(--callout-ex-border);
            color: var(--callout-ex-text);
        }}

        /* Lists */
        .styled-list {{
            margin: 1rem 0 1.25rem 1.75rem;
            line-height: 1.7;
        }}

        .styled-list li {{
            margin-bottom: 0.5rem;
        }}

        /* Tables */
        .table-container {{
            overflow-x: auto;
            margin: 1.5rem 0;
        }}

        .styled-table {{
            width: 100%;
            border-collapse: collapse;
            font-family: var(--font-sans);
            font-size: 0.9rem;
        }}

        .styled-table th, .styled-table td {{
            padding: 0.65rem 1rem;
            text-align: left;
            border-bottom: 1px solid var(--border-color);
        }}

        .styled-table th {{
            background: var(--bg-secondary);
            font-weight: 600;
            color: var(--text-primary);
        }}

        /* Math Blocks */
        .math-block {{
            overflow-x: auto;
            margin: 1.2rem 0;
            padding: 0.5rem 0;
        }}

        /* Reading Controls Bar */
        .reading-controls {{
            position: fixed;
            bottom: 1.5rem;
            right: 1.5rem;
            background: var(--bg-secondary);
            border: 1px solid var(--border-color);
            border-radius: 30px;
            padding: 0.4rem 0.8rem;
            display: flex;
            align-items: center;
            gap: 0.5rem;
            box-shadow: 0 4px 12px rgba(0,0,0,0.15);
            z-index: 90;
        }}

        /* Accessibility: Skip Link */
        .skip-link {{
            position: absolute;
            top: -40px;
            left: 0;
            background: var(--accent-primary);
            color: white;
            padding: 8px;
            z-index: 1000;
            transition: top 0.2s;
        }}

        .skip-link:focus {{
            top: 0;
        }}

        @media (max-width: 900px) {{
            .sidebar {{
                display: none;
            }}
            .main-content {{
                padding: 1.5rem 1rem 5rem 1rem;
            }}
            .top-navbar {{
                padding: 0.5rem 1rem;
            }}
            .search-container {{
                width: 180px;
            }}
        }}
    </style>
</head>
<body>
    <a href="#main-reading-content" class="skip-link">Skip to main content</a>
    
    <header class="top-navbar" role="banner">
        <div class="nav-left">
            <a href="#" class="brand-title">
                <span>🌌</span> <span>Liu Companion</span>
            </a>
        </div>
        <div class="nav-right">
            <div class="search-container" role="search">
                <span class="search-icon">🔍</span>
                <input type="text" id="searchInput" class="search-input" placeholder="Search concepts, equations..." aria-label="Search companion notes">
            </div>
            <button class="btn" id="themeToggleBtn" onclick="toggleTheme()" title="Toggle Dark/Light/Sepia Theme">🌗 Theme</button>
            <a href="main.pdf" class="btn btn-primary" target="_blank" title="Download or view PDF edition">📄 PDF (102p)</a>
        </div>
    </header>

    <div class="app-layout">
        <aside class="sidebar" role="navigation" aria-label="Table of Contents">
            <div class="sidebar-heading">Chapters</div>
            {''.join([f'<a href="#{c["id"]}" class="nav-chapter-item" id="nav-{c["id"]}">{c["title"]}</a>' for c in chapters_data])}
        </aside>

        <main class="main-content" id="main-reading-content" role="main">
            {main_intro_html}

            <div id="searchResults" style="display: none; margin-bottom: 2rem;"></div>

            <div id="chaptersContainer">
                {''.join([f'''
                <article class="chapter-article" id="{c["id"]}">
                    {c["html"]}
                </article>
                ''' for c in chapters_data])}
            </div>
        </main>
    </div>

    <div class="reading-controls" role="toolbar" aria-label="Accessibility and font controls">
        <button class="btn" onclick="adjustFontSize(-1)" title="Decrease font size">A-</button>
        <button class="btn" onclick="adjustFontSize(1)" title="Increase font size">A+</button>
        <button class="btn" onclick="toggleDyslexicFont()" id="dyslexicBtn" title="Toggle Sans/Serif reading font">Font</button>
    </div>

    <script>
    // Search index data
    const chaptersData = {json.dumps([{"id": c["id"], "title": c["title"], "text": c["plain_text"]} for c in chapters_data])};

    // Instant Search
    const searchInput = document.getElementById('searchInput');
    const searchResults = document.getElementById('searchResults');
    const chaptersContainer = document.getElementById('chaptersContainer');

    searchInput.addEventListener('input', (e) => {{
        const query = e.target.value.trim().toLowerCase();
        if (query.length < 2) {{
            searchResults.style.display = 'none';
            chaptersContainer.style.display = 'block';
            return;
        }}

        const matches = [];
        chaptersData.forEach(ch => {{
            const textLower = ch.text.toLowerCase();
            let idx = textLower.indexOf(query);
            let count = 0;
            let snippets = [];
            while (idx !== -1 && count < 3) {{
                const start = Math.max(0, idx - 60);
                const end = Math.min(ch.text.length, idx + query.length + 60);
                snippets.push('...' + ch.text.substring(start, end) + '...');
                idx = textLower.indexOf(query, idx + query.length + 1);
                count++;
            }}
            if (snippets.length > 0) {{
                matches.push({{
                    id: ch.id,
                    title: ch.title,
                    snippets: snippets
                }});
            }}
        }});

        if (matches.length === 0) {{
            searchResults.innerHTML = '<div class="callout"><p>No results found for "<strong>' + query + '</strong>".</p></div>';
        }} else {{
            let resHtml = '<h3>Search Results (' + matches.length + ' chapters found)</h3>';
            matches.forEach(m => {{
                resHtml += '<div class="callout callout-physics" style="cursor: pointer;" onclick="scrollToChapter(\\'' + m.id + '\\')">';
                resHtml += '<div class="callout-header"><span class="callout-title">' + m.title + '</span></div>';
                resHtml += '<div class="callout-body">';
                m.snippets.forEach(snip => {{
                    resHtml += '<p style="font-size: 0.9rem; margin-bottom: 0.4rem;">' + snip.replace(new RegExp(query, 'gi'), '<mark>$&</mark>') + '</p>';
                }});
                resHtml += '</div></div>';
            }});
            searchResults.innerHTML = resHtml;
        }}
        searchResults.style.display = 'block';
        chaptersContainer.style.display = 'none';
    }});

    function scrollToChapter(chId) {{
        searchInput.value = '';
        searchResults.style.display = 'none';
        chaptersContainer.style.display = 'block';
        const el = document.getElementById(chId);
        if (el) {{
            el.scrollIntoView({{ behavior: 'smooth' }});
        }}
    }}

    // Theme toggle
    const themes = ['light', 'dark', 'sepia'];
    let currentThemeIdx = 0;
    function toggleTheme() {{
        currentThemeIdx = (currentThemeIdx + 1) % themes.length;
        const newTheme = themes[currentThemeIdx];
        document.documentElement.setAttribute('data-theme', newTheme);
        localStorage.setItem('liu-companion-theme', newTheme);
    }}

    // Saved theme
    const savedTheme = localStorage.getItem('liu-companion-theme');
    if (savedTheme) {{
        document.documentElement.setAttribute('data-theme', savedTheme);
        currentThemeIdx = themes.indexOf(savedTheme);
    }}

    // Font size adjuster
    let currentFontSize = 17;
    function adjustFontSize(delta) {{
        currentFontSize = Math.min(24, Math.max(14, currentFontSize + delta));
        document.documentElement.style.setProperty('--font-size-base', currentFontSize + 'px');
        localStorage.setItem('liu-companion-fontsize', currentFontSize);
    }}

    // Font family toggle
    let isSans = false;
    function toggleDyslexicFont() {{
        isSans = !isSans;
        document.body.style.fontFamily = isSans ? 'var(--font-sans)' : 'var(--font-serif)';
    }}

    // Scroll spy for active sidebar item
    window.addEventListener('scroll', () => {{
        const articles = document.querySelectorAll('.chapter-article');
        let current = '';
        articles.forEach(art => {{
            const top = art.getBoundingClientRect().top;
            if (top <= 120) {{
                current = art.getAttribute('id');
            }}
        }});
        if (current) {{
            document.querySelectorAll('.nav-chapter-item').forEach(item => {{
                item.classList.remove('active');
            }});
            const activeNav = document.getElementById('nav-' + current);
            if (activeNav) activeNav.classList.add('active');
        }}
    }});
    </script>
</body>
</html>
"""
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html_template)
    print("Generated index.html successfully.")

def build_markdown_editions():
    """Build markdown editions in markdown/ directory."""
    os.makedirs("markdown", exist_ok=True)
    full_companion_content = [
        "# Reading Companion to Hong Liu's Lectures on Entanglement, von Neumann Algebras, and Emergence of Spacetime\n",
        "**arXiv:2510.07017**\n\n---\n"
    ]

    for filename, title in CHAPTERS:
        filepath = os.path.join("chapters", filename)
        if not os.path.exists(filepath):
            continue
        with open(filepath, "r", encoding="utf-8") as f:
            tex_content = f.read()

        md_content = tex_to_markdown(tex_content)
        md_filename = os.path.splitext(filename)[0] + ".md"
        md_path = os.path.join("markdown", md_filename)
        
        with open(md_path, "w", encoding="utf-8") as f:
            f.write(f"# {title}\n\n" + md_content)
            
        full_companion_content.append(f"\n\n---\n\n{md_content}")

    with open(os.path.join("markdown", "full_companion.md"), "w", encoding="utf-8") as f:
        f.write('\n'.join(full_companion_content))
        
    print("Generated Markdown chapters and markdown/full_companion.md successfully.")

if __name__ == "__main__":
    build_web_app()
    build_markdown_editions()
