from flask import Flask, render_template, request, session, make_response
import openai
import pdfkit
import re

app = Flask(__name__)

# Set your OpenAI API Key here
openai.api_key = "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"
openai.api_base = "https://openrouter.ai/api/v1"

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/generate', methods=['POST'])
def generate():
    company_name = request.form['company_name']
    industry_type = request.form['industry_type']
    target_audience = request.form['target_audience']
    services = request.form['services']
    contact = request.form['contact']
    color_theme = request.form.get('color_theme', 'Any')
    output_type = request.form['output_type']

    prompt = f"""
    Create a professional and creative {output_type} for a company.
    
    Company Name: {company_name}
    Industry: {industry_type}
    Target Audience: {target_audience}
    Services: {services}
    Contact Info: {contact}
    Preferred Colors: {color_theme}

    Include:
    - Company intro
    - Highlights of services
    - Call-to-action
    - Visual theme suggestion
    """

    response = openai.ChatCompletion.create(
    model="openai/gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a professional marketing copywriter."},
        {"role": "user", "content": prompt}
    ],
    temperature=0.7,
    max_tokens=600
)

    generated_content = response['choices'][0]['message']['content']
    #return generated_content  # ✅ THIS LINE FIXES THE ERROR
    return render_template('result.html', content=generated_content)



# 👇 This part is important!
if __name__ == '__main__':
    app.run(debug=True)