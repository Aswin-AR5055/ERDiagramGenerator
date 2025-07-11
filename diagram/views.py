from django.shortcuts import render
from .forms import ERInputForm

def parse_er_text_to_mermaid(er_text):
    lines = er_text.strip().split('\n')
    entities = {}
    relationships = []

    for line in lines:
        line = line.strip()
        if not line:
            continue  # skip empty lines

        if '->' in line:
            # Relationship
            left, right = line.split('->')
            relationships.append((left.strip(), right.strip()))
        elif '(' in line and ')' in line:
            # Entity definition
            entity_name = line.split('(')[0].strip()
            attributes = line[line.find('(')+1 : line.find(')')].split(',')
            entity_attrs = []
            for attr in attributes:
                attr = attr.strip()
                if ':' in attr:
                    attr_name, attr_type = attr.split(':')
                    attr_name = attr_name.strip()
                    attr_type = attr_type.strip()
                else:
                    attr_name = attr
                    # Use simple default: 'id' = int, otherwise string
                    if attr_name.lower() == 'id':
                        attr_type = 'int'
                    else:
                        attr_type = 'string'
                entity_attrs.append((attr_type, attr_name))
            entities[entity_name] = entity_attrs

    # Convert to Mermaid syntax
    mermaid_lines = ["erDiagram"]
    for entity, attrs in entities.items():
        mermaid_lines.append(f"    {entity} {{")
        for attr_type, attr_name in attrs:
            mermaid_lines.append(f"        {attr_type} {attr_name}")
        mermaid_lines.append("    }")

    for left, right in relationships:
        mermaid_lines.append(f"    {left} ||--o{{ {right} : has")

    return '\n'.join(mermaid_lines)

def home(request):
    diagram_code = None
    form = ERInputForm()

    if request.method == 'POST':
        form = ERInputForm(request.POST)
        if form.is_valid():
            er_text = form.cleaned_data['er_text']
            diagram_code = parse_er_text_to_mermaid(er_text)

    return render(request, 'diagram/home.html', {
        'form': form,
        'diagram_code': diagram_code
    })

def logo(request):
    return render(request, 'logo/logo.html')
