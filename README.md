# Api_toxicity

Api_toxicity is a Flask-based application that offers multi-label image and text classification capabilities. The application can detect toxic sentences in text and classify explicit and unpleasant images.

## Table of Contents

- [Features](#features)
- [Screenshots](#screenshots)
- [Installation and Setup](#installation-and-setup)
- [Usage](#usage)
- [Dependencies](#dependencies)
- [Contributing](#contributing)
- [License](#license)

## Features

1. **Text Classification**: Detects toxic sentences in the provided text.
2. **Image Classification**: Classifies images into categories such as drugs, normal, pornographic, and unpleasant visuals.
3. **API Endpoints**: Provides endpoints for checking toxicity in text and classifying images.

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

