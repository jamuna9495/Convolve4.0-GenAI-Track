# Convolve4.0-GenAI-Track
🚜 Intelligent Document AI for Field Extraction (IDFC FIRST Bank Track)
📌 Project Overview
This project is an end-to-end Generative AI solution built for Convolve 4.0. It automates the extraction of critical data from tractor loan quotations and invoices, supporting multiple languages and complex layouts. 

🛠️ Tech Stack & Architecture
We have designed a Low-Cost, High-Accuracy Pipeline using:


OCR Layer: PaddleOCR (Superior support for Hindi, Gujarati, and English) 
+2


Vision Layer: YOLOv8 (For precise Signature and Stamp detection) 


Logic Layer: RapidFuzz & Regex (For data validation and cleaning) 
+2

🔄 Workflow:

Ingestion: Converts PDF to high-res images. 


Detection: YOLO identifies Signatures and Stamps. 


Extraction: OCR reads vernacular and English text. 
+1


Reasoning: Fuzzy matching ensures Dealer names match the master file (≥90%). 
+1

📊 Performance Metrics

Document Level Accuracy (DLA): Target ≥95% 🎯 


Processing Time: < 30 seconds per document ⚡ 


Inference Cost: < $0.01 per document (Budget Friendly!) 💰 

📁 Repository Structure
Plaintext

├── executable.py          # 🚀 Main entry point for extraction
├── requirements.txt       # 📦 Project dependencies
├── README.md              # 📖 Documentation (You are here!)
├── weights/               # 🧠 Trained YOLO model weights
├── utils/                 # 🔧 Helper scripts (OCR, cleanup)
└── sample_output/         # 📄 sample result.json
📝 Output Format (JSON)
The system outputs a structured JSON for every document:

JSON

{
  "doc_id": "invoice_001",
  "fields": {
    "dealer_name": "ABC Tractors Pvt Ltd",
    "model_name": "Mahindra 575 DI",
    "horse_power": 50,
    "asset_cost": 525000,
    "signature": {"present": true, "bbox": [100, 200, 300, 250]},
    "stamp": {"present": true, "bbox": [400, 500, 500, 550]}
  },
  "confidence": 0.96,
  "processing_time_sec": 3.8,
  "cost_estimate_usd": 0.002
}


🚀 Installation & Usage
Clone the Repo:

Bash

git clone https://github.com/jamuna9495/idfc-genai-track.git
Install Requirements:

Bash

pip install -r requirements.txt
Run Extraction:

Bash

python executable.py
👥 Team Details
Event: Convolve 4.0 - Generative AI Track

Team: [sunshine]

Members: jamuna.k

⭐ Built with passion for IDFC FIRST Bank & IIT Guwahati.
