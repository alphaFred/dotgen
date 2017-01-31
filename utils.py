def persist_dot_text(node, parser, path):
    dot_text = parser.to_dot(node)

    with open(path, 'w') as dot_file:
        dot_file.write(dot_text)
