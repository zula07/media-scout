from flask import Flask, render_template, request, jsonify
from googlesearch import search

app = Flask(__name__)

def perform_search(query_name):
    variations = [
        f"{query_name} izle",
        f"{query_name} watch online",
        f"{query_name} full movie",
        f"{query_name} izleme sitesi",
        f"{query_name} stream"
    ]
    found_links = set()
    for variation in variations:
        try:
            for url in search(variation, num_results=5, sleep_interval=2):
                found_links.add(url)
        except Exception as e:
            print(f"Hata: {e}")
            continue
    return list(found_links)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['GET'])
def search_route():
    query = request.args.get('q')
    if not query:
        return jsonify({"error": "Film adı boş olamaz!"}), 400
    
    links = perform_search(query)
    return jsonify({"links": links})

if __name__ == '__main__':
    print("🚀 MediaScout Web Uygulaması AĞ MODUNDA Başlatıldı!")
    print("🔗 Bilgisayarından erişim: http://127.0.0.1:5000")
    print("📱 Diğer cihazlardan erişim: http://192.168.1.53:5000")
    app.run(host='0.0.0.0', port=5000, debug=True)
