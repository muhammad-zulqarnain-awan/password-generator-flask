from flask import Flask, render_template, request
import random
import string

app = Flask(__name__)


@app.route('/', methods=['GET','POST'])
def home():
    
    if request.method == 'POST':
        pass_length = int(request.form.get('length'))
        generated_password = ''

        char_list = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation

        if pass_length > 0 and pass_length <= 12:
            generated_password = ''.join(random.choice(char_list) for _ in range(pass_length))
            return render_template('home.html', generated_password=generated_password)
        else:
            generated_password = 'Password length should be in between 1 and 12'
            return render_template('home.html', generated_password=generated_password)

if __name__ == "__main__":
    app.run(port=5000)