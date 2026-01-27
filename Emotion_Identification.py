from tkinter import *
import pickle

model = pickle.load(open("model.pkl", "rb"))
ve = pickle.load(open("vectorizer.pkl", "rb"))
le = pickle.load(open("label_encoder.pkl", "rb"))

def predict_emotions():
    sentence=text_input.get(1.0,END)
    s=ve.transform([sentence])
    predicted_emotion=model.predict(s)
    emotion.set(le.inverse_transform(predicted_emotion)[0])

def remove_text():
    text_input.delete(1.0, END)
    emotion.set("")

window = Tk()
window.title("Human Emotion Detection")
window.geometry("500x400")
window.resizable(False, False)

heading = Label(
    window,
    text="Human Emotion Detection from Text",
    font=("Arial", 16, "bold")
)
heading.pack()
heading.place(x=60, y=10)

text_label = Label(
    window,
    text="Enter your sentence:",
    font=("Arial", 12)
)
text_label.pack()
text_label.place(x=20, y=50)

text_input = Text(
    window,
    height=5,
    width=50,
    font=("Arial", 11)
)
text_input.pack()
text_input.place(x=40, y=80)

predict_btn = Button(
    window,
    text="Predict Emotion",
    font=("Arial", 12),
    bg="#4CAF50",
    fg="white",
    command=predict_emotions
)
predict_btn.pack()
predict_btn.place(x=180, y=200)

emotion_label = Label(
    window,
    text="Predicted Emotion:",
    font=("Arial", 12)
)
emotion_label.pack()
emotion_label.place(x=20, y=250)

emotion = StringVar()
emotion_entry = Entry(
    window,
    textvariable=emotion,
    font=("Arial", 12),
    width=25,
    justify="center",
    state="readonly"
)
emotion_entry.pack()
emotion_entry.place(x=120, y=280)

refresh_btn = Button(
    window,
    text="Refresh",
    font=("Arial", 12),
    bg="#4CAF50",
    fg="white",
    command=remove_text
)
refresh_btn.pack()
refresh_btn.place(x=205, y=330)

window.mainloop()