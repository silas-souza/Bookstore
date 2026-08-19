from django.http import JsonResponse, HttpResponse  # <-- ADICIONA HttpResponse
from django.shortcuts import render

def hello_world(request):
    return JsonResponse({"message": "Hello, World!"})

def update(request):
    return JsonResponse({"status": "updated"})

# ADICIONE ESTA FUNÇÃO:
def home(request):
    return HttpResponse("""
        <!DOCTYPE html>
        <html>
        <head>
            <title>📚 Bookstore API</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    max-width: 800px;
                    margin: 50px auto;
                    padding: 20px;
                    background: #f5f5f5;
                }
                .container {
                    background: white;
                    padding: 30px;
                    border-radius: 10px;
                    box-shadow: 0 2px 10px rgba(0,0,0,0.1);
                }
                h1 { color: #2c3e50; }
                .links { margin-top: 20px; }
                .links a {
                    display: inline-block;
                    margin: 5px 10px 5px 0;
                    padding: 10px 20px;
                    background: #3498db;
                    color: white;
                    text-decoration: none;
                    border-radius: 5px;
                }
                .links a:hover { background: #2980b9; }
                .links a.admin { background: #e74c3c; }
                .links a.admin:hover { background: #c0392b; }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>📚 Bookstore API</h1>
                <p>Sua API de livraria está no ar!</p>
                <div class="links">
                    <a href="/api/v1/product/">📦 Produtos</a>
                    <a href="/api/v1/category/">🏷️ Categorias</a>
                    <a href="/admin/" class="admin">🔧 Admin</a>
                    <a href="/hello/">👋 Hello World</a>
                </div>
            </div>
        </body>
        </html>
    """)
