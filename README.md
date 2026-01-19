# Convolve4.0-GenAI-Track
Intelligent Document AI for Field Extraction (IDFC FIRST Bank Track)
1. Project Overview
This repository contains an end-to-end Generative AI solution designed to extract structured information from diverse tractor loan invoices and quotations. The system is built to handle:

Multilingual Documents: English, Hindi, and Gujarati.

Complex Layouts: Scanned PDFs, handwritten text, and varied document structures.

Visual Markers: Automated detection of Dealer Signatures and Stamps.

2. Proposed Architecture
We utilize a Hybrid Vision-Language Pipeline to ensure high accuracy (≥95% DLA) while maintaining low inference costs.

Pipeline Workflow:
Pre-processing: PDF conversion to high-resolution images using pdf2image.

Visual Marker Detection (YOLOv8): A dedicated Object Detection model identifies the bounding boxes for Signature and Stamp.

Multilingual OCR (PaddleOCR): We use PaddleOCR's multilingual model to extract text from vernacular regions (Hindi/Gujarati). It performs superiorly on handwritten and low-quality scans.

Field Extraction Logic:

Dealer Name: Extracted using OCR and verified via Fuzzy Matching (Levenshtein Distance) against a master list.

Model & HP: Identified through Regex patterns and exact string matching.

Asset Cost: Cleaned using numeric parsing to remove currency symbols and commas.

Post-processing: Confidence scoring and JSON formatting.

3. Key Features
Language Agnostic: Built-in support for regional Indian languages.

Cost Optimized: Unlike heavy LLM APIs (GPT-4), our local SLM/OCR approach keeps the cost under $0.002 per document.

High Precision: Uses RapidFuzz for dealer name validation to handle minor OCR misspellings.

4. Performance & Cost Analysis
Document Level Accuracy (DLA): Targetting ≥95%.

Average Latency: ~3.5 seconds per page.

Estimated Inference Cost:

Local GPU/CPU: $0.00 (No API costs).

Cloud Scaled: ~$0.002 per document (Computation only).

5. Repository Structure
Plaintext

├── executable.py          # Main entry point for extraction
├── requirements.txt       # Dependencies (PaddleOCR, Ultralytics, etc.)
├── README.md              # Project documentation
├── weights/               # Trained YOLO weights for Signature/Stamp
├── utils/                 # Helper scripts for OCR and Cleanup
└── sample_output/         # Sample result.json
6. Installation & Usage
Clone the repo:

Bash

git clone https://github.com/[jamuna9495]/IDFC-GenAI-Solution.git
Install Dependencies:

Bash

pip install -r requirements.txt
Run Extraction:

Bash

python executable.py --input ./test_docs --output ./result.json
7. Team Details
Track: Generative AI – IDFC FIRST Bank (Convolve 4.0)

Team Members: [jamuna.k ]

Institutes: [SSM institute of engineering and technology college,Dindigul,Tamil nadu]
