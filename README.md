# Machine Learning Mastery --- Zero to Advanced

> A structured, hands-on learning journey from absolute beginner to
> building, evaluating, deploying, and explaining machine-learning
> systems.

**Repository:** `machine-learning-mastery`\
**Description:** A complete zero-to-advanced Machine Learning learning
journey covering Python programming, Mathematics, Statistics, Data
Analysis, Machine Learning, Deep Learning, Artificial Intelligence,
hands-on projects, daily practice, and practical implementations.

------------------------------------------------------------------------

## 1. Mission and learning principles

The goal is not to finish videos quickly. The goal is to understand
concepts, implement them yourself, explain why they work, and use them
to solve real problems.

Follow this learning loop for every topic:

1.  **Learn:** Read or watch one focused lesson.
2.  **Understand:** Write the idea in your own words.
3.  **Implement:** Code the concept without blindly copying.
4.  **Practise:** Solve small exercises.
5.  **Explain:** Write what you learned and what confused you.
6.  **Commit:** Push your work to GitHub.
7.  **Review:** Revisit difficult concepts after a few days.

Do not move forward just because a video is complete. Move forward when
you can explain the topic and solve a few problems independently.

### Suggested weekly routine

A realistic starting target is 8--12 focused hours per week. Increase
only when it fits your school, rest, and other responsibilities.

  Activity                 Suggested time
  ---------------------- ----------------
  Learn a concept              30--45 min
  Code/practise                30--45 min
  Mathematics practice         20--30 min
  Notes and revision           10--15 min
  GitHub update                 5--10 min

Consistency matters more than long study sessions. Keep one lighter
review day each week.

------------------------------------------------------------------------

## 2. Complete roadmap at a glance

  -----------------------------------------------------------------------
  Phase                   Main focus              Exit goal
  ----------------------- ----------------------- -----------------------
  0                       Computer and learning   Comfortable using
                          setup                   files, terminal, editor
                                                  and Git

  1                       Python fundamentals     Write small programs
                                                  independently

  2                       Intermediate Python     Organize code into
                                                  functions, modules and
                                                  projects

  3                       Mathematics foundations Understand the maths
                                                  used by common ML
                                                  methods

  4                       Statistics and          Describe data,
                          probability             uncertainty and
                                                  distributions

  5                       Data tools              Work with NumPy, pandas
                                                  and visualizations

  6                       Data analysis           Clean, explore and
                                                  explain a dataset

  7                       Core machine learning   Train and evaluate
                                                  baseline ML models

  8                       Better ML practice      Improve models without
                                                  data leakage or
                                                  misleading metrics

  9                       Advanced ML             Understand ensembles,
                                                  tuning and specialized
                                                  methods

  10                      Deep learning           Build and train neural
                                                  networks

  11                      Specializations         Explore NLP, computer
                                                  vision, time series and
                                                  recommender systems

  12                      Production and          Package, deploy,
                          portfolio               monitor and explain
                                                  projects
  -----------------------------------------------------------------------

This is a mastery path, not a deadline. Some phases may take several
weeks or months.

------------------------------------------------------------------------

# PHASE 0 --- Computer and developer foundations

### Learn

-   What an operating system, file, folder, extension and path are.
-   How to install and update software safely.
-   Basic terminal/command-line navigation.
-   How Python runs a program.
-   What an editor/IDE is and how to run a script.
-   What Git and GitHub are; the difference between local and remote
    repositories.
-   Basic Markdown for documentation.

### Tools to set up

-   Python 3 (current stable version).
-   VS Code or another Python editor.
-   Git.
-   A GitHub account.
-   JupyterLab or Jupyter notebooks (later, for exploration).

### Practise

-   Create folders and files from the terminal.
-   Run a simple Python file.
-   Create a Git repository, make a commit and push it to GitHub.
-   Write a short README.

**Exit checkpoint:** You can create a project folder, run a Python file,
use basic terminal commands and push a commit to GitHub.

------------------------------------------------------------------------

# PHASE 1 --- Python programming from zero

Do not skip this phase. Python is the main language used throughout this
roadmap.

## 1. Getting started

-   What Python is and where it is used.
-   Installing Python and checking the version.
-   Running Python in the terminal, editor and notebook.
-   Comments, indentation and syntax.
-   Errors: syntax errors, runtime errors and logical errors.

## 2. Variables and data types

-   Variables and naming rules.
-   Integers, floats, strings and booleans.
-   `None`.
-   Type conversion and checking types.
-   Input and output with `input()` and `print()`.
-   Operators: arithmetic, comparison, assignment and logical.

## 3. Strings

-   Indexing and slicing.
-   String methods.
-   Formatting with f-strings.
-   Searching, replacing, splitting and joining.
-   Escape characters.

## 4. Collections

-   Lists: indexing, slicing, methods and nested lists.
-   Tuples and immutability.
-   Sets and set operations.
-   Dictionaries: keys, values, items and updates.
-   Choosing the correct collection.

## 5. Conditions and loops

-   `if`, `elif`, `else`.
-   `for` and `while`.
-   `range()`.
-   `break`, `continue` and `pass`.
-   Nested loops.
-   Looping through strings, lists and dictionaries.

## 6. Functions

-   Defining and calling functions.
-   Parameters, arguments and return values.
-   Default and keyword arguments.
-   Scope and local/global variables.
-   Lambda functions (basic understanding).
-   Docstrings and readable function names.

## 7. Useful Python concepts

-   List, dictionary and set comprehensions.
-   Unpacking.
-   `enumerate()` and `zip()`.
-   Sorting with `sorted()` and `key`.
-   Iterables and iterators (introductory understanding).
-   Generators (introductory understanding).

## 8. Files and errors

-   Reading and writing text files.
-   Working with CSV and JSON.
-   `with` statements.
-   Exceptions: `try`, `except`, `else`, `finally`.
-   Raising useful errors.

## 9. Object-oriented programming

-   Classes and objects.
-   Attributes and methods.
-   `__init__`.
-   Instance vs class attributes.
-   Inheritance and composition.
-   Encapsulation and polymorphism (basic practical understanding).

## 10. Professional Python habits

-   Modules and imports.
-   Virtual environments.
-   Installing packages with `pip`.
-   Project structure.
-   Debugging.
-   Basic testing with `assert` and `pytest`.
-   Type hints and formatting basics.

### Python practice projects

1.  Calculator.
2.  Number guessing game.
3.  Quiz application.
4.  To-do list stored in a file.
5.  Expense tracker using CSV.
6.  Contact book using dictionaries and JSON.
7.  A small object-oriented library-management program.

**Exit checkpoint:** You can solve beginner problems, write functions,
read files, handle errors and build a small multi-file Python project
without following a tutorial line by line.

------------------------------------------------------------------------

# PHASE 2 --- Intermediate Python and developer skills

### Topics

-   Clean code and separation of responsibilities.
-   Packages, imports and project structure.
-   Virtual environments and dependency files.
-   Debugging and logging.
-   Unit tests and test cases.
-   Working with APIs and JSON (useful for obtaining data).
-   Basic SQL: tables, rows, columns, `SELECT`, `WHERE`, `GROUP BY`,
    joins.
-   Git branches, meaningful commits and `.gitignore`.
-   Basic command-line arguments.
-   Introductory complexity: why some operations scale better than
    others.

### Practice project

Build a Python data collector that reads a public dataset or permitted
API, validates the data, stores it as CSV/JSON or in SQLite, and
produces a short report.

**Exit checkpoint:** You can create a reproducible Python project,
install its dependencies and test its main functions.

------------------------------------------------------------------------

# PHASE 3 --- Mathematics for Machine Learning

You do not need to become a mathematician before starting ML. Learn the
foundations carefully, then study deeper maths when an algorithm
requires it.

## A. Arithmetic and algebra

-   Positive and negative numbers.
-   Fractions, decimals, ratios and percentages.
-   Order of operations.
-   Powers, roots and scientific notation.
-   Variables and algebraic expressions.
-   Simplifying and rearranging equations.
-   Linear equations and simultaneous equations.
-   Inequalities.
-   Polynomials and factorization.
-   Coordinate plane and graphs.
-   Functions, domain, range and function notation.
-   Linear, quadratic, exponential and logarithmic functions.
-   Absolute value.

**Why it matters:** Equations describe model predictions, errors,
transformations and relationships between variables.

## B. Functions, graphs and logarithms

-   Slope and intercept.
-   Gradient of a straight line.
-   Function composition and inverse functions.
-   Exponential growth and decay.
-   Logarithm rules and change of base.
-   Reading and interpreting graphs.
-   Sigmoid, tanh and ReLU as function shapes.

**Why it matters:** Many ML models are functions; logarithms appear in
probability, loss functions and information theory.

## C. Linear algebra

Study in this order: 1. Scalars, vectors and matrices. 2. Vector
notation, dimensions and shapes. 3. Vector addition and scalar
multiplication. 4. Dot product. 5. Matrix addition and multiplication.
6. Transpose and identity matrix. 7. Systems of linear equations. 8.
Linear independence, span and basis. 9. Rank and inverse (conceptual and
practical). 10. Determinants (basic understanding). 11. Norms and
distances: L1, L2 and Euclidean distance. 12. Eigenvalues and
eigenvectors (intuition first). 13. Singular Value Decomposition (SVD)
and Principal Component Analysis (PCA) intuition.

**Why it matters:** Datasets are represented as matrices; model
parameters are vectors; neural networks rely heavily on matrix
operations.

## D. Calculus

1.  What a limit means.
2.  Continuity (basic intuition).
3.  Average and instantaneous rate of change.
4.  Derivatives and derivative notation.
5.  Derivatives of powers, sums, products and quotients.
6.  Chain rule.
7.  Partial derivatives.
8.  Gradients.
9.  Tangent lines and slope.
10. Minima and maxima.
11. Optimization intuition.
12. Integrals and area-under-curve intuition.
13. Multivariable functions.

**Why it matters:** Gradient descent uses derivatives to adjust model
parameters and reduce error. The chain rule is central to
backpropagation.

## E. Probability

-   Experiments, outcomes and sample spaces.
-   Events and probability rules.
-   Complementary events.
-   Conditional probability.
-   Independence and dependence.
-   Bayes' theorem.
-   Counting basics: permutations and combinations.
-   Random variables.
-   Discrete and continuous random variables.
-   Expected value and variance.
-   Common distributions: Bernoulli, binomial, uniform, normal and
    Poisson.

**Why it matters:** ML makes predictions under uncertainty and many
algorithms use probability.

## F. Statistics

-   Population and sample.
-   Sampling and sampling bias.
-   Mean, median and mode.
-   Range, variance and standard deviation.
-   Percentiles and quartiles.
-   Interquartile range and outliers.
-   Covariance and correlation.
-   Distribution shape, skewness and spread.
-   Normal distribution and standard scores (z-scores).
-   Central Limit Theorem (intuition).
-   Confidence intervals.
-   Hypothesis testing, null and alternative hypotheses.
-   p-values and statistical significance.
-   Type I and Type II errors.
-   Correlation vs causation.

**Why it matters:** Statistics helps you understand data, evaluate
evidence and avoid false conclusions.

## G. Optimization and information theory

-   Objective and loss functions.
-   Parameters and hyperparameters.
-   Convexity intuition.
-   Gradient descent.
-   Learning rate.
-   Local and global minima.
-   Entropy and information gain.
-   Cross-entropy.
-   KL divergence (conceptual understanding).

**Math exit checkpoint:** You can work with vectors and matrices,
interpret derivatives and gradients, calculate basic probabilities and
summary statistics, and explain how gradient descent updates parameters.

------------------------------------------------------------------------

# PHASE 4 --- Statistics and data reasoning in practice

Use Python to connect the maths to real datasets.

### Learn

-   Descriptive vs inferential statistics.
-   Sampling methods and bias.
-   Missing data and outliers.
-   Distribution plots and summary tables.
-   Correlation and its limitations.
-   Confidence intervals and hypothesis tests.
-   A/B testing concepts.
-   Probability distributions and simulation.
-   Choosing a statistic that matches a question.

### Practice

-   Generate random data and simulate probability experiments.
-   Compare two groups using summary statistics and plots.
-   Explain why correlation does not prove causation.
-   Write a short report with a conclusion and limitations.

**Exit checkpoint:** You can inspect a dataset and explain what its
statistics do---and do not---tell you.

------------------------------------------------------------------------

# PHASE 5 --- Python data science libraries

## NumPy

-   Arrays and dimensions.
-   `shape`, `ndim`, `dtype` and data types.
-   Indexing and slicing.
-   Reshaping and joining arrays.
-   Vectorization and broadcasting.
-   Aggregations and axis.
-   Random number generation.
-   Linear algebra basics.

## pandas

-   Series and DataFrames.
-   Reading CSV, Excel and JSON.
-   Inspecting data with `head`, `info` and `describe`.
-   Selecting, filtering and sorting.
-   Missing values and duplicates.
-   Type conversion.
-   Grouping and aggregation.
-   Merging, joining and concatenation.
-   Dates and times.
-   Exporting clean data.

## Visualization

-   Matplotlib fundamentals.
-   Seaborn for statistical plots.
-   Line, bar, histogram, scatter and box plots.
-   Labels, titles, legends and scales.
-   Choosing a chart that answers the question.

## Helpful tools to explore later

-   JupyterLab or notebooks.
-   SciPy.
-   Statsmodels.
-   scikit-learn.

**Projects** 1. Personal or public-data analysis with pandas. 2. Sales
dataset analysis. 3. Weather or transport trend visualization using a
permitted dataset.

**Exit checkpoint:** You can load, clean, transform, summarize and
visualize a dataset.

------------------------------------------------------------------------

# PHASE 6 --- Exploratory Data Analysis (EDA)

### Learn the workflow

1.  Understand the problem and target question.
2.  Identify rows, columns, units and data types.
3.  Inspect missing values and duplicates.
4.  Check invalid values and unusual ranges.
5.  Study numerical and categorical variables.
6.  Visualize distributions.
7.  Explore relationships between features.
8.  Check possible target leakage.
9.  Record assumptions and limitations.
10. Summarize findings.

### Data preparation concepts

-   Numerical and categorical features.
-   Encoding categories.
-   Scaling and normalization.
-   Standardization.
-   Imputation.
-   Outlier investigation.
-   Feature creation.
-   Train, validation and test split.
-   Data leakage and why preprocessing must be fitted only on training
    data.

**Project:** Choose a public dataset, perform EDA, clean it, create
visualizations and write a report explaining the findings.

------------------------------------------------------------------------

# PHASE 7 --- Core Machine Learning

## 1. Understand the ML workflow

-   What machine learning is and when it is useful.
-   AI vs ML vs deep learning.
-   Supervised, unsupervised and reinforcement learning.
-   Features, labels and examples.
-   Training, validation and test data.
-   Parameters vs hyperparameters.
-   Generalization.
-   Overfitting and underfitting.
-   Baseline models.

## 2. Supervised learning: regression

Learn: - Simple linear regression. - Multiple linear regression. -
Polynomial regression. - Regularization: Ridge and Lasso. - Decision
tree regression. - Random forest regression.

Understand: - Prediction equation. - Residuals. - Mean Absolute Error
(MAE). - Mean Squared Error (MSE). - Root Mean Squared Error (RMSE). -
R-squared and its limitations.

## 3. Supervised learning: classification

Learn: - Logistic regression. - k-Nearest Neighbors (k-NN). - Naive
Bayes. - Decision trees. - Random forests. - Support Vector Machines
(SVM). - Basic gradient boosting.

Understand: - Confusion matrix. - Accuracy, precision and recall. -
Specificity. - F1 score. - ROC curve and AUC. - Precision-recall
curve. - Class imbalance and threshold selection.

## 4. Unsupervised learning

-   k-means clustering.
-   Hierarchical clustering.
-   DBSCAN (conceptual and practical).
-   Principal Component Analysis (PCA).
-   Anomaly detection basics.

Understand: - Distance and similarity. - Scaling before distance-based
methods. - Choosing and interpreting clusters. - Limits of clustering
metrics.

## 5. Essential model workflow

-   Create a simple baseline.
-   Split data correctly.
-   Fit preprocessing on training data only.
-   Train a model.
-   Evaluate on validation data.
-   Compare models fairly.
-   Use a final test set only for final evaluation.
-   Explain model limitations.

**Projects** 1. House-price prediction (regression). 2.
Student-performance prediction using an appropriate, ethically handled
public dataset. 3. Spam-message classification with a permitted dataset.
4. Customer segmentation (clustering).

**Exit checkpoint:** You can choose a suitable baseline model, train it,
evaluate it with an appropriate metric and explain its limitations.

------------------------------------------------------------------------

# PHASE 8 --- Reliable and improved machine learning

### Topics

-   Cross-validation and stratified cross-validation.
-   Pipelines and `ColumnTransformer`.
-   Feature engineering and feature selection.
-   Hyperparameter tuning: grid and randomized search.
-   Regularization and bias-variance trade-off.
-   Imbalanced datasets and resampling concepts.
-   Calibration and decision thresholds.
-   Learning curves and validation curves.
-   Error analysis.
-   Permutation importance and model interpretation.
-   SHAP concepts (use carefully and understand limitations).
-   Reproducibility and random seeds.
-   Data leakage, target leakage and evaluation mistakes.
-   Fairness, privacy and responsible use.

**Exit checkpoint:** You can build a repeatable ML pipeline, tune it
using validation data and report honest test results.

------------------------------------------------------------------------

# PHASE 9 --- Advanced machine learning

Explore these after core ML is comfortable:

-   Gradient boosting: XGBoost, LightGBM and CatBoost.
-   Ensemble methods: bagging, boosting and stacking.
-   Advanced feature engineering.
-   Time-series fundamentals: trend, seasonality, lag features and
    time-based validation.
-   Recommendation systems: content-based and collaborative filtering.
-   Anomaly detection.
-   Probabilistic modelling basics.
-   Model interpretability and responsible AI.
-   Introductory reinforcement learning: agent, state, action, reward
    and policy.

Do not learn every algorithm just to collect names. For each method,
understand the problem it solves, its assumptions, strengths, weaknesses
and evaluation method.

**Projects** - A time-series forecasting experiment with chronological
evaluation. - A recommendation prototype using a public dataset. - A
comparison of several boosting models on one dataset.

------------------------------------------------------------------------

# PHASE 10 --- Deep Learning and neural networks

### Foundations

-   Perceptrons and artificial neurons.
-   Weights, biases and activations.
-   Forward propagation.
-   Loss functions.
-   Gradient descent and optimizers.
-   Backpropagation and chain rule.
-   Epochs, batches and iterations.
-   Learning rates.
-   Initialization.
-   Overfitting and regularization.
-   Dropout and batch normalization.
-   GPU basics.

### Framework

Start with **PyTorch** or TensorFlow/Keras. Pick one first; do not try
to master both simultaneously.

For a PyTorch path, learn: - Tensors and tensor shapes. - Datasets and
DataLoaders. - Building a model with `nn.Module`. - Loss functions and
optimizers. - Training and evaluation loops. - Saving and loading model
weights. - Using CPU/GPU safely.

### Neural network architectures

-   Feed-forward neural networks (MLP).
-   Convolutional Neural Networks (CNNs).
-   Recurrent Neural Networks (RNNs) at an introductory level.
-   LSTM and GRU concepts.
-   Attention mechanism.
-   Transformer architecture.

**Projects** 1. Handwritten-digit classification. 2. Image
classification on a permitted dataset. 3. Text sentiment classification.
4. Compare a small neural network with a traditional ML baseline.

**Exit checkpoint:** You can explain forward propagation and
backpropagation, train a small neural network, track validation
performance and save a trained model.

------------------------------------------------------------------------

# PHASE 11 --- Choose an AI specialization

You do not need to master every specialization. First build broad
foundations, then choose one or two areas based on your interests.

## Natural Language Processing (NLP)

-   Text cleaning and tokenization.
-   Vocabulary and embeddings.
-   Bag of Words and TF-IDF.
-   Sequence models (concepts).
-   Attention and transformers.
-   Using pretrained language models.
-   Text classification and information extraction.
-   Evaluation and limitations of language models.

## Computer vision

-   Image representation and preprocessing.
-   Convolution and pooling.
-   CNN architectures.
-   Transfer learning.
-   Object detection and image segmentation concepts.
-   Evaluation metrics for vision tasks.

## Generative AI and Large Language Models

-   What language models learn.
-   Tokens and embeddings.
-   Transformer overview.
-   Pretraining and fine-tuning concepts.
-   Prompt design and structured outputs.
-   Retrieval-Augmented Generation (RAG) concepts.
-   Vector search and embeddings.
-   Evaluation, hallucinations, privacy and safety.
-   Responsible use of model APIs.

## Time series

-   Trend, seasonality and noise.
-   Time-based splits.
-   Baselines and forecasting metrics.
-   Classical forecasting concepts.
-   ML-based forecasting.
-   Deep-learning approaches when justified.

## Reinforcement learning

-   Agent, environment, state, action and reward.
-   Policy and value function.
-   Exploration vs exploitation.
-   Q-learning concepts.
-   Evaluation in safe simulated environments.

------------------------------------------------------------------------

# PHASE 12 --- MLOps, deployment and production basics

A model is not a complete product just because it works in a notebook.

### Learn

-   Saving and loading models.
-   Building a simple prediction API with FastAPI.
-   Input validation and error handling.
-   Basic Docker concepts.
-   Environment and dependency management.
-   Experiment tracking.
-   Model and dataset versioning concepts.
-   Logging and monitoring.
-   Data drift and model drift.
-   Testing a model service.
-   Basic cloud deployment concepts.
-   Security, privacy and responsible data handling.

### Capstone project

Build an end-to-end application:

1.  Define a real, appropriately scoped problem.
2.  Find a permitted dataset and document its source.
3.  Explore and clean the data.
4.  Create a simple baseline.
5.  Train and evaluate multiple models.
6.  Select a model using validation results.
7.  Evaluate once on held-out test data.
8.  Save the model and preprocessing pipeline.
9.  Create a small API or application.
10. Write setup instructions, results, limitations and future
    improvements.

------------------------------------------------------------------------

# 3. Required mathematics checklist

Use this checklist to track your maths foundations.

## Algebra and functions

-   [ ] Fractions, ratios, percentages and powers
-   [ ] Equations and inequalities
-   [ ] Coordinate geometry and slope
-   [ ] Functions, graphs and composition
-   [ ] Exponential and logarithmic functions

## Linear algebra

-   [ ] Scalars, vectors and matrices
-   [ ] Vector operations and dot product
-   [ ] Matrix multiplication and transpose
-   [ ] Systems of linear equations
-   [ ] Norms, distances and rank
-   [ ] Eigenvalues and eigenvectors
-   [ ] PCA and SVD intuition

## Calculus

-   [ ] Limits and continuity
-   [ ] Derivatives and rules
-   [ ] Chain rule
-   [ ] Partial derivatives
-   [ ] Gradients
-   [ ] Minima, maxima and optimization
-   [ ] Integral intuition

## Probability

-   [ ] Events and probability rules
-   [ ] Conditional probability
-   [ ] Independence
-   [ ] Bayes' theorem
-   [ ] Random variables
-   [ ] Expected value and variance
-   [ ] Common probability distributions

## Statistics

-   [ ] Mean, median and mode
-   [ ] Variance and standard deviation
-   [ ] Percentiles and quartiles
-   [ ] Covariance and correlation
-   [ ] Sampling and bias
-   [ ] Confidence intervals
-   [ ] Hypothesis testing and p-values
-   [ ] Type I and Type II errors

## Optimization and information theory

-   [ ] Loss and objective functions
-   [ ] Gradient descent
-   [ ] Learning rate
-   [ ] Regularization
-   [ ] Entropy and information gain
-   [ ] Cross-entropy

------------------------------------------------------------------------

# 4. GitHub repository structure

Keep the repository organized as you progress. You can add folders when
a phase begins.

``` text
machine-learning-mastery/
│
├── README.md
├── 00-computer-foundations/
├── 01-python-basics/
│   ├── notes/
│   ├── exercises/
│   └── projects/
├── 02-intermediate-python/
├── 03-mathematics/
│   ├── algebra/
│   ├── linear-algebra/
│   ├── calculus/
│   ├── probability/
│   ├── statistics/
│   └── optimization/
├── 04-data-science-libraries/
│   ├── numpy/
│   ├── pandas/
│   └── visualization/
├── 05-data-analysis/
├── 06-core-machine-learning/
│   ├── regression/
│   ├── classification/
│   └── clustering/
├── 07-advanced-machine-learning/
├── 08-deep-learning/
├── 09-specializations/
│   ├── nlp/
│   ├── computer-vision/
│   └── generative-ai/
├── 10-mlops-deployment/
├── projects/
│   ├── beginner/
│   ├── intermediate/
│   └── capstone/
└── learning-log/
```

------------------------------------------------------------------------

# 5. Daily learning log template

Create one Markdown file per day inside `learning-log/`, for example
`day-001.md`.

``` markdown
# Day 001 — [Topic]

## What I learned
- Concept 1
- Concept 2

## Explanation in my own words
Write a simple explanation without copying the lesson.

## Code / practical work
Describe what you implemented and link the notebook or script.

## Questions I can now answer
1. Question one?
2. Question two?

## What I still find confusing
- Point to revise

## Practice completed
- [ ] Exercise 1
- [ ] Exercise 2
- [ ] Exercise 3

## Next session
- Topic to learn
```

### Commit message examples

``` text
Day 001: Set up Python environment
Day 002: Learn variables and data types
Day 003: Practise strings and operators
Phase 1: Complete Python fundamentals exercises
Math: Add vector operations notes and examples
Project: Build a CSV expense tracker
```

Commit meaningful work. Do not upload passwords, API keys, private
datasets or personal information. Use a `.gitignore` for virtual
environments, caches and local secrets.

------------------------------------------------------------------------

# 6. How to study each topic

For each topic, use this sequence:

1.  **Concept:** What is it?
2.  **Purpose:** Why do we need it?
3.  **Working:** How does it work?
4.  **Example:** Can I understand a simple example?
5.  **Implementation:** Can I code it myself?
6.  **Practice:** Can I solve a new problem?
7.  **Explanation:** Can I teach the idea in simple words?
8.  **Review:** Can I still do it after a few days?

### Topic completion rule

Mark a topic complete only when: - \[ \] I understand the main idea. -
\[ \] I can explain it in my own words. - \[ \] I have written and run
code myself where applicable. - \[ \] I have completed practice
questions. - \[ \] I have recorded mistakes and corrected them. - \[ \]
I have committed the work to GitHub.

------------------------------------------------------------------------

# 7. Recommended learning resources

Prefer official documentation and structured courses. Use one primary
resource at a time rather than collecting dozens of playlists.

### Python

-   Python tutorial: https://docs.python.org/3/tutorial/
-   Automate the Boring Stuff: https://automatetheboringstuff.com/
-   CS50 Python: https://cs50.harvard.edu/python/

### Mathematics

-   Khan Academy: https://www.khanacademy.org/
-   3Blue1Brown (visual intuition): https://www.3blue1brown.com/
-   Mathematics for Machine Learning book: https://mml-book.github.io/

### Data science

-   NumPy documentation: https://numpy.org/doc/
-   pandas getting started:
    https://pandas.pydata.org/docs/getting_started/
-   Matplotlib tutorials: https://matplotlib.org/stable/tutorials/

### Machine learning

-   Google Machine Learning Crash Course:
    https://developers.google.com/machine-learning/crash-course
-   scikit-learn user guide:
    https://scikit-learn.org/stable/user_guide.html
-   Kaggle Learn: https://www.kaggle.com/learn

### Deep learning and AI

-   PyTorch tutorials: https://pytorch.org/tutorials/
-   Dive into Deep Learning: https://d2l.ai/
-   Hugging Face course: https://huggingface.co/learn

Always check the current documentation for installation steps and API
changes.

------------------------------------------------------------------------

# 8. Your first 14 days --- start here

This is a gentle starting sequence. Spend more than one day on a topic
if needed.

  -----------------------------------------------------------------------
  Day                     Learning target         Practical task
  ----------------------- ----------------------- -----------------------
  1                       Install Python, editor  Run your first Python
                          and Git                 program

  2                       `print()`, comments and Print a personal
                          variables               learning profile using
                                                  sample data

  3                       Data types and type     Build a simple
                          conversion              unit-conversion
                                                  practice program

  4                       Arithmetic and          Create a calculator
                          comparison operators    

  5                       Strings and f-strings   Format a short report

  6                       Conditions              Build a simple
                                                  eligibility checker
                                                  with sample rules

  7                       Revision                Solve beginner
                                                  exercises without notes

  8                       Lists and tuples        Build a small list
                                                  manager

  9                       Dictionaries and sets   Create a contact-book
                                                  data structure

  10                      `for` and `while` loops Make a quiz with a
                                                  score

  11                      Functions               Refactor earlier
                                                  programs into functions

  12                      Files and JSON          Save and load a small
                                                  practice dataset

  13                      Exceptions and          Handle invalid input
                          debugging               gracefully

  14                      Review and mini-project Complete a command-line
                                                  quiz application
  -----------------------------------------------------------------------

After these 14 days, continue through the remaining Python topics. Do
not jump to ML algorithms yet.

------------------------------------------------------------------------

# 9. Progress tracker

Update this section as you complete each phase.

-   [ ] Phase 0 --- Computer and developer foundations
-   [ ] Phase 1 --- Python fundamentals
-   [ ] Phase 2 --- Intermediate Python
-   [ ] Phase 3 --- Mathematics
-   [ ] Phase 4 --- Statistics and probability
-   [ ] Phase 5 --- Data science libraries
-   [ ] Phase 6 --- Exploratory data analysis
-   [ ] Phase 7 --- Core machine learning
-   [ ] Phase 8 --- Reliable ML practice
-   [ ] Phase 9 --- Advanced machine learning
-   [ ] Phase 10 --- Deep learning
-   [ ] Phase 11 --- AI specialization
-   [ ] Phase 12 --- MLOps and deployment
-   [ ] Capstone --- End-to-end ML project

------------------------------------------------------------------------

# 10. Final advice

-   Start with Python. Do not begin with advanced ML algorithms.
-   Study mathematics alongside programming once Python basics are
    comfortable.
-   Practise more than you watch.
-   Use small public datasets and respect their licenses and privacy.
-   Never report only accuracy when another metric is more appropriate.
-   Keep a record of failed experiments; mistakes are useful evidence.
-   Do not compare your progress with someone else's timeline.
-   Build fewer projects with clear explanations rather than many copied
    projects.
-   Revisit fundamentals whenever an advanced topic feels confusing.

**Your first milestone is simple: finish the first 14 days, understand
Python fundamentals, and push your first mini-project to GitHub.**

Machine Learning mastery comes from understanding, implementation,
careful evaluation and consistent practice---not from completing a
playlist.
