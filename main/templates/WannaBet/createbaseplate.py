import sys

# This creates a basic template for a new page
# Usage createbaseplate.py <filename>

def html(filename):
    # data = []
    with open(filename, 'w') as b:
        b.write("{% extends 'WannaBet/base.html' %}\n\n{% load static %}\n\n{% block content %}\n\n{% endblock %}\n\n")
        b.write("<style>\n\n</style>\n\n\n<script>\n\n<\script>")
    print(f"New file created : {filename}")

def main():
    filename = sys.argv[1]
    html(f"{filename}.html")

if __name__ == "__main__":
   main()    
