# ML Prediction App
This project showcases a webapp developed using streamlit to test and see visual outputs for machine learning models trained on different datasets.

## Description
This project includes 2 models for now to play around with:

1. Predict Diabetes Likelihood for Women
2. Predict California (CA) house prices

## Getting Started
### Operating System
- MacOS
- Windows
- Linux

### How to run
1. To run this project, first run all cells in the jupyter notebook files to save the model locally:
    - CA House Price Prediction/CA_house_model.ipynb
    - Diabetes Prediction/diabetes_model.ipynb
2. Once the model artifacts are saved, run the following command to run the web application.
    ```
    python main.py
    ```

## Project Setup
### Prerequisites
- Anaconda installed on the system
    - If not installed on system, install from [here](https://www.anaconda.com/download)
- Git installed on the system
    - If not installed on system, use [this](https://github.com/git-guides/install-git) resource
- Github account
    - If no account exists, create one using [this](https://docs.github.com/en/get-started/start-your-journey/creating-an-account-on-github)

### Environment Setup
1. Create a new conda virtual environment to store all project dependencies
```
conda create -p ./venv python=3.11.5
```

This command creates a new virtual environement in the current project directory that is open.

2. Activate the environment
```
conda activate .venv_SIGN/
```

### Dependencies/Package
run the following command only once after activating the virtual environment to install all the packages needed to recreate/run this project.
```
pip install -r requirements.txt
```

### Github Workflow
1. Clone the repository to a dedicated folder:
```
git clone https://github.com/Ansh0210/Prediction-App.git
```

2. Create a new branch for your work:
```
git checkout -b your-branch-name
```

Choose a descriptive name for your branch (could be your name)

3. Verify that you're on correct branch
```
git branch
```
This command lists out all the branches, with an asterisk **(*)** next to the current branch

4. Make changes and commit them:
```
git add .
git commit -m "Descriptive commit message"
```

5. Push your branch to Github
```
git push origin your-branch-name
```

6. Go to GitHub repo and click on "Pull request"

7. Click "New Pull Request"

8. Select your branch from the dropdown menu and click "Create pull request"

9. Add a title and description for your pull request, explaining the changes you've made

10. Click "Create pull request" to submit it for review

11. Wait for the project maintainers to review your changes. They may request modifications or approve and merge your changes into the main branch.

**Remember to always pull in the latest changes from the main branch before starting new work**
```
git checkout main
git pull origin main
git checkout -b your-branch-name
```

### Branch Protection and Merging Rules
This project will require at least one review before merging changes into the main branch. This will help maintain the code base and encourage collabaration between people

1. When creating pull request, it can't be merged until at least one other contributor reviews and approves the changes

2. The reviewer(s) will examine the code, may comment on it, and may request changes.

3. Once pull request has been approved, you can merge it into the main branch

## Author
- [Shivansh Shukla](https://github.com/Ansh0210)