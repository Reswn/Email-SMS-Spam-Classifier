import streamlit as st
import pickle
import string
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from sklearn.exceptions import NotFittedError

# =================== Setup ===================
nltk.download('punkt')
nltk.download('stopwords')

ps = PorterStemmer()

# =================== Styling ===================
st.markdown("""
    <style>
    .main-title {
        font-size: 36px;
        font-weight: bold;
        text-align: center;
        color: #fff;
        margin-bottom: 30px;
    }

    .result-box {
        padding: 20px;
        border-radius: 10px;
        text-align: center;
        font-size: 24px;
        font-weight: bold;
        margin-top: 20px;
    }

    .spam {
        background-color: #ffcccc;
        color: #cc0000;
        border: 2px solid #cc0000;
    }

    .not-spam {
        background-color: #ccffcc;
        color: #006600;
        border: 2px solid #006600;
    }

    .stTextArea textarea {
        font-size: 16px;
        line-height: 1.6;
    }
    </style>
""", unsafe_allow_html=True)

# =================== Fungsi Preprocessing ===================
def transform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)

    y = []
    for i in text:
        if i.isalnum():
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        y.append(ps.stem(i))

    return " ".join(y)

# =================== Load Model ===================
try:
    tfidf = pickle.load(open('vectorizer.pkl', 'rb'))
    model = pickle.load(open('model.pkl', 'rb'))
except Exception as e:
    st.error(f"Gagal memuat model: {e}")
    st.stop()

# =================== UI ===================
st.markdown('<div class="main-title">📧 Email/SMS Spam Classifier</div>', unsafe_allow_html=True)

input_sms = st.text_area("Enter the message below 👇", height=150)

if st.button('🔍 Predict'):
    if input_sms.strip() == "":
        st.warning("⚠️ Please enter a message.")
    else:
        # Preprocessing
        transformed_sms = transform_text(input_sms)
        vector_input = tfidf.transform([transformed_sms]).toarray()


        try:
            result = model.predict(vector_input)[0]
            if result == 1:
                st.markdown('<div class="result-box spam">🚫 Spam</div>', unsafe_allow_html=True)
            else:
                st.markdown('<div class="result-box not-spam">✅ Not Spam</div>', unsafe_allow_html=True)
        except NotFittedError:
            st.error("Model belum dilatih. Silakan fit model terlebih dahulu.")
