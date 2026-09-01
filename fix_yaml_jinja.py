import re
import glob
import os

files = glob.glob("template/.github/workflows/*.jinja")
for f in files:
    with open(f, 'r') as file:
        content = file.read()
    
    # We want to replace ${{ ... }} with {% raw %}${{ ... }}{% endraw %}
    # But only if it's not already wrapped.
    content = re.sub(r'(?<!{% raw %})(\${{.*?}})(?!{% endraw %})', r'{% raw %}\1{% endraw %}', content)
    
    with open(f, 'w') as file:
        file.write(content)

