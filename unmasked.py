import streamlit as st
from streamlit_extras.switch_page_button import switch_page

st.set_page_config(layout="wide", page_title='Unmasked', page_icon = 'logo.jpg')

with st.empty():
    st.markdown(
        """
        <style>
        .main .block-container {
            padding-top: 0rem;
            padding-bottom: 2rem;
            padding-left: 0rem;
            padding-right: 0rem;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

html_code = """
<div id="vanta-background" style="position: absolute; width: 100%; height: 100%; z-index: -1;"></div>

<div style="display: flex; position: relative; z-index: 1; padding: 2rem; color: black; height: 80vh;">
    <!-- Left side content with static text -->
    <div style="flex: 2.1; text-align: left; padding-top: 300px; padding-right:100px;">  <!-- Adjust this value to move text down -->
        <h1 style="font-family: 'Times New Roman', serif; font-size: 4.5em; margin: 0;">Unmasked</h1>
        <div id="animated-text" style="font-family: 'Lucida Handwriting', cursive; font-size: 1.2em;">
            <!-- Words will be inserted here by JavaScript -->
        </div>
    </div>

    <!-- Right side with individual card display -->
    <div style="flex: 1; display: flex; align-items: center; justify-content: center;">
        <div id="carousel" style="position: relative; width: 100%; height: 450px;">
            <!-- Cards -->
            <div class="card active" style="width: 21rem; height: 450px; margin: 10px;">
    <img class="card-img-top" src="https://i.ibb.co/50VwRPz/track.png" alt="Card image cap" width="100%">
    <div class="card-body">
        <p class="card-text"><br>▶ Tracks user locations via Ngrok ports when links are clicked.<br><br>▶ Logs cyber-related activities for enhanced security analysis.<br><br>▶ AI-driven deepfake detection with 93% accuracy.<br><br>▶ Real-time monitoring of flagged media across digital platforms.</p>
    </div>
</div>
<div class="card" style="width: 21rem; height: 450px; margin: 10px;">
    <img class="card-img-top" src="https://i.ibb.co/q33VY8pM/deepfake.png" alt="Card image cap" width="100%">
    <div class="card-body">
        <p class="card-text"><br>▶ Intelligent fake news detection using agentic AI systems.<br><br>▶ Automated scanning of fact-checking databases via RAG.<br><br>▶ URL-based verification against misinformation sources.<br><br>▶ Real-time analysis of online articles for accuracy.</p>
    </div>
</div>
<div class="card" style="width: 21rem; height: 450px; margin: 10px;">
    <img class="card-img-top" src="https://i.ibb.co/cSkB3dtB/news2.png" alt="Card image cap" width="100%">
    <div class="card-body">
        <p class="card-text"><br>▶ Social media video scraping for deepfake detection.<br><br>▶ Automated flagging of manipulated content.<br><br>▶ AI-based classification of authentic vs fake media.<br><br>▶ Integrated dashboard for forensic analysis.</p>
    </div>
</div>
<div class="card" style="width: 21rem; height: 450px; margin: 10px;">
    <img class="card-img-top" src="https://i.ibb.co/DfxPWmmz/news.png" alt="Card image cap" width="100%">
    <div class="card-body">
        <p class="card-text"><br>▶ Interactive carousels for verified and flagged news.<br><br>▶ Cross-platform monitoring for deepfake content.<br><br>▶ Automated reporting with timeline-based analysis.<br><br>▶ Dynamic selection of detection parameters for detailed insights.</p>
    </div>
</div>

            </div>
        </div>
    </div>
</div>

<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r134/three.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/vanta@latest/dist/vanta.fog.min.js"></script>
<script>
VANTA.FOG({
  el: "#vanta-background",
  mouseControls: true,
  touchControls: true,
  gyroControls: false,
  minHeight: 200.00,
  minWidth: 400.00,
    highlightColor: 0xffb3,
  midtoneColor: 0xfff0,
  lowlightColor: 0xff77,
  baseColor: 0xebfffa,
  speed: 6.00
});

// Card rotation function for a sequential fade effect
let currentCardIndex = 0;
const cards = document.querySelectorAll('#carousel .card');
const totalCards = cards.length;

function showNextCard() {
    // Hide all cards first
    cards.forEach(card => card.classList.remove('active', 'fade-in'));

    // Show only the current card
    cards[currentCardIndex].classList.add('active', 'fade-in');

    // Move to the next card in a circular manner
    currentCardIndex = (currentCardIndex + 1) % totalCards;
}

setInterval(showNextCard, 4000);

// Fading text animation function
const text = "An app for deepfake detection that accurately tracks cyber-related user activity and detects fake news, delivering precise insights even in complex digital environments.";
const words = text.split(" ");
const animatedTextDiv = document.getElementById('animated-text');

function fadeInWords() {
    animatedTextDiv.innerHTML = ""; // Clear previous content

    words.forEach((word, index) => {
        const span = document.createElement('span');
        span.textContent = word + " "; // Add space for separation
        span.style.opacity = 0; // Start with transparent text
        span.style.transition = "opacity 1s ease"; // Set transition
        animatedTextDiv.appendChild(span);

        // Delay the fade-in for each word
        setTimeout(() => {
            span.style.opacity = 1; // Fade in the word
        }, index * 300); // 500ms delay for each word
    });

    // Start over after all words are shown
    setTimeout(fadeInWords, (words.length * 300) + 4000); // 3000ms before restarting
}

// Start the fading animation
fadeInWords();
</script>

<style>
/* Styling for individual card display */
.card {
    width: 21rem;
    height: 450px;
    margin: 0 10px;
    background-color: rgb(0,0,0);
    border-radius: 8px;
    box-shadow: 0 6px 10px rgba(0,0,0,0.6);
    text-align: left;
    color: white; 
    opacity: 0;
    position: absolute;
    transition: opacity 2s ease;
    padding: 15px;
}
.card-img-top {
    border-top-left-radius: 8px;
    border-top-right-radius: 8px;
    height: 200px; 
}

/* Visibility settings for active card */
.card.active {
    opacity: 1;
    z-index: 1; /* Ensures the active card is on top */
}

.fade-in {
    opacity: 1; /* Ensures the card fades into view smoothly */
}

/* Animation for the text */
#animated-text {
    transition: opacity 1s ease; /* Transition for fading */
}
</style>
"""

st.components.v1.html(html_code, height=600, scrolling=False)

col1, col2 = st.columns([0.05, 1])
with col2: 
    st.markdown("""<p style="font-family: 'Times New Roman', serif; font-size: 2.1em;">• Explore our Functionalities</p>""", unsafe_allow_html=True)
    st.markdown(" ")
c0,c1,c2,c3,c4, c5= st.columns([0.07,1,1,1,1, 0.07])

def video_html(video_path):
    return f"""
        <div style="width:100%; height:auto; max-width:560px; overflow:hidden;">
        <iframe id="ytplayer" 
                src={video_path} 
                frameborder="0" 
                allow="autoplay; encrypted-media" 
                allowfullscreen
                style="width:100%; height:200px;">
        </iframe>
        </div>
    """
with c1:
    with st.form(key='seg'): 
        st.markdown(video_html("https://www.youtube.com/embed/56XRnIvUzvI?autoplay=1&mute=1&loop=1&playlist=56XRnIvUzvI"), unsafe_allow_html=True)
        st.markdown('<p style="text-align: center">Flag news Articles</p>', unsafe_allow_html=True)
        if st.form_submit_button('Test Authenticity of News ▶', use_container_width=True):
            switch_page('fakenews')

with c2:
    with st.form(key="adj"): 
        st.markdown(video_html("https://www.youtube.com/embed/BceXMkwlXPs?autoplay=1&mute=1&loop=1&playlist=BceXMkwlXPs"), unsafe_allow_html=True)
        st.markdown('<p style="text-align: center">Segregate DeepFakes</p>', unsafe_allow_html=True)
        if st.form_submit_button('Authenticate DeepFake ▶', use_container_width=True):
            switch_page('deepfake')

with c3:
    with st.form(key="partial"): 
        st.markdown(video_html("https://www.youtube.com/embed/UpSsVStfbmM?autoplay=1&mute=1&loop=1&playlist=UpSsVStfbmM"), unsafe_allow_html=True)
        st.markdown('<p style="text-align: center">See more features</p>', unsafe_allow_html=True)
        if st.form_submit_button('Explore More ▶', use_container_width=True):
            pass

with c4:
    with st.form(key="loc"): 
        st.markdown(video_html("https://www.youtube.com/embed/766uYY-6E1g?autoplay=1&mute=1&loop=1&playlist=766uYY-6E1g"), unsafe_allow_html=True)
        st.markdown('<p style="text-align: center">Log Location of users</p>', unsafe_allow_html=True)
        if st.form_submit_button('Track Suspicious users ▶', use_container_width=True):
            switch_page('track')
         

# Page styling
st.markdown(
    """
    <style>
[data-testid="stForm"] {
    background-color: rgba(86, 84, 80, 0.3);
    border: 2px solid rgb(57, 255, 212);
}
.stButton button {
    border: 2px solid white;
    transition: all 0.2s ease;
}

.stButton button:hover {
    border: 2px solid rgb(57, 255, 212);
    color: rgb(57, 255, 212);
    transform: scale(1.05);
    border-bottom: 4px solid rgb(57, 255, 212);
    border-left: 4px solid rgb(57, 255, 212);
}
.stButton button:active {
    background-color: black;
}
@keyframes borderMove {
    0% {
        border-image: linear-gradient(0deg, #00ef9f,#08fd14, #5ffaff, rgb(203, 145, 255)) 1;
    }

    50% {
        border-image: linear-gradient(180deg, #00ef9f, #08fd14,#5ffaff,rgb(203, 145, 255)) 1;
    }

    100% {
        border-image: linear-gradient(360deg, #00ef9f, #08fd14, #5ffaff,rgb(203, 145, 255)) 1;
    }
}

[data-testid="stForm"] {
    border: 2px solid;
    border-image-slice: 1;
    border-image: linear-gradient(90deg, #00ef9f,#08fd14, #5ffaff,rgb(203, 145, 255)) 1;
    animation: borderMove 5s linear infinite;
    border: 2px solid rgb(57, 255, 212);
    box-shadow: 0px 0px 10px 4px rgba(57, 255, 212, 0.6);
}
    </style>
    """,
    unsafe_allow_html=True
)
