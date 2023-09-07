# Api_toxicity

Api_toxicity is a Flask-based application that offers multi-label image and text classification capabilities. The application can detect toxic sentences in text and classify explicit and unpleasant images.

## Table of Contents

- [Features](#features)
- [Repository Structure](#repository-structure)
- [Endpoints](#endpoints)
- [Screenshots](#screenshots)
- [Installation and Setup](#installation-and-setup)
- [Usage](#usage)
- [Dependencies](#dependencies)
- [Contributing](#contributing)
- [License](#license)

## Features:
- **Text Classification**: Detects toxic sentences.
- **Image Classification**: Classifies images into categories like drugs, normal, pornographic, and unpleasant visuals.
- **Flask API**: Provides endpoints to check toxicity in text and images.

## Repository Structure:
- `api.py`: Flask API that provides endpoints for checking toxicity in text and images.
- `image_classif.py`: Contains the image classification model built using ResNet50.
- `testing_model.py`: Script to test the model's performance.
- `trp_sample.py`: Sample script to test the text classification model.
- `Toxicity.h5`: Pre-trained model for text classification.
- `image_classificationD32.h5` & `image_classificationDR32.h5`: Pre-trained models for image classification.
- `tokenizer.pickle`: Tokenizer used for text preprocessing.
- `requirements.txt`: List of required packages to run the project.

## Endpoints:
- `/`: Main endpoint that renders the main HTML page.
- `/toxicity_check`: Endpoint to check the toxicity of a given text.
- `/toxicity_image_text`: Endpoint to check toxicity in both text and images.

## Screenshots

### Text classification sample
![Text Classification Sample](https://github.com/Gourav2000/Api_toxicity/blob/master/text_classif_proof_Trim.gif)

### Image classification sample
![Image Classification Sample](https://github.com/Gourav2000/Api_toxicity/blob/master/image_classif_proof.gif)

## Installation and Setup

1. Clone the repository:
```
git clone https://github.com/Gourav2000/Api_toxicity.git
```

2. Navigate to the project directory:
```
cd Api_toxicity
```

3. Install the required dependencies:
```
pip install -r requirements.txt
```

4. Run the app:
```
python api.py
```

## Usage

- To check for toxicity in text, use the `/toxicity_check` endpoint with the `text` parameter.
- To classify images and text for toxicity, use the `/toxicity_image_text` endpoint with the `toxic_image` and `tox_text` parameters.

## Dependencies

The application relies on several libraries and frameworks, including Flask, TensorFlow, Keras, and PIL. For a complete list, refer to the `requirements.txt` file.

## Contributing

Contributions are welcome! Feel free to fork the repository, make changes, and submit pull requests.

## License

Please refer to the `LICENSE` file in the repository for licensing information.

