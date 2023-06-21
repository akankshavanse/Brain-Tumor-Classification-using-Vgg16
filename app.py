import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image
import base64

from streamlit_option_menu import option_menu
import smtplib

st.set_page_config(layout="wide")


model = tf.keras.models.load_model('./adamTumor.h5')


def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"jpg"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
add_bg_from_local('1.jpg') 
st.set_option('deprecation.showfileUploaderEncoding', False)

def predict_class(image, model):
    image = tf.cast(image, tf.float32)
    image = tf.image.resize(image, [224, 224])
    image = np.expand_dims(image, axis=0)
    prediction = model.predict(image)
    return prediction

def get_treatment_recommendation(result):
    if result == 'glioma_tumor':
        return '''Identification of symptoms:
Headaches: Persistent or worsening headaches, often accompanied by nausea or vomiting.
Seizures: Gliomas can cause seizures, which may manifest as uncontrolled movements, altered consciousness, or unusual sensations.
Neurological deficits: Weakness, numbness, or tingling in the limbs, difficulty speaking or understanding speech, changes in vision, coordination problems, or problems with memory and cognition.
Behavioral and personality changes: Irritability, mood swings, personality changes, or changes in social behavior.
Control of glioma tumors:
Medical evaluation: Seek medical attention if you experience concerning symptoms. A healthcare professional will evaluate your symptoms, conduct a thorough neurological examination, and order imaging tests (such as MRI) to diagnose and characterize the tumor.
Treatment planning: The treatment approach depends on several factors, including the tumor's grade, location, and size, as well as the patient's overall health and preferences.
Surgery: Surgical removal of the tumor is often a primary treatment for gliomas, if feasible. The goal is to remove as much of the tumor as possible while minimizing damage to healthy brain tissue. In some cases, complete removal may not be possible due to the tumor's location or size.
Radiation therapy: Radiation may be used in conjunction with surgery or as the primary treatment for gliomas. It targets remaining tumor cells and helps control tumor growth.
Chemotherapy: Depending on the type and grade of glioma, chemotherapy drugs may be prescribed. They can be administered orally, intravenously, or directly into the tumor site.
    '''

    elif result == 'meningioma_tumor':
        return '''Identification of symptoms:

Headaches: Persistent or worsening headaches, particularly in the morning or upon waking up.
Seizures: Uncontrolled movements, altered consciousness, or unusual sensations.
Neurological deficits: Weakness, numbness, tingling, difficulty speaking or understanding speech, vision changes, hearing loss, balance problems, or coordination difficulties.
Cognitive and personality changes: Memory problems, difficulty concentrating, confusion, or personality changes.
Visual disturbances: Blurred vision, double vision, partial or complete loss of vision, or visual field deficits.
Nausea and vomiting: Persistent nausea and vomiting.
Fatigue and weakness: Persistent fatigue, weakness, or a general feeling of malaise.
Controlling meningioma tumors:

Medical evaluation: Seek medical attention for proper diagnosis and evaluation of symptoms.
Treatment planning: A multidisciplinary team of healthcare professionals will develop an individualized treatment plan based on the tumor's characteristics and the patient's overall health.
Surgery: Surgical removal of the tumor is often the primary treatment. The goal is to remove as much of the tumor as possible while minimizing damage to surrounding healthy brain tissue.
Radiation therapy: Radiation may be used after surgery to target any remaining tumor cells or as the primary treatment for inoperable or difficult-to-access tumors.
Medications: Medications may be prescribed to manage symptoms associated with meningiomas, such as corticosteroids to reduce swelling or antiepileptic drugs to control seizures.
Follow-up care: Regular monitoring and imaging scans are essential to track tumor growth and assess the effectiveness of treatment.
It's important to consult with healthcare professionals to determine the most appropriate approach for identifying symptoms, controlling meningioma tumors, and managing individual cases.
'''
    elif result == 'no_tumor':
        st.balloons()
        return 'No treatment needed. The brain is healthy.'
        
    
    elif result == 'pituitary_tumor':
        return '''
        Identification of symptoms:
Hormonal disturbances: Pituitary tumors can disrupt the normal production and regulation of hormones, leading to various symptoms. These symptoms can include unexplained weight gain or loss, changes in appetite, fatigue, irregular or absent menstrual periods, decreased libido, infertility, growth abnormalities in children, and changes in body hair distribution.
Vision problems: Tumors that grow large enough can compress the optic nerves or optic chiasm, resulting in visual disturbances. These may include blurry or double vision, peripheral vision loss, or difficulty with visual fields.
Headaches: Persistent or severe headaches are common, typically localized to the front or sides of the head.
Neurological symptoms: Larger tumors can exert pressure on surrounding brain structures, leading to symptoms such as dizziness, difficulty with coordination, facial numbness or tingling, and memory or cognitive problems.
Controlling pituitary tumors:
Medical evaluation: Seek medical attention if you experience concerning symptoms. An evaluation by a healthcare professional will involve a comprehensive medical history, physical examination, and potentially hormone level testing and imaging studies (such as MRI) to diagnose and characterize the tumor.
Treatment planning: The treatment approach depends on the type, size, and behavior of the tumor, as well as the individual's symptoms and overall health.
Observation: Small, asymptomatic tumors may be monitored with regular imaging scans to track their growth and determine if treatment is necessary.
Medications: Certain pituitary tumors, particularly those producing excessive hormones, can be managed with medication to control hormone levels or shrink the tumor. Medications may include dopamine agonists, somatostatin analogs, or other hormone-modulating drugs.
Surgery: Surgical removal of the tumor is often recommended for larger tumors, those causing significant symptoms, or tumors that are not responding to medication. The goal is to remove the tumor while preserving normal pituitary function. Minimally invasive techniques, such as transsphenoidal surgery, are commonly used.
Radiation therapy: Radiation may be used as a primary treatment for tumors that cannot be completely removed surgically, or as an adjuvant therapy after surgery to target any remaining tumor cells'''
        
    else:
        return 'Unknown disease. Consult an expert for proper treatment.'




def send_text_message(contact_number, feedback_message): 
    # feedback_message = 
    st.success("Message sent successfully!")

EXAMPLE_NO = 1
def streamlit_menu(example=1):
    if example == 1:
        # 1. as sidebar menu
        with st.sidebar:
            selected = option_menu(
                menu_title="Main Menu",  # required
                options=["Home", "Tumor Classifier", "Contact"],  # required
                icons=["house", "book", "envelope"],  # optional
                menu_icon="cast",  # optional
                default_index=0,  # optional
            )
        return selected

    if example == 2:
        # 2. horizontal menu w/o custom style
        selected = option_menu(
            menu_title=None,  # required
            options=["Home", "Tumor Classifier", "Contact"],  # required
            icons=["house", "book", "envelope"],  # optional
            menu_icon="cast",  # optional
            default_index=0,  # optional
            orientation="horizontal",
        )
        return selected
    

    if example == 3:
        # 2. horizontal menu with custom style
        selected = option_menu(
            menu_title=None,  # required
            options=["Home", "Tumor Classifier", "Contact"],  # required
            icons=["house", "book", "envelope"],  # optional
            menu_icon="cast",  # optional
            default_index=0,  # optional
            orientation="horizontal",
            styles={
                "container": {"padding": "0!important", "background-color": "#fafafa"},
                "icon": {"color": "orange", "font-size": "25px"},
                "nav-link": {
                    "font-size": "25px",
                    "text-align": "left",
                    "margin": "0px",
                    "--hover-color": "#eee",
                },
                "nav-link-selected": {"background-color": "blue"},
            },
        )
        return selected
    
selected = streamlit_menu(example=EXAMPLE_NO)

if selected == "Home":
    st.title(f"{selected}")
    st.header("Welcome to Brain Tumor Classifier! ")
    st.subheader(f'''
    This web app helps to classify Brain tumor using MRI scans and provides treatment recommendations.
    This web app is created using Streamlit, TensorFlow, PIL, and base64.
    It utilizes a deep learning model to classify Brain tumor.
    Upload an MRI image of Brain, and the model will predict the disease. 
    The corresponding treatment recommendation will be displayed.''')
if selected == "Tumor Classifier":
    st.title(f"{selected}")
    file = st.file_uploader("Upload an Brain MRI image", type=["jpg", "png","jpeg"])
    if file is None:
        st.text('Waiting for upload....')
    else:
        slot = st.empty()
        slot.text('Running inference....')

        test_image = Image.open(file)
        st.image(test_image, caption="Input Image", width=400)

        pred = predict_class(np.asarray(test_image), model)

        class_names = ['glioma_tumor', 'meningioma_tumor', 'no_tumor', 'pituitary_tumor']
        result = class_names[np.argmax(pred)]
        output = 'The image is ' + result
        st.success(output)

        treatment = get_treatment_recommendation(result)
        st.info('Treatment Recommendation:')
        st.write(treatment)

        
if selected == "Contact":
    st.title(f"{selected}")
    contact_number = 0 
    st.header("Feedback Form")
    feedback_message = st.text_area("Message", height=200)
    if st.button("Send Message"):
        if feedback_message.strip() == "":
            st.warning("Please enter a feedback message.")
        else:
            send_text_message(contact_number, feedback_message)
    col1, col2 = st.columns(2)
    if col1.button("👍"):
        st.success("You liked the app, Thank you!")
    if col2.button("👎"):
        st.error("You disliked the app!")