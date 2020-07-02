
# coding: utf-8

# ---
# 
# _You are currently looking at **version 1.1** of this notebook. To download notebooks and datafiles, as well as get help on Jupyter notebooks in the Coursera platform, visit the [Jupyter Notebook FAQ](https://www.coursera.org/learn/python-social-network-analysis/resources/yPcBs) course resource._
# 
# ---

# # Assignment 1 - Creating and Manipulating Graphs
# 
# Eight employees at a small company were asked to choose 3 movies that they would most enjoy watching for the upcoming company movie night. These choices are stored in the file `Employee_Movie_Choices.txt`.
# 
# A second file, `Employee_Relationships.txt`, has data on the relationships between different coworkers. 
# 
# The relationship score has value of `-100` (Enemies) to `+100` (Best Friends). A value of zero means the two employees haven't interacted or are indifferent.
# 
# Both files are tab delimited.

# In[1]:


import networkx as nx
import pandas as pd
import numpy as np
from networkx.algorithms import bipartite


# This is the set of employees
employees = set(['Pablo',
                 'Lee',
                 'Georgia',
                 'Vincent',
                 'Andy',
                 'Frida',
                 'Joan',
                 'Claude'])

# This is the set of movies
movies = set(['The Shawshank Redemption',
              'Forrest Gump',
              'The Matrix',
              'Anaconda',
              'The Social Network',
              'The Godfather',
              'Monty Python and the Holy Grail',
              'Snakes on a Plane',
              'Kung Fu Panda',
              'The Dark Knight',
              'Mean Girls'])


# you can use the following function to plot graphs
# make sure to comment it out before submitting to the autograder
def plot_graph(G, weight_name=None):
    '''
    G: a networkx G
    weight_name: name of the attribute for plotting edge weights (if G is weighted)
    '''
    get_ipython().magic('matplotlib notebook')
    import matplotlib.pyplot as plt
    
    plt.figure()
    pos = nx.spring_layout(G)
    edges = G.edges()
    weights = None
    
    if weight_name:
        weights = [int(G[u][v][weight_name]) for u,v in edges]
        labels = nx.get_edge_attributes(G,weight_name)
        nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)
        nx.draw_networkx(G, pos, edges=edges, width=weights);
    else:
        nx.draw_networkx(G, pos, edges=edges);


# ### Question 1
# 
# Using NetworkX, load in the bipartite graph from `Employee_Movie_Choices.txt` and return that graph.
# 
# *This function should return a networkx graph with 19 nodes and 24 edges*

# In[11]:


def answer_one():
        
    # Your Code Here
    G1_df = pd.read_csv('Employee_Movie_Choices.txt', sep='\t',
                       header=None, skiprows = 1, names=['Employees', 'Movies'])
    G1 = nx.from_pandas_dataframe(G1_df, 'Employees', 'Movies')
    return G1 # Your Answer Here
answer_one()


# ### Question 2
# 
# Using the graph from the previous question, add nodes attributes named `'type'` where movies have the value `'movie'` and employees have the value `'employee'` and return that graph.
# 
# *This function should return a networkx graph with node attributes `{'type': 'movie'}` or `{'type': 'employee'}`*

# In[12]:


def answer_two():
    
    # Your Code Here
    G2 = answer_one()
    G2.add_nodes_from(employees, bipartite=0, type = 'employee') 
    G2.add_nodes_from(movies, bipartite=1, type = 'movie')
    return G2 # Your Answer Here
answer_two()


# ### Question 3
# 
# Find a weighted projection of the graph from `answer_two` which tells us how many movies different pairs of employees have in common.
# 
# *This function should return a weighted projected graph.*

# In[9]:


def answer_three():
        
    # Your Code Here
    G3 = answer_two()
    weighted_projection = bipartite.weighted_projected_graph(G3, employees)
    return weighted_projection # Your Answer Here
#plot_graph(answer_three())
answer_three()


# ### Question 4
# 
# Suppose you'd like to find out if people that have a high relationship score also like the same types of movies.
# 
# Find the Pearson correlation ( using `DataFrame.corr()` ) between employee relationship scores and the number of movies they have in common. If two employees have no movies in common it should be treated as a 0, not a missing value, and should be included in the correlation calculation.
# 
# *This function should return a float.*

# In[13]:


def answer_four():
        
    # Your Code Here
    G4 = pd.DataFrame(answer_three().edges(data=True), columns=['Emp1', 'Emp2', 'movies_in_common'])
    G4['movies_in_common'] = G4['movies_in_common'].map(lambda x: x['weight'])
    G4_duplicate = G4.copy()
    G4_duplicate.rename(columns={'Emp1': 'Emp2', 'Emp2': 'Emp1'}, inplace=True)
    G4_common_movies = pd.concat([G4, G4_duplicate], ignore_index=True)
    
    G4_employee_rel = pd.read_csv('Employee_Relationships.txt', sep='\t', 
                   header=None, names=['Emp1', 'Emp2', 'Relationship'])
    
    G4_merged = pd.merge(G4_employee_rel, G4_common_movies, how='left')
    G4_merged['movies_in_common'].fillna(value=0, inplace=True)
    correlation_score = G4_merged['movies_in_common'].corr(G4_merged['Relationship'])
    
    return correlation_score # Your Answer Here

answer_four()

