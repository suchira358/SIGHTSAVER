from flask import Flask, request, jsonify
from image_model import detect_product
from comparator import compare

app = Flask(__name__)

@app.route("/upload", methods=["POST"])
def upload():

    file = request.files["image"]

    file_path = "temp.jpg"

    file.save(file_path)

    product = detect_product(file_path)

    best, all_results = compare(product)

    return jsonify({
        "detected_product": product,
        "best_option": best,
        "all_results": all_results
    })

if __name__ == "__main__":
    app.run(debug=True)
    
