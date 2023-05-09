import pandas as pd
import recordlinkage

# Load the datasets
google_df = pd.read_excel('C:/Users/pc/Desktop/progetti data management/data-management-project/google_indirizzo_pulito.xlsx', header=None, names=['ID', 'Address'])
trip_df = pd.read_excel('C:/Users/pc/Desktop/progetti data management/data-management-project/trip_indirizzo_pulito_excel.xlsx', header=None, names=['ID', 'Address'])

# Initialize the indexers
indexer = recordlinkage.Index()
indexer.block('Address')
candidate_links = indexer.index(google_df, trip_df)

# Define the comparison functions
comp_func = recordlinkage.compare.String()

# Compare the datasets
compare_cl = recordlinkage.Compare()
compare_cl.string('Address', 'Address', method=comp_func, threshold=0.85)

# Compute the similarity matrix
similarity_matrix = compare_cl.compute(candidate_links, google_df, trip_df)

# Select the record pairs with a similarity score above the threshold
matches = similarity_matrix[similarity_matrix.sum(axis=1) > 1.5]

# Save the linked dataset
linked_df = pd.merge(google_df, trip_df, how='inner', left_index=True, right_index=True, suffixes=('_google', '_trip'))
print(linked_df)
linked_df.to_excel('linked_records.xlsx', index=False)
