# MCQ Generator using Generative AI (Langchain)

## Overview

This project is a MCQ (Multiple Choice Questions) Generator that utilizes Generative AI, specifically Langchain, to generate multiple-choice questions based on the content provided in the form of PDF or text documents. The generator extracts relevant information from the PDF content and generates MCQs according to the user given difficulty level .

Also deployed this application on the AWS EC2 instance (t2.small with 20 GB Memory)

## Features

- **PDF Parsing**: The generator can parse PDF documents to extract text content.
- **Generative AI (Langchain)**: Uses Langchain, a Generative AI model, to generate multiple-choice questions based on the extracted content.
- **Customization**: Allows users to specify the number of MCQs to generate and set the difficulty level .

## Usage

1. **Input File**: Provide the PDF or text document containing the content from which MCQs need to be generated.

2. **Specify Parameters**: Specify the number of MCQs to generate, difficulty level and the subject.

3. **Generate MCQs**: Run the generator, which will parse the PDF, analyze the content, and generate MCQs using Generative AI.


## Setup

1. **Clone the Repository**: Clone this repository to your local machine.

2. **Install Dependencies**: Install the required Python dependencies using
   ```bash
   pip install -r requirements.txt
   ```

3. **Run StreamlitApp**: Run the sreamlit app which contains frontend
   ```bash
   streamlit run StreamlitApp.py
   ```  

## Contributing

Contributions are welcome! If you have any suggestions, feature requests, or bug reports, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
