from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def home():
    triforce = """
       /\\
      /  \\
     /    \\
    /______\\
   /\\      /\\
  /  \\    /  \\
 /    \\  /    \\
/______\\/______\\
"""
    return render_template_string('''
    <html>
        <head>
            <style>
                @keyframes pulse {
                    0% { color: gold; }
                    50% { color: white; }
                    100% { color: gold; }
                }
                .triforce {
                    animation: pulse 2s infinite;
                }
            </style>
        </head>
        <body style="background-color: black; font-family: monospace; text-align: center; padding-top: 50px;">
            <h1 style="color: gold;">The Triforce</h1>
            <pre class="triforce">{{ triforce }}</pre>
        </body>
    </html>
    ''', triforce=triforce)

if __name__ == '__main__':
    app.run(debug=True)