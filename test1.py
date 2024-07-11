import numpy
PROBS = {

    # Unconditional probabilities for having gene
    "gene": {
        2: 0.01,
        1: 0.03,
        0: 0.96
    },

    "trait": {

        # Probability of trait given two copies of gene
        2: {
            True: 0.65,
            False: 0.35
        },

        # Probability of trait given one copy of gene
        1: {
            True: 0.56,
            False: 0.44
        },

        # Probability of trait given no gene
        0: {
            True: 0.01,
            False: 0.99
        }
    },

    # Mutation probability
    "mutation": 0.01
}



def joint_probability(people, one_gene, two_genes, have_trait):
    """
    Compute and return a joint probability.

    The probability returned should be the probability that
        * everyone in set `one_gene` has one copy of the gene, and
        * everyone in set `two_genes` has two copies of the gene, and
        * everyone not in `one_gene` or `two_gene` does not have the gene, and
        * everyone in set `have_trait` has the trait, and
        * everyone not in set` have_trait` does not have the trait.
    """
    prob_list = []
    gene_pass_gene = {}  # represents the number of genes a person has and how many gene will that person pass to their child

    for person in people:
        if person in two_genes:
            gene_pass_gene[person] = [2, 1]

        elif person in one_gene:
            gene_pass_gene[person] = [1, 0.5]

        else:
            gene_pass_gene[person] = [0, 0]
    for person in people:
        if people[person]["father"] is None:
                prob_list.append(PROBS["gene"][gene_pass_gene[person][0]] * PROBS["trait"][gene_pass_gene[person][0]][person in have_trait])

        else:
            print("else", person)
            p_f_m = abs(gene_pass_gene[people[person]["father"]][1] - PROBS["mutation"])
            p_m_m = abs(gene_pass_gene[people[person]["mother"]][1] - PROBS["mutation"])

            if gene_pass_gene[person][0] == 1:
                print("if")
                p_g = (p_f_m * (1-p_m_m)) + (p_m_m * (1-p_f_m))

            elif gene_pass_gene[person][0] == 2:
                p_g = p_f_m + p_m_m

            else:
                p_g = 1 - p_f_m + 1 - p_m_m

            prob_list.append(p_g * PROBS["trait"][gene_pass_gene[person][0]][person in have_trait])
    return prob_list




people = {"James": {"name": "James", "mother": None, "father": None, "trait": True},
          "lily": {"name": "lily", "mother": None, "father": None, "trait": False},
          "harry": {"name": "harry", "mother": "lily", "father": "James", "trait": None}}

one_gene = {"harry"}
two_genes = {"James"}
have_trait = {"James"}

p = joint_probability(people, one_gene, two_genes, have_trait)

print(numpy.product(p))

for i in range(3):
    pass

print(i)

