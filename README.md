# Mildew Detection in Cherry Leaves

This project applies data science and machine learning to distinguish between healthy and diseased cherry leaves. Users can upload images through a Streamlit dashboard to predict leaf health. Alongside the model, the project includes insights from traditional data analysis, hypothesis evaluation, and model performance assessment.

To keep things organized and efficient, the project is structured around three Jupyter notebooks: one for data import and cleaning, one for data visualization, and another for developing and evaluating a TensorFlow deep learning model. This setup ensures a smooth workflow from data processing to model deployment.

The goal is to help an agri-food business tackle a powdery mildew infestation in its cherry tree plantations. Right now, trees are inspected manually—a slow and labor-intensive process. By automating detection through machine learning, this solution can save time and improve accuracy, making it easier to identify and treat infected trees quickly.

The project is hosted on the streamlit app and a live version may be found [here](https://milestone-project-mildew-detection-in-0b9a.onrender.com)

## Dataset Content

- The dataset is sourced from [Kaggle](https://www.kaggle.com/codeinstitute/cherry-leaves). We then created a fictitious user story where predictive analytics can be applied in a real project in the workplace.
- The dataset contains +4 thousand images taken from the client's crop fields. The images show healthy cherry leaves and cherry leaves that have powdery mildew, a fungal disease that affects many plant species. The cherry plantation crop is one of the finest products in their portfolio, and the company is concerned about supplying the market with a compromised quality product.

## Business Requirements

The cherry plantation crop from Farmy & Foods is facing a challenge where their cherry plantations have been presenting powdery mildew. Currently, the process is manual verification if a given cherry tree contains powdery mildew. An employee spends around 30 minutes in each tree, taking a few samples of tree leaves and verifying visually if the leaf tree is healthy or has powdery mildew. If there is powdery mildew, the employee applies a specific compound to kill the fungus. The time spent applying this compound is 1 minute. The company has thousands of cherry trees located on multiple farms across the country. As a result, this manual process is not scalable due to the time spent in the manual process inspection.

To save time in this process, the IT team suggested an ML system that detects instantly, using a leaf tree image, if it is healthy or has powdery mildew. A similar manual process is in place for other crops for detecting pests, and if this initiative is successful, there is a realistic chance to replicate this project for all other crops. The dataset is a collection of cherry leaf images provided by Farmy & Foods, taken from their crops.

- 1 - The client is interested in conducting a study to visually differentiate a healthy cherry leaf from one with powdery mildew.
- 2 - The client is interested in predicting if a cherry leaf is healthy or contains powdery mildew.

## Hypothesis and Validation Approach

### Hypothesis

Infected cherry leaves can be visually identified due to a distinct powdery white layer on their surface.

### Validation Steps

1. **Data Collection**  
   - Gather an image dataset of healthy and infected leaves from the client.  

1. **Visual Inspection**  
   - Create an image montage to compare healthy and infected leaves, highlighting key differences.  

1. **Testing with Image Analysis**  
   - Perform an average image analysis to identify consistent patterns or visual features that distinguish infected leaves from healthy ones.

## The rationale to map the business requirements to the Data Visualisations and ML tasks

### Business Requirement 1

The study should include analysis on:  

- **Average and variability images** for each class (healthy or powdery mildew).  
- **Differences between average healthy and average powdery mildew cherry leaves** to highlight distinguishing features.  
- **An image montage** for each class to provide a visual reference.  

### Business Requirement 2

- The ML system should **predict whether a cherry leaf is healthy or infected with powdery mildew**.  
- The dashboard should include:  
  - **An image montage feature** for visual comparison.  
  - **A prediction feature** that allows users to upload an image and receive a classification result.  

## ML Business Case

- In the previous bullet, you potentially visualised an ML task to answer a business requirement. You should frame the business case using the method we covered in the course.

## Dashboard Design

- List all dashboard pages and their content, either blocks of information or widgets, like buttons, checkboxes, images, or any other items, that your dashboard library supports.
- Finally, during the project development, you may revisit your dashboard plan to update a given feature (for example, at the beginning of the project, you were confident you would use a given plot to display an insight, but later, you chose another plot type).

## Unfixed Bugs

None

## Deployment

1. Log in to Render.com using Github.
1. Click on the New button, select Web Service.
1. At Source Code, select Git Providor. Select your repository name. Click Connect.
1. Enter a unique name for your web service.
1. Select the Python3 language.
1. Select the main branch.
1. Select the Frankfurt (EU Central) Region.
1. Set the Build Command: `pip install -r requirements.txt && ./setup.sh`
1. Set the Start Command: `streamlit run app.py`
1. Set Instance Type: Free
1. Set the Environment Variables: `Key: PORT` `Value: 8501` and `Key: PYTHON_VERSION` `Value: 3.12.1`
1. Click Deploy Web Service

## Main Data Analysis and Machine Learning Libraries

- [NumPy](https://numpy.org/) - Used to convert information to arrays
- [Pandas](https://pandas.pydata.org/) - Used to convert numerical data into dataframes
- [Matplotlib](https://matplotlib.org/) - Used to plot images such as augmented images and data images
- [Seaborn](https://seaborn.pydata.org/) - Used to plot image datasets, especially with multiple axes and more features
- [Plotly](https://plotly.com/python/) - Used for plotting results of ML model training
- [Joblib](https://joblib.readthedocs.io/) - Used for runnning tasks in parallel
- [TensorFlow](https://www.tensorflow.org/) - Machine learning library used to build the model
- [Keras Tuner](https://keras.io/) - Tuning of hyperparameters to find the best combination for model accuracy

### Other technologies used

- [Streamlit](https://streamlit.io/) - Library for building interactive multi-page dashboard
- [Render](https://render.com/) - Deployment of the dashboard as a web application
- [Git/GitHub](https://github.com/) - Version control and storing the source code
- [VSCode](https://code.visualstudio.com/) - IDE for local development

## Credits

- In this section, you need to reference where you got your content, media and from where you got extra help. It is common practice to use code from other repositories and tutorials. However, it is necessary to be very specific about these sources to avoid plagiarism.
- You can break the credits section up into Content and Media, depending on what you have included in your project.

### Content

- The text for the Home page was taken from Wikipedia Article A.
- Instructions on how to implement form validation on the Sign-Up page were taken from [Specific YouTube Tutorial](https://www.youtube.com/).
- The icons in the footer were taken from [Font Awesome](https://fontawesome.com/).

### Media

- The photos used on the home and sign-up page are from This Open-Source site.
- The images used for the gallery page were taken from this other open-source site.

## Acknowledgements (optional)

- Thank the people who provided support throughout this project.
