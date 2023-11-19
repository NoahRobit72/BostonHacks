from flask import Flask, render_template, request

# Scripts
from processImage import *  # Jared: process image and get the objects
from getStory import *      # Mete: create AI-generated story involving objects
from getVoices import *     # Jilin: assign AI-generated voice to objects
from ObjectChar import *    # Objects' class

app = Flask(__name__)



# Receive the user picture; get the identified objects and their attributes
@app.route('/processImage', methods=['POST'])
def processImage():
    #charsAndContext = genCharAndContext()
    sampleOutput = """Name: Benjamin Banana
Age Group: Adult
Gender: Man
Object: Banana
Personality: Cheerful, optimistic
Appearance: Bright yellow with a friendly smile

Name: Amelia Apple
Age Group: Teen
Gender: Woman
Object: Apple
Personality: Ambitious, determined
Appearance: Shiny red with a confident aura

Beginning Prompt:
On a small wooden table, a diverse group of fruits gathered. Benjamin Banana, the cheerful adult, and Amelia Apple, the ambitious teenager, stood side by side, among others who were yet to be named. Their vibrant colors and distinct personalities made each fruit unique, just like their presence around the table. As the narrator, I couldn't help but wonder what adventures awaited these fruits beyond the confines of this ordinary setting. Little did they know that fate had something extraordinary in store for them. It all started when a mischievous wind blew open the window, setting the stage for an unexpected journey that would forever change their lives."""



    return charsAndContext

# Send the generated stories and voice to the frontend
@app.route('/toDatabase', methods=['POST'])
def toDatabase():
    return "hey!"

if __name__ == '__main__':
    app.run(debug=True)
