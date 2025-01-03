from flask import Flask, render_template, request, jsonify
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch
from nltk.tokenize import sent_tokenize

# Flask app
app = Flask(__name__)

# Device setup
device = "cuda" if torch.cuda.is_available() else "cpu"

# Load tokenizer and model
tokenizer = AutoTokenizer.from_pretrained("humarin/chatgpt_paraphraser_on_T5_base")
model = AutoModelForSeq2SeqLM.from_pretrained("humarin/chatgpt_paraphraser_on_T5_base").to(device)


# Paraphrase one sentence
def paraphrase_one_sentence(
        question,
        num_beams=5,
        num_beam_groups=5,
        num_return_sequences=1,
        repetition_penalty=10.0,
        diversity_penalty=3.0,
        no_repeat_ngram_size=2,
        temperature=0.7,
        max_length=128
):
    input_ids = tokenizer(
        f'paraphrase: {question}',
        return_tensors="pt", padding="longest",
        max_length=max_length,
        truncation=True,
    ).input_ids.to(device)

    outputs = model.generate(
        input_ids, temperature=temperature, repetition_penalty=repetition_penalty,
        num_return_sequences=num_return_sequences, no_repeat_ngram_size=no_repeat_ngram_size,
        num_beams=num_beams, num_beam_groups=num_beam_groups,
        max_length=max_length, diversity_penalty=diversity_penalty
    )

    res = tokenizer.batch_decode(outputs, skip_special_tokens=True)

    return res


# Paraphrase paragraph
def paraphrase(paragraph):
    sentences = sent_tokenize(paragraph)
    paraphrased_sentences = []

    for sentence in sentences:
        paraphrased_result = paraphrase_one_sentence(sentence, num_beams=2, num_beam_groups=2, num_return_sequences=1,
                                                     max_length=128)
        paraphrased_sentences.append(paraphrased_result[0])

    return " ".join(paraphrased_sentences)


# Flask routes
@app.route("/")
def home():
    return render_template("index.html")


@app.route("/paraphrase", methods=["POST"])
def paraphrase_text():
    data = request.json
    input_text = data.get("text", "")
    if not input_text.strip():
        return jsonify({"error": "Input text is empty"}), 400

    paraphrased_text = paraphrase(input_text)
    return jsonify({"paraphrased_text": paraphrased_text})


if __name__ == "__main__":
    app.run(debug=True)
