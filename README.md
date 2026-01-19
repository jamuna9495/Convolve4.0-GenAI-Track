# Convolve4.0-GenAI-Track

🚜 Intelligent Document AI for Field Extraction (IDFC FIRST Bank Track)📌 Project OverviewThis project is an end-to-end Generative AI solution built for Convolve 4.0. It automates the extraction of critical data from tractor loan quotations and invoices, supporting multiple languages (English, Hindi, Gujarati) and complex semi-structured layouts. 1111+2🛠️ Tech Stack & ArchitectureWe have designed a Low-Cost, High-Accuracy Pipeline using a hybrid Vision-Language approach:OCR Layer: PaddleOCR (Superior multilingual support for vernacular scripts like Hindi and Gujarati). 2222+2Vision Layer: YOLOv8 (For precise detection of Signatures and Stamps). 3333+1Logic Layer: RapidFuzz & Regex (For data validation, fuzzy matching, and numeric cleaning). 4444+2🔄 Workflow Pipeline:Ingestion: PDF to high-resolution image conversion using pdf2image. 5Detection: YOLOv8 identifies bounding boxes for Signatures and Stamps. 6666+1Extraction: Multilingual OCR extracts raw text from digital and handwritten regions. 7777+1Reasoning: Fuzzy matching ensures Dealer names match the master file with $\ge 90\%$ accuracy. 8888+1📊 Performance MetricsDocument Level Accuracy (DLA): Target $\ge 95\%$ 🎯 9999+1Processing Time: $< 30$ seconds per document ⚡ 10Inference Cost: $< \$0.01$ per document (CPU Optimized) 💰 11📁 Repository StructurePlaintext├── executable.py          # 🚀 Main entry point for extraction
├── requirements.txt       # 📦 Project dependencies
├── README.md              # 📖 Documentation
├── weights/               # 🧠 Trained YOLO model weights (.pt files)
├── utils/                 # 🔧 Helper modules (OCR helpers, validators)
└── sample_output/         # 📄 sample result.json
12📝 Output Format (JSON)The system outputs a structured JSON for every document including confidence scores and latency:
JSON{
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
13🚀 Installation & UsageClone the Repo:Bashgit clone https://github.com/jamuna9495/Convolve4.0-GenAI-Track.git
Install Requirements:Bashpip install -r requirements.txt
Run Extraction:Bashpython executable.py
👥 Team DetailsEvent: Convolve 4.0 - Generative AI TrackOrganization: IIT Guwahati & IDFC FIRST Bank 14Members: [jamuna.k]⭐ Built for accuracy, efficiency, and scale.
