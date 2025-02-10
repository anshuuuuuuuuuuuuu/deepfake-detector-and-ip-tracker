Here’s a **README** for your **Unmasked** project:

---

# **Unmasked**

**Unmasked** is an integrated solution for detecting deepfakes, fake news, and tracking IP addresses. It combines state-of-the-art machine learning models with a secure tunneling system to provide a reliable and user-friendly toolset. The project’s frontend is built using **Streamlit**, offering an intuitive 3D interface for users to interact with all features.

---

## **Features**

### **1. Deepfake Detection**
- A **Deepfake Detection System** built using **LSTM** and **GRU** models to identify manipulated media.
- Detects images and videos that have been altered or created using deep learning techniques.
- Uses a trained model to analyze visual patterns and detect inconsistencies associated with deepfakes.

### **2. Fake News Detection**
- A **Fake News Detection System** powered by a **web scraper** that collects news and compares it to credible sources.
- **DeepSeek** and **Serper** are utilized to verify news accuracy by comparing them to trusted platforms and returning **credible sources**.
- If the news is real, credible sources are provided as references for validation.

### **3. IP Tracker**
- **IP Tracking System** creates secure tunnel links using **ngrok** and then converts them into tracking links.
- Uses **Ipify** to extract IP addresses from the tunnel for precise tracking.
- Ideal for safely monitoring web traffic while ensuring data privacy and security.

### **4. Frontend Interface**
- The **Streamlit** frontend is **3D**-based for a more engaging user experience.
- The user interface allows easy interaction with all systems (deepfake detection, fake news verification, and IP tracking).
- All systems can be accessed directly through the interactive, visually appealing Streamlit dashboard.

---


## **Usage**

- **Deepfake Detection:** Upload a media file (image or video) and the system will analyze it to check if it’s a deepfake.
- **Fake News Detection:** Paste a URL or scrape news content directly, and the system will verify its validity.
- **IP Tracker:** Use the system to create secure tunnel links with ngrok, and it will provide IP tracking links for monitoring.

---

## **Technologies Used**

- **Deepfake Detection:** LSTM and GRU models (built using TensorFlow/Keras)
- **Fake News Detection:** Web scraping tools and DeepSeek/Serper API integration
- **IP Tracker:** ngrok for secure tunneling, ipify for IP tracking
- **Frontend:** Streamlit (with 3D user interface)
  
---

## **Contributing**

Contributions are welcome! Feel free to fork the repo and submit pull requests with improvements or fixes.

---


Let me know if you'd like any changes or additions! 😊
