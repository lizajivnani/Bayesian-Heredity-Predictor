<h1> Baysian GJB2 gene heredity predictor </h1>

The project focuses on the GJB2 gene, mutations of which are a leading cause of hearing impairment in newborns. The AI uses a Bayesian Network to model the relationships between genes, traits, and family members, making inferences about the probability of individuals having certain genes or traits.


![image](https://github.com/user-attachments/assets/7dbe7f99-c1b4-4483-9c2d-30943b980361)



Features:
1) Calculates probability distributions for gene presence and trait expression
2) Handles family data with information about parents and observed traits
3) Uses a Bayesian Network model for genetic inheritance and trait expression


Run the program using:
>> python heredity.py [data_filename]


Project Structure:

heredity.py: Main Python script containing the AI logic
data/: Directory containing CSV files with family data
PROBS: Dictionary in heredity.py with probability constants

Key Functions Implemented:
1) joint_probability: Compute the joint probability of a given set of gene and trait distributions.
2) update: Update the probability distributions based on new joint probability calculations.
3) normalize: Normalize the probability distributions to ensure they sum to 1.

Additional Information:
The project uses a simplified model of genetic inheritance and trait expression.
Probabilities are based on the hearing impairment version of the GJB2 gene but can be adapted for other genes and traits.

Acknowledgments:
This project was implemented as part of the coursework for Harvard University's CS50 Introduction to Artificial Intelligence with Python.
