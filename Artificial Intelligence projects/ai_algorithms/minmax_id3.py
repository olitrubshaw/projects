import math
import statistics
'''
#first table with values in
table1 = [
    [1, 0, "Y", "A", True],
    [1, 1, "N", "A", False],
    [2, 0, "N", "B", False],
    [2, 1, "N", "C", False],
    [3, 0, "N", "C", True],
    [3, 1, "Y", "A", False],
    [3, 0, "Y", "B", True],
    [3, 1, "Y", "A", False],
    [1, 0, "N", "A", False],
    [1, 1, "Y", "B", True],
    [1, 0, "Y", "B", True],
    [1, 1, "N", "B", False],
    [2, 0, "Y", "C", False]
]

#representation for each colmn in table1
features = ["Industry", "Size", "Quoted", "Category"]

#function for gini index
def gini(rows):
    if len(rows) == 0:
        return 0
    trueCount = sum(row[4] == True for row in rows)
    falseCount = sum(row[4] == False for row in rows)
    p_true = trueCount / len(rows)
    p_false = falseCount / len(rows)
    return 1 - (p_true ** 2 - p_false ** 2)

def combined_gini(table1, feature_index):
    groups = {}
    for row in table1:
        value = row[feature_index]
        if value not in groups:
            groups[value] = []
        groups[value].append(row)
    total_gini = 0
    for group in groups.values():
        weight = len(group) / len(table1)
        total_gini += weight * gini(group)
    return total_gini

for i, feature in enumerate(features):
    score = combined_gini(table1, i)
    print(feature, ":", round(score, 4))

'''    
 #values for second table
table2 = [
    ["Yes", "Single", 125, "No"],
    ["No", "Married", 100, "No"],
    ["No", "Single", 70, "No"],
    ["Yes", "Divorced", 120, "No"],
    ["No", "Married", 95, "Yes"],
    ["No", "Married", 60, "No"],
    ["Yes", "Divorced", 220, "No"],
    ["No", "Single", 85, "Yes"],
    ["No", "Married", 75, "No"],
    ["No", "Single", 90, "Yes"]
]

#create a threshold for salary row
threshold = statistics.median(row[2] for row in table2)
print("Median threshold for 'Income':", threshold)

for row in table2:
    if row[2] <= threshold:
        row[2] = "Low"
    else:
        row[2] = "High"

print(table2)

def entropy(rows, target_index):
    if len(rows) == 0:
        return 0
    counts = {}
    for row in rows:
        target = row
        counts[target] = counts.get(target, 0) + 1
    result = 0
    for count in counts.values():
        p = count / len(rows)
        result -= p * math.log2(p)
    return result
 #function to implement id3 algorithm
def id3(rows, features_indecies, target_index):
    targets = [row[target_index] for row in rows]
    if len(set(targets)) == 1:
        return targets[0]
    if not features_indecies:
        return max(set(targets), key=targets.count)
    base_entropy = entropy(rows, target_index)
    best_gain = 0
    best_feature = None
    for feature_index in features_indecies:
        groups = {}
        for row in rows:
            value = row[feature_index]
            groups.setdefault(value, []).append(row)
        new_entropy = 0
        for group in groups.values():
            weight = len(group) / len(rows)
            new_entropy += (weight * entropy(group, target_index))
        gain = base_entropy - new_entropy
        if gain > best_gain:
            best_gain = gain
            best_feature = feature_index
    if best_feature is None:
        return max(set(targets), key=targets.count)
    tree = {best_feature: {}}
    for row in rows:
        value = row[best_feature]
        groups.setdefault(value, []).append(row)
    remaining_features = [i for i in features_indecies if i != best_feature]
    for value, group in groups.items():
        tree[best_feature][value] = id3(group, remaining_features, target_index)
    return tree

features = ["Refund", "Marital Status", "Income"]
tree = id3(table2, [0, 1, 2], 3)
print(tree)