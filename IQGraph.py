import numpy as np
import matplotlib.pyplot as plt

plt.title("State IQ vs Sentiment on Trump and Biden")
plt.xlabel("State IQ")
plt.ylabel("State Sentiment")
plt.xlim([94, 105])
plt.ylim([-0.2, 0.2])

X_trump = np.array([95.7, 99.0, 97.4, 97.5, 95.5, 101.6, 103.1, 100.4, 98.4, 98.0, 95.6, 101.4, 99.9, 101.7, 103.2, 102.8, 99.4, 95.3, 103.4, 99.7, 104.3, 100.5, 103.7, 94.2, 101.0, 103.4, 102.3, 96.5, 104.2, 102.8, 85.7, 100.7, 100.2, 103.8, 101.8, 99.3, 101.2, 101.5, 99.5, 98.4, 102.8, 97.7, 100.0, 101.1, 103.9, 101.9, 101.9, 98.7, 102.9, 102.4])
Y_trump = np.array([0.0412, 0.0819, 0.0096, -0.0194, -0.0144, 0.0043, -0.0123, -0.0687, 0.0115, 0.0166, 0.0066, -0.0207, -0.0327, 0.0844, -0.0513, 0.0395, 0.0218, 0.0667, 0.0089, -0.0412, -0.0317, -0.0513, -0.0025, 0.0230, -0.0401, -0.0509, 0.0499, 0.0143, -0.0265, -0.0084, 0.0395, -0.0390, 0.0064, -0.0630, -0.0105, -0.0384, -0.0342, -0.0710, 0.0111, -0.0506, 0.0864, 0.0319, -0.0141, -0.0050, -0.1301, -0.0273, -0.0355, 0.0103, -0.0287, 0.0146])
X_biden = np.array([95.7, 99.0, 97.4, 97.5, 95.5, 101.6, 103.1, 100.4, 98.4, 98.0, 95.6, 101.4, 99.9, 101.7, 103.2, 102.8, 99.4, 95.3, 103.4, 99.7, 104.3, 100.5, 103.7, 94.2, 101.0, 103.4, 102.3, 96.5, 104.2, 102.8, 85.7, 100.7, 100.2, 103.8, 101.8, 99.3, 101.2, 101.5, 99.5, 98.4, 102.8, 97.7, 100.0, 101.1, 103.9, 101.9, 101.9, 98.7, 102.9, 102.4])
Y_biden = np.array([0.0672, 0.0216, 0.0701, 0.0479, 0.1033, 0.1152, 0.0647, 0.1641, 0.0784, 0.0884, 0.0465, 0.0654, 0.0902, 0.1575, 0.0850, 0.1311, 0.0650, 0.1860, 0.1268, 0.0576, 0.0994, 0.0588, 0.0934, 0.0437, 0.0791, 0.0526, 0.0753, 0.1240, 0.0425, 0.0782, 0.1416, 0.0890, 0.1005, 0.0964, 0.0839, 0.0850, 0.0793, 0.0910, 0.1014, 0.0163, 0.1721, 0.1106, 0.0775, 0.0409, 0.0433, 0.1045, 0.0962, 0.0636, 0.1153, 0.0520])
S_trump = np.array([860, 311, 2922, 687, 31156, 3618, 2207, 252, 16634, 2945, 706, 608, 6777, 1556, 880, 900, 1484, 2162, 398, 3925, 4865, 3065, 1821, 241, 2440, 188, 394, 2388, 2295, 5045, 502, 22881, 3415, 483, 3871, 847, 3197, 7012, 312, 1117, 1223, 3909, 16491, 1309, 911, 2489, 3152, 300, 1480, 269])
S_biden = np.array([878, 429, 3328, 518, 25816, 2687, 1612, 338, 13310, 3256, 635, 404, 5500, 1552, 572, 888, 1196, 1836, 317, 3282, 3892, 3080, 1622, 266, 1877, 311, 374, 2233, 1594, 3961, 446, 21005, 3054, 289, 4413, 806, 2335, 5403, 278, 1208, 1363, 3874, 14191, 1094, 234, 2226, 2305, 367, 1657, 238])

annotations=["Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Delaware", "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota", "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey", "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Vermont", "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"]

plt.scatter(X_trump,Y_trump, c="red", s=S_trump/50)
plt.scatter(X_biden,Y_biden, c="blue", s=S_biden/50)
plt.plot([94,105], [0,0], c="black", linestyle="dashed")

m_trump, b_trump = np.polyfit(X_trump, Y_trump, 1)
plt.plot(X_trump, m_trump*X_trump+b_trump, color='red')

m_biden, b_biden = np.polyfit(X_biden, Y_biden, 1)
plt.plot(X_biden, m_biden*X_biden+b_biden, color='blue')


# for i, label in enumerate(annotations):
#     plt.annotate(label, (X_trump[i], Y_trump[i]))
#     plt.annotate(label, (X_biden[i], Y_biden[i]))

plt.show()

