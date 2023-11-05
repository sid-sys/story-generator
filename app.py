from flask import Flask, request, jsonify
from waitress import serve
import openai
import os


app = Flask(__name__)

os.environ['OPENAI_API_KEY'] = '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'
openai.api_key = os.getenv("OPENAI_API_KEY")

def BasicGeneration(userPrompt):
    inputPrompt = f"""I want you to act as a storyteller. You will come up with entertaining stories that are engaging, imaginative and captivating for the audience. It can be fairy tales, educational stories or any other type of stories which has the potential to capture people's attention and imagination. Depending on the target audience, you may choose specific themes or topics for your storytelling session e.g., if it’s children then you can talk about animals; If it’s adults then history-based tales might engage them better etc. My first request is: {userPrompt}"""
    completion = openai.ChatCompletion.create(model="gpt-3.5-turbo",messages=[{"role":"user","content":inputPrompt}])
    # completion = openai.ChatCompletion.create(model="gpt-4",messages=[{"role":"user","content":inputPrompt}])
    return completion.choices[0].message.content

@app.route('/generate', methods=['POST', 'GET'])
def generate_story():
    if request.method == 'POST':
        data = request.get_json()
        user_prompt = data.get('prompt')
        response = BasicGeneration(user_prompt)
        return jsonify({"response": response})
    else:
        return jsonify({"message": "Welcome to the Storytelling API! Send a POST request with 'prompt' parameter to generate a story."})

# if __name__ == '__main__':
#     app.run(debug=True)

serve(app,host='0.0.0.0',port=8080)